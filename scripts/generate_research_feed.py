import os
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path
from google import genai

KST = timezone(timedelta(hours=9))
NOW_KST = datetime.now(KST)
TODAY_STR = NOW_KST.strftime("%Y-%m-%d")
DATE_HEADER = NOW_KST.strftime("%Y-%m-%d %H:%M:%S +0900")

ARXIV_QUERIES = [
    "cat:cs.RO AND (manipulation OR grasping OR deformable OR \"point cloud\" OR \"physical AI\" OR \"world model\")",
    "cat:cs.CV AND (\"point cloud\" OR \"3D vision\" OR \"world model\" OR \"RGB-D\")",
]


def fetch_arxiv_papers(max_results: int = 10) -> list[dict]:
    papers = []
    for query in ARXIV_QUERIES:
        params = urllib.parse.urlencode({
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        url = f"http://export.arxiv.org/api/query?{params}"
        with urllib.request.urlopen(url, timeout=20) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns):
            title = (entry.findtext("atom:title", "", ns) or "").strip().replace("\n", " ")
            summary = (entry.findtext("atom:summary", "", ns) or "").strip().replace("\n", " ")
            link = entry.findtext("atom:id", "", ns) or ""
            published = entry.findtext("atom:published", "", ns) or ""
            papers.append({
                "title": title,
                "summary": summary,
                "link": link,
                "published": published,
            })
    return papers


def generate_post(papers: list[dict]) -> str:
    api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    papers_json = json.dumps(papers[:12], ensure_ascii=False, indent=2)
    prompt = f"""당신은 피지컬 AI(Physical AI), 3D Vision(Point Cloud, RGB-D), World Model 분야를 연구하는 엔지니어를 위한 리서치 피드 에디터입니다.

아래 arXiv 최신 논문 목록에서 오늘({TODAY_STR}) 가장 가치 있는 논문 1편을 선정해, Jekyll `_research_feed` 포스트 마크다운 전체를 작성하세요.
선정 우선순위:
1. Physical AI / Robot Manipulation / 비정형·정량 파지(Deformable, Granular, Food grasping 등)
2. 3D Vision / Point Cloud / RGB-D 인식 및 파지
3. World Model / Frontier AI & Robotics

출력 형식 (반드시 아래 YAML frontmatter로 시작하고, 코드블록(```)으로 감싸지 마세요):
---
layout: feed_note
title: "논문 핵심을 담은 한국어 제목"
date: {DATE_HEADER}
channel: research-papers
channel_label: "Research Papers"
summary: "2~3문장 핵심 요약 (공개일, 핵심 방법, 검증 범위 및 한계 포함)"
---

본문 구성 (한국어, 과장 없이 초록에 근거한 사실만 작성):
1. 도입 문단 (논문 제목, arXiv 링크, 핵심 문제의식)
2. `## 핵심 방법론` (데이터 흐름 및 구조 설명)
3. `## 실험 및 검증` (보고된 실험 환경과 한계)
4. `## 엔지니어링 관점의 시사점` (실제 로봇/3D 비전 시스템 적용 시 고려사항)

후보 논문 목록:
{papers_json}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    text = (response.text or "").strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text + "\n"


def main() -> None:
    out_dir = Path("_research_feed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{TODAY_STR}-research-papers.md"
    if out_file.exists():
        print(f"Already exists: {out_file}")
        return

    papers = fetch_arxiv_papers()
    if not papers:
        raise RuntimeError("No papers fetched from arXiv.")

    content = generate_post(papers)
    out_file.write_text(content, encoding="utf-8")
    print(f"Generated: {out_file}")


if __name__ == "__main__":
    main()
