import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from google import genai
from google.genai import types

KST = timezone(timedelta(hours=9))
NOW_KST = datetime.now(KST)
TODAY_STR = NOW_KST.strftime("%Y-%m-%d")
DATE_HEADER = NOW_KST.strftime("%Y-%m-%d %H:%M:%S +0900")
OUT_DIR = Path("_research_feed")

MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-4-hydrogen")

ARXIV_QUERIES = [
    'cat:cs.RO AND (manipulation OR grasping OR deformable OR "point cloud" OR "physical AI" OR "world model" OR VLA OR VLM)',
    'cat:cs.CV AND ("point cloud" OR "3D vision" OR "world model" OR "RGB-D" OR "embodied")',
]

AI_ROBOTICS_RSS_FEEDS = [
    ("IEEE Spectrum Robotics", "https://spectrum.ieee.org/feeds/topic/robotics.rss"),
    ("MIT News Robotics", "https://news.mit.edu/topic/mitrobotics-rss.xml"),
    ("Hugging Face Blog", "https://huggingface.co/blog/feed.xml"),
    ("Google DeepMind Blog", "https://deepmind.google/blog/rss.xml"),
    ("NVIDIA Blog", "https://blogs.nvidia.com/feed/"),
]


def http_get(url: str, timeout: int = 30, retries: int = 3) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "nayana224-research-feed/2.0 (+https://nayana224.github.io/)"},
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:
            if attempt == retries - 1:
                raise
            print(f"Fetch failed ({url}, attempt {attempt + 1}/{retries}): {exc}")
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Unreachable: {url}")


def load_existing_references() -> set[str]:
    """Collect arXiv IDs and URLs already cited in _research_feed/ to avoid duplicates."""
    seen: set[str] = set()
    if not OUT_DIR.exists():
        return seen
    arxiv_re = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
    url_re = re.compile(r"https?://[^\s\)\"'>]+")
    for md_file in OUT_DIR.glob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in arxiv_re.findall(text):
            seen.add(m)
        for u in url_re.findall(text):
            seen.add(u.rstrip(".,;:"))
    return seen


def extract_arxiv_id(url: str) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})", url or "")
    return m.group(1) if m else ""


def strip_html(text: str) -> str:
    cleaned = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", cleaned).strip()


def fetch_arxiv_papers(seen_refs: set[str], per_query: int = 8) -> list[dict]:
    papers: list[dict] = []
    seen_ids: set[str] = set()
    for query in ARXIV_QUERIES:
        params = urllib.parse.urlencode({
            "search_query": query,
            "start": 0,
            "max_results": per_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        url = f"https://export.arxiv.org/api/query?{params}"
        try:
            xml_data = http_get(url, timeout=45, retries=3)
        except Exception as exc:
            print(f"arXiv query failed: {exc}")
            continue
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        query_count = 0
        for entry in root.findall("atom:entry", ns):
            link = (entry.findtext("atom:id", "", ns) or "").strip()
            aid = extract_arxiv_id(link)
            if aid and (aid in seen_refs or aid in seen_ids):
                continue
            if aid:
                seen_ids.add(aid)
            title = re.sub(r"\s+", " ", entry.findtext("atom:title", "", ns) or "").strip()
            summary = re.sub(r"\s+", " ", entry.findtext("atom:summary", "", ns) or "").strip()
            published = (entry.findtext("atom:published", "", ns) or "").strip()
            papers.append({
                "title": title,
                "summary": summary,
                "link": link,
                "published": published,
            })
            query_count += 1
            if query_count >= 6:
                break
    return papers


def fetch_ai_robotics_news(seen_refs: set[str], per_feed: int = 4) -> list[dict]:
    items: list[dict] = []
    seen_links: set[str] = set()
    for source_name, feed_url in AI_ROBOTICS_RSS_FEEDS:
        try:
            xml_data = http_get(feed_url, timeout=25, retries=2)
            root = ET.fromstring(xml_data)
        except Exception as exc:
            print(f"RSS fetch failed ({source_name}): {exc}")
            continue

        # Support both RSS 2.0 (<item>) and Atom (<entry>)
        entries = root.findall(".//item")
        is_atom = False
        if not entries:
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entries = root.findall(".//atom:entry", ns)
            is_atom = True

        count = 0
        for entry in entries:
            if is_atom:
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                title = strip_html(entry.findtext("atom:title", "", ns))
                link_el = entry.find("atom:link", ns)
                link = (link_el.attrib.get("href", "") if link_el is not None else "").strip()
                summary = strip_html(
                    entry.findtext("atom:summary", "", ns)
                    or entry.findtext("atom:content", "", ns)
                )[:1200]
                published = (
                    entry.findtext("atom:published", "", ns)
                    or entry.findtext("atom:updated", "", ns)
                    or ""
                ).strip()
            else:
                title = strip_html(entry.findtext("title", ""))
                link = (entry.findtext("link", "") or "").strip()
                summary = strip_html(entry.findtext("description", ""))[:1200]
                published = (entry.findtext("pubDate", "") or "").strip()

            norm_link = link.rstrip(".,;:")
            if not title or not norm_link or norm_link in seen_refs or norm_link in seen_links:
                continue
            seen_links.add(norm_link)
            items.append({
                "source": source_name,
                "title": title,
                "summary": summary,
                "link": norm_link,
                "published": published,
            })
            count += 1
            if count >= per_feed:
                break
    return items


def call_gemini(prompt: str) -> str:
    api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_level="MEDIUM"),
                ),
            )
            text = (response.text or "").strip()
            if text.startswith("```"):
                lines = text.splitlines()
                if lines and lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                text = "\n".join(lines).strip()
            if not text.startswith("---"):
                raise ValueError("Generated output missing YAML frontmatter.")
            return text + "\n"
        except Exception as exc:
            if attempt == 2:
                raise
            print(f"Gemini call failed (attempt {attempt + 1}/3): {exc}")
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("Gemini generation failed.")


def generate_research_paper_post(papers: list[dict]) -> str:
    papers_json = json.dumps(papers[:12], ensure_ascii=False, indent=2)
    prompt = f"""당신은 피지컬 AI(Physical AI), 로봇 매니퓰레이션, 3D Vision, World Model 분야를 연구하는 엔지니어를 위한 리서치 피드 에디터입니다.

아래 arXiv 최신 논문 목록에서 오늘({TODAY_STR}) 가장 엔지니어링·연구 가치가 높은 논문 1편을 선정해, Jekyll `_research_feed` 포스트 마크다운 전체를 작성하세요.
선정 우선순위:
1. Robot Manipulation / VLA / VLM / Robot Learning / 비정형·정밀 파지
2. 3D Vision / Point Cloud / RGB-D 인식 및 제어 결합
3. World Model / Physical AI

출력 형식 (반드시 아래 YAML frontmatter로 시작하고, 코드블록(```)으로 감싸지 마세요):
---
layout: feed_note
title: "논문의 핵심 메커니즘이나 수치가 드러나는 구체적인 한국어 제목"
date: {DATE_HEADER}
channel: research-papers
channel_label: "Research Papers"
summary: "2~3문장 핵심 요약 (공개일, 핵심 방법, 검증 범위 및 한계 포함)"
---

작성 원칙 (매우 중요):
- **사실 엄수**: 초록에 없는 수치·실험 조건·성능을 절대 지어내지 마세요. 초록에 정량 수치가 없으면 억지로 표를 만들지 말고, 확인된 내용과 초록만으로 확인되지 않는 한계를 명확히 구분해 서술하세요.
- **제목 & 소제목 품질**: `## 핵심 방법론`, `## 실험 및 검증` 같은 기계적인 소제목 대신, 이 논문의 핵심 통찰이 드러나는 자연스러운 서술형 소제목 3개를 사용하세요.
- **문체**: 도입부는 엔지니어가 공감할 구체적인 문제 제기(질문 또는 현장의 병목)로 시작하고, 논문 원제목과 arXiv 링크를 자연스럽게 포함하세요.
- **구성**:
  1. 도입 문단 (2~3문장): 문제 제기 + 논문 소개(공개일, arXiv 링크)
  2. 소제목 1: 기존 접근의 병목과 이 논문이 바꾼 핵심 아이디어 (데이터/처리 흐름을 한 줄 `A → B → C` 형태로 포함)
  3. 소제목 2: 초록에서 확인된 검증 범위·수치와 확인되지 않은 한계(Caveat)
  4. 소제목 3: 로봇·AI 시스템 엔지니어 관점의 실무 시사점 (2~3개 불릿)

후보 논문 목록:
{papers_json}
"""
    return call_gemini(prompt)


def generate_ai_robotics_post(news_items: list[dict]) -> str:
    news_json = json.dumps(news_items[:15], ensure_ascii=False, indent=2)
    prompt = f"""당신은 피지컬 AI(Physical AI), 로보틱스, 멀티모달 AI 분야의 최신 동향을 정리하는 리서치 피드 에디터입니다.

아래 최신 로보틱스·AI 소식 목록에서 오늘({TODAY_STR}) 로보틱스·AI 연구자에게 가장 의미 있는 소식 1건을 선정해, Jekyll `_research_feed` 포스트 마크다운 전체를 작성하세요.
선정 우선순위:
1. 로봇 하드웨어/파운데이션 모델/시뮬레이션(Isaac, VLA, World Model, 휴머노이드, 매니퓰레이션) 발표
2. 오픈소스 모델·데이터셋·프레임워크 릴리스
3. 산업/연구기관의 실질적인 기술 진전 (단순 투자·인사·마케팅 기사 제외)

출력 형식 (반드시 아래 YAML frontmatter로 시작하고, 코드블록(```)으로 감싸지 마세요):
---
layout: feed_note
title: "핵심 변화나 구체적 포인트를 담은 한국어 제목"
date: {DATE_HEADER}
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "2~3문장 핵심 요약 (발표 주체·시점, 핵심 내용, 해석 시 주의할 한계 포함)"
---

작성 원칙 (매우 중요):
- **사실 엄수**: 제공된 요약과 출처에 없는 수치나 세부 사항을 추측해서 쓰지 마세요. 발표 내용만으로 확인되지 않는 부분(예: 실물 일반화, 재현성, 비용)은 한계로 명확히 짚어주세요.
- **소제목 품질**: 글의 내용에 맞는 구체적이고 읽기 쉬운 소제목 3개를 사용하세요.
- **구성**:
  1. 도입 문단 (2~3문장): 왜 주목할 만한지 문제 제기 + 출처(기관/매체, 원문 링크) 명시
  2. 소제목 1: 무엇이 달라졌는지 핵심 기술·구조 정리
  3. 소제목 2: 발표에서 확인된 근거와 주의해서 읽어야 할 한계
  4. 소제목 3: 로보틱스·AI 연구자/엔지니어 관점의 의미 (2~3개 불릿)

후보 소식 목록:
{news_json}
"""
    return call_gemini(prompt)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seen_refs = load_existing_references()
    errors: list[str] = []

    # 1. Research Papers channel
    papers_file = OUT_DIR / f"{TODAY_STR}-research-papers.md"
    if papers_file.exists():
        print(f"Already exists: {papers_file}")
    else:
        try:
            papers = fetch_arxiv_papers(seen_refs)
            if not papers:
                raise RuntimeError("No new papers fetched from arXiv.")
            content = generate_research_paper_post(papers)
            papers_file.write_text(content, encoding="utf-8")
            print(f"Generated: {papers_file}")
        except Exception as exc:
            msg = f"research-papers failed: {exc}"
            print(msg)
            errors.append(msg)

    # 2. AI & Robotics channel
    news_file = OUT_DIR / f"{TODAY_STR}-ai-robotics.md"
    if news_file.exists():
        print(f"Already exists: {news_file}")
    else:
        try:
            news_items = fetch_ai_robotics_news(seen_refs)
            if not news_items:
                raise RuntimeError("No new AI & Robotics items fetched from RSS feeds.")
            content = generate_ai_robotics_post(news_items)
            news_file.write_text(content, encoding="utf-8")
            print(f"Generated: {news_file}")
        except Exception as exc:
            msg = f"ai-robotics failed: {exc}"
            print(msg)
            errors.append(msg)

    if len(errors) == 2:
        raise RuntimeError("Both channels failed: " + " | ".join(errors))


if __name__ == "__main__":
    main()
