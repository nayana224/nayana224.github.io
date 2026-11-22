import argparse
import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

KST = timezone(timedelta(hours=9))
NOW_KST = datetime.now(KST)
OUT_DIR = Path("_research_feed")
IMG_DIR = Path("images/research-feed")

MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-4-hydrogen")
FALLBACK_MODELS = [MODEL_NAME, "gemini-2.5-flash", "gemini-2.0-flash"]

ARXIV_QUERIES = [
    'cat:cs.RO AND (manipulation OR grasping OR deformable OR "point cloud" OR "physical AI" OR "world model" OR VLA OR VLM)',
    'cat:cs.CV AND ("point cloud" OR "3D vision" OR "world model" OR "RGB-D" OR "embodied")',
]

AI_ROBOTICS_RSS_FEEDS = [
    ("IEEE Spectrum Robotics", "https://spectrum.ieee.org/feeds/topic/robotics.rss"),
    ("MIT News Robotics", "https://news.mit.edu/topic/mitrobotics-rss.xml"),
    ("Hugging Face Blog", "https://huggingface.co/blog/feed.xml"),
    ("BAIR Blog", "https://bair.berkeley.edu/blog/feed.xml"),
    ("NVIDIA Blog", "https://blogs.nvidia.com/feed/"),
]


def http_get(url: str, timeout: int = 30, retries: int = 3) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "nayana224-research-feed/2.1 (+https://nayana224.github.io/)"},
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


def fetch_arxiv_papers(seen_refs: set[str], per_query: int = 15) -> list[dict]:
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
                "arxiv_id": aid,
                "title": title,
                "summary": summary,
                "link": link,
                "published": published,
            })
            query_count += 1
            if query_count >= 10:
                break
    return papers


def fetch_ai_robotics_news(seen_refs: set[str], per_feed: int = 8) -> list[dict]:
    items: list[dict] = []
    seen_links: set[str] = set()
    for source_name, feed_url in AI_ROBOTICS_RSS_FEEDS:
        try:
            xml_data = http_get(feed_url, timeout=25, retries=2)
            root = ET.fromstring(xml_data)
        except Exception as exc:
            print(f"RSS fetch failed ({source_name}): {exc}")
            continue

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


def extract_pdf_figures_and_text(arxiv_id: str, date_str: str, max_figs: int = 2) -> tuple[list[tuple[str, bytes]], str]:
    """Download arXiv PDF, crop up to `max_figs` key figures from pages 1-4, and extract intro text."""
    if not fitz or not arxiv_id:
        return [], ""

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        pdf_bytes = http_get(pdf_url, timeout=45, retries=2)
    except Exception as exc:
        print(f"PDF download failed ({pdf_url}): {exc}")
        return [], ""

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    saved_figs: list[tuple[str, bytes]] = []
    extracted_text_parts: list[str] = []

    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception as exc:
        print(f"PDF open failed ({arxiv_id}): {exc}")
        return [], ""

    try:
        # Extract text from first 3 pages for richer context
        for p_idx in range(min(3, len(doc))):
            extracted_text_parts.append(doc[p_idx].get_text("text"))

        # Strategy 1: Caption-based crop (captures both vector TikZ/PDF diagrams and raster figures)
        chosen: list[tuple[int, fitz.Rect]] = []
        caption_patterns = ["Figure 1", "Fig. 1", "Figure 2", "Fig. 2"]
        for pat in caption_patterns:
            if len(chosen) >= max_figs:
                break
            found = False
            for p_idx in range(min(4, len(doc))):
                page = doc[p_idx]
                hits = page.search_for(pat)
                if not hits:
                    continue
                cap_rect = hits[0]
                page_rect = page.rect
                # Crop region above the caption (up to ~42% of page height) + caption line
                top_y = max(page_rect.y0 + 36, cap_rect.y0 - page_rect.height * 0.46)
                bot_y = min(page_rect.y1 - 30, cap_rect.y1 + 36)
                if bot_y - top_y < 110:
                    continue
                # Use full content width (with small horizontal margins)
                margin_x = page_rect.width * 0.06
                fig_rect = fitz.Rect(margin_x, top_y, page_rect.width - margin_x, bot_y)
                if any(cp == p_idx and (cr & fig_rect).get_area() > 0.3 * fig_rect.get_area() for cp, cr in chosen):
                    continue
                chosen.append((p_idx, fig_rect))
                found = True
                break
            if found and len(chosen) >= max_figs:
                break

        # Strategy 2: Fallback to largest raster image bboxes if caption search found fewer than max_figs
        if len(chosen) < max_figs:
            candidates: list[tuple[float, int, fitz.Rect]] = []
            for p_idx in range(min(4, len(doc))):
                page = doc[p_idx]
                page_rect = page.rect
                for img_info in page.get_image_info(xrefs=True):
                    bbox = fitz.Rect(img_info["bbox"]) & page_rect
                    w, h = bbox.width, bbox.height
                    if w < 180 or h < 90:
                        continue
                    score = (w * h) * (1.25 if p_idx < 2 else 1.0)
                    candidates.append((score, p_idx, bbox))

            candidates.sort(key=lambda x: x[0], reverse=True)
            for _, p_idx, rect in candidates:
                if any(cp == p_idx and (cr & rect).get_area() > 0.3 * rect.get_area() for cp, cr in chosen):
                    continue
                chosen.append((p_idx, rect))
                if len(chosen) >= max_figs:
                    break

        # Render and crop chosen figures cleanly at 2x resolution
        for idx, (p_idx, rect) in enumerate(chosen, start=1):
            page = doc[p_idx]
            pad = 6
            clip = fitz.Rect(
                max(page.rect.x0, rect.x0 - pad),
                max(page.rect.y0, rect.y0 - pad),
                min(page.rect.x1, rect.x1 + pad),
                min(page.rect.y1, rect.y1 + pad),
            )
            pix = page.get_pixmap(clip=clip, matrix=fitz.Matrix(2, 2), alpha=False)
            png_bytes = pix.tobytes("png")
            safe_id = arxiv_id.replace(".", "_")
            rel_path = f"/images/research-feed/{date_str}-{safe_id}-fig{idx}.png"
            out_path = IMG_DIR / f"{date_str}-{safe_id}-fig{idx}.png"
            out_path.write_bytes(png_bytes)
            saved_figs.append((rel_path, png_bytes))
            print(f"Cropped figure: {out_path}")
    finally:
        doc.close()

    intro_text = re.sub(r"\s+", " ", " ".join(extracted_text_parts))[:6000]
    return saved_figs, intro_text


def call_gemini(contents, thinking_level: str = "MEDIUM") -> str:
    api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
    last_exc: Exception | None = None
    for model_id in FALLBACK_MODELS:
        for attempt in range(2):
            try:
                cfg = types.GenerateContentConfig()
                if "gemini-4" in model_id or "gemini-2.5" in model_id:
                    cfg = types.GenerateContentConfig(
                        thinking_config=types.ThinkingConfig(thinking_level=thinking_level),
                    )
                response = client.models.generate_content(
                    model=model_id,
                    contents=contents,
                    config=cfg,
                )
                text = (response.text or "").strip()
                if text.startswith("```"):
                    lines = text.splitlines()
                    if lines and lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].startswith("```"):
                        lines = lines[:-1]
                    text = "\n".join(lines).strip()
                return text
            except Exception as exc:
                last_exc = exc
                err_str = str(exc)
                print(f"Gemini call failed ({model_id}, attempt {attempt + 1}/2): {exc}")
                # If daily quota exceeded (429PerDay) or model not found, switch to next fallback model immediately
                if "GenerateRequestsPerDay" in err_str or "404" in err_str or "NOT_FOUND" in err_str:
                    break
                time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"Gemini generation failed across all models: {last_exc}")


def select_best_paper(papers: list[dict], date_str: str) -> dict:
    """Deterministically rank candidate papers by Physical AI / Manipulation / VLA keywords (saves 1 API request/day)."""
    priority_terms = [
        ("vla", 4), ("vision-language-action", 4), ("manipulation", 3), ("grasping", 3),
        ("dexterous", 3), ("bimanual", 3), ("world model", 3), ("physical ai", 3),
        ("point cloud", 2), ("rgb-d", 2), ("3d", 2), ("sim-to-real", 2), ("isaac", 2),
        ("policy", 2), ("teleoperation", 2), ("embodied", 2),
    ]
    best_paper = papers[0]
    best_score = -1
    for idx, p in enumerate(papers[:12]):
        blob = (p["title"] + " " + p["summary"]).lower()
        score = sum(w for term, w in priority_terms if term in blob) - (idx * 0.15)
        if score > best_score:
            best_score = score
            best_paper = p
    return best_paper


def generate_research_paper_post(papers: list[dict], date_str: str, date_header: str) -> tuple[str, str]:
    paper = select_best_paper(papers, date_str)
    figs, pdf_text = extract_pdf_figures_and_text(paper["arxiv_id"], date_str, max_figs=2)

    fig_instructions = ""
    if figs:
        fig_paths = "\n".join(f"- Figure {i}: `{path}`" for i, (path, _) in enumerate(figs, start=1))
        fig_instructions = f"""
첨부된 논문 PDF에서 추출한 주요 Figure 이미지 경로:
{fig_paths}
- 본문에서 이 논문의 **핵심 Method 컨셉을 설명하는 위치**에 반드시 위 이미지를 마크다운(`![직관적인 한국어 캡션](경로)`)으로 삽입하고, 그림 속 구조/흐름을 짚어주며 독자가 Method의 컨셉을 한눈에 이해할 수 있도록 설명하세요.
"""

    prompt = f"""당신은 피지컬 AI(Physical AI), 로봇 매니퓰레이션, 3D Vision, World Model 분야를 연구하는 엔지니어를 위한 리서치 피드 에디터입니다.

아래 선정된 arXiv 논문 1편에 대해 Jekyll `_research_feed` 포스트 마크다운 전체를 작성하세요.
독자가 **논문이 주장하는 Method의 핵심 컨셉을 빠르고 직관적으로 이해**할 수 있게 쓰는 것이 최우선 목표입니다.

출력 형식 (반드시 아래 YAML frontmatter로 시작하고, 코드블록(```)으로 감싸지 마세요):
---
layout: feed_note
title: "논문의 핵심 메커니즘이나 수치가 드러나는 구체적인 한국어 제목"
date: {date_header}
channel: research-papers
channel_label: "Research Papers"
tags: ["Manipulation", "VLA / VLM"]
summary: "2~3문장 핵심 요약 (공개일, 핵심 방법, 검증 범위 및 한계 포함)"
---
(참고: `tags`는 반드시 `["Manipulation", "VLA / VLM", "World Model", "3D Vision", "Humanoid & Locomotion", "Sim & Systems"]` 중에서 가장 알맞은 1~2개만 골라 배열로 작성하세요.)
{fig_instructions}
작성 원칙 (매우 중요):
- **사실 엄수**: 논문 초록·본문·첨부 Figure에 없는 수치·실험 조건을 절대 지어내지 마세요.
- **제목 & 소제목 품질**: `## 핵심 방법론`, `## 실험 및 검증` 같은 기계적인 소제목 대신, 이 논문의 핵심 통찰이 드러나는 자연스러운 서술형 소제목 3개를 사용하세요.
- **구성**:
  1. 도입 문단 (2~3문장): 엔지니어가 공감할 구체적인 문제 제기 + 논문 원제목·공개일·arXiv 링크(`{paper['link']}`)
  2. 소제목 1 (핵심 컨셉 & Figure 해설): 기존 방식의 병목과 이 논문이 제안한 핵심 아이디어를 직관적으로 설명. 첨부 Figure가 있다면 여기에 삽입하고 그림의 흐름(`입력 → 핵심 모듈 → 출력`)을 쉽게 풀어쓰세요.
  3. 소제목 2 (검증 범위와 한계): 확인된 실험 결과·수치와 함께, 아직 검증되지 않은 한계(Caveat)를 명확히 구분해 서술.
  4. 소제목 3 (엔지니어링 시사점): 실제 로봇·AI 시스템 설계 시 참고할 실무 포인트 2~3개 불릿.

논문 메타데이터:
- Title: {paper['title']}
- Published: {paper['published']}
- Link: {paper['link']}
- Abstract: {paper['summary']}

PDF 도입부 발췌:
{pdf_text[:3500]}
"""

    contents: list = [prompt]
    for _, png_bytes in figs:
        contents.append(types.Part.from_bytes(data=png_bytes, mime_type="image/png"))

    text = call_gemini(contents, thinking_level="MEDIUM")
    if not text.startswith("---"):
        raise ValueError("Generated research-papers output missing YAML frontmatter.")
    # Inject source_url and primary image into YAML frontmatter
    extra_fm = f'source_url: "{paper["link"]}"\n'
    if figs:
        extra_fm += f'image: "{figs[0][0]}"\n'
    text = re.sub(r"^---\n", "---\n" + extra_fm, text, count=1)
    # Guarantee cropped figures are embedded even if the model omitted them
    for idx, (rel_path, _) in enumerate(figs, start=1):
        if rel_path not in text:
            img_md = f"\n![논문 주요 Figure {idx}]({rel_path})\n"
            m_h2 = re.search(r"(^## .+$)", text, flags=re.MULTILINE)
            if m_h2:
                pos = m_h2.end()
                text = text[:pos] + "\n" + img_md + text[pos:]
            else:
                text = text + "\n" + img_md
    return text + "\n", paper["arxiv_id"]


def fetch_og_image(article_url: str, date_str: str) -> str:
    """Download og:image / twitter:image from a news article into images/research-feed/."""
    if not article_url:
        return ""
    try:
        html = http_get(article_url, timeout=20, retries=2).decode("utf-8", errors="ignore")
        m = re.search(
            r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)["\']',
            html,
            flags=re.IGNORECASE,
        )
        if not m:
            m = re.search(
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\']',
                html,
                flags=re.IGNORECASE,
            )
        if not m:
            return ""
        img_url = urllib.parse.urljoin(article_url, m.group(1).strip())
        img_bytes = http_get(img_url, timeout=20, retries=2)
        if len(img_bytes) < 5000:
            return ""
        ext = ".jpg"
        lower_url = img_url.lower()
        if ".png" in lower_url:
            ext = ".png"
        elif ".webp" in lower_url:
            ext = ".webp"
        IMG_DIR.mkdir(parents=True, exist_ok=True)
        fname = f"{date_str}-ai-robotics-hero{ext}"
        (IMG_DIR / fname).write_bytes(img_bytes)
        print(f"Saved article hero image: {IMG_DIR / fname}")
        return f"/images/research-feed/{fname}"
    except Exception as exc:
        print(f"og:image fetch skipped ({article_url}): {exc}")
        return ""


def generate_ai_robotics_post(news_items: list[dict], date_str: str, date_header: str) -> tuple[str, str]:
    news_json = json.dumps(news_items[:15], ensure_ascii=False, indent=2)
    prompt = f"""당신은 피지컬 AI(Physical AI), 로보틱스, 멀티모달 AI 분야의 최신 동향을 정리하는 리서치 피드 에디터입니다.

아래 최신 로보틱스·AI 소식 목록에서 오늘({date_str}) 로보틱스·AI 연구자에게 가장 의미 있는 소식 1건을 선정해, Jekyll `_research_feed` 포스트 마크다운 전체를 작성하세요.
선정 우선순위:
1. 로봇 하드웨어/파운데이션 모델/시뮬레이션(Isaac, VLA, World Model, 휴머노이드, 매니퓰레이션) 발표
2. 오픈소스 모델·데이터셋·프레임워크 릴리스
3. 산업/연구기관의 실질적인 기술 진전 (단순 투자·인사·마케팅 기사 제외)

출력 형식 (반드시 아래 YAML frontmatter로 시작하고, 코드블록(```)으로 감싸지 마세요):
---
layout: feed_note
title: "핵심 변화나 구체적 포인트를 담은 한국어 제목"
date: {date_header}
channel: ai-robotics
channel_label: "AI & Robotics"
tags: ["Humanoid & Locomotion", "Sim & Systems"]
summary: "2~3문장 핵심 요약 (발표 주체·시점, 핵심 내용, 해석 시 주의할 한계 포함)"
---

(참고: `tags`는 반드시 `["Manipulation", "VLA / VLM", "World Model", "3D Vision", "Humanoid & Locomotion", "Sim & Systems"]` 중에서 가장 알맞은 1~2개만 골라 배열로 작성하세요.)

작성 원칙 (매우 중요):
- **사실 엄수**: 제공된 요약과 출처에 없는 수치나 세부 사항을 추측해서 쓰지 마세요. 발표 내용만으로 확인되지 않는 부분은 한계로 명확히 짚어주세요.
- **소제목 품질**: 글의 내용에 맞는 구체적이고 읽기 쉬운 소제목 3개를 사용하세요.
- **구성**:
  1. 도입 문단 (2~3문장): 왜 주목할 만한지 문제 제기 + 출처(기관/매체, 원문 링크) 명시
  2. 소제목 1: 무엇이 달라졌는지 핵심 기술·구조 정리
  3. 소제목 2: 발표에서 확인된 근거와 주의해서 읽어야 할 한계
  4. 소제목 3: 로보틱스·AI 연구자/엔지니어 관점의 의미 (2~3개 불릿)

후보 소식 목록:
{news_json}
"""
    text = call_gemini(prompt, thinking_level="MEDIUM")
    if not text.startswith("---"):
        raise ValueError("Generated ai-robotics output missing YAML frontmatter.")
    # Extract first URL in output for dedup tracking and hero image
    m = re.search(r"https?://[^\s\)\"'>]+", text)
    used_url = m.group(0).rstrip(".,;:") if m else ""
    hero_path = fetch_og_image(used_url, date_str)
    extra_fm = ""
    if used_url:
        extra_fm += f'source_url: "{used_url}"\n'
    if hero_path:
        extra_fm += f'image: "{hero_path}"\n'
    if extra_fm:
        text = re.sub(r"^---\n", "---\n" + extra_fm, text, count=1)
    if hero_path and hero_path not in text:
        m_h2 = re.search(r"(^## .+$)", text, flags=re.MULTILINE)
        img_md = f"\n![기사 대표 이미지]({hero_path})\n"
        if m_h2:
            pos = m_h2.start()
            text = text[:pos] + img_md + "\n" + text[pos:]
        else:
            text = text + "\n" + img_md
    return text + "\n", used_url


def run_for_date(date_str: str, force: bool, seen_refs: set[str]) -> list[str]:
    date_header = f"{date_str} 07:30:00 +0900"
    errors: list[str] = []

    papers_file = OUT_DIR / f"{date_str}-research-papers.md"
    if papers_file.exists() and not force:
        print(f"Already exists: {papers_file}")
    else:
        try:
            papers = fetch_arxiv_papers(seen_refs)
            if not papers:
                raise RuntimeError("No new papers fetched from arXiv.")
            content, used_aid = generate_research_paper_post(papers, date_str, date_header)
            papers_file.write_text(content, encoding="utf-8")
            if used_aid:
                seen_refs.add(used_aid)
            print(f"Generated: {papers_file}")
        except Exception as exc:
            msg = f"{date_str} research-papers failed: {exc}"
            print(msg)
            errors.append(msg)

    news_file = OUT_DIR / f"{date_str}-ai-robotics.md"
    if news_file.exists() and not force:
        print(f"Already exists: {news_file}")
    else:
        try:
            news_items = fetch_ai_robotics_news(seen_refs)
            if not news_items:
                raise RuntimeError("No new AI & Robotics items fetched from RSS feeds.")
            content, used_url = generate_ai_robotics_post(news_items, date_str, date_header)
            news_file.write_text(content, encoding="utf-8")
            if used_url:
                seen_refs.add(used_url)
            print(f"Generated: {news_file}")
        except Exception as exc:
            msg = f"{date_str} ai-robotics failed: {exc}"
            print(msg)
            errors.append(msg)

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backfill-from", default=os.environ.get("BACKFILL_FROM", ""), help="Start date YYYY-MM-DD to backfill up to today")
    parser.add_argument("--force", action="store_true", help="Overwrite existing posts for target date(s)")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seen_refs = load_existing_references()

    today_str = NOW_KST.strftime("%Y-%m-%d")
    if args.backfill_from:
        start_dt = datetime.strptime(args.backfill_from, "%Y-%m-%d").date()
        end_dt = NOW_KST.date()
        dates = []
        cur = start_dt
        while cur <= end_dt:
            dates.append(cur.strftime("%Y-%m-%d"))
            cur += timedelta(days=1)
    else:
        dates = [today_str]

    all_errors: list[str] = []
    for idx, d in enumerate(dates):
        if idx > 0:
            time.sleep(12)
        all_errors.extend(run_for_date(d, args.force, seen_refs))

    if len(dates) == 1 and len(all_errors) == 2:
        raise RuntimeError("Both channels failed: " + " | ".join(all_errors))


if __name__ == "__main__":
    main()
