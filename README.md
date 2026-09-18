# nayana224.github.io

Inpyo Lee의 개인 Robotics & AI 홈페이지입니다.

현재는 정적인 GitHub Pages 사이트를 기반으로, 연구 관심사와 프로젝트를 정리하고 Markdown으로 학습/연구 기록을 남기는 개인 아카이브 형태로 운영합니다.

## Profile

- Robotics & AI Research Intern @ KITECH
- B.S. in Mechatronics Engineering
- Minor in Intelligent Robotics
- Tech University of Korea
- Interests: VLM, VLA, Robot Learning, Robotic Manipulation, Embodied AI

## Site Structure

```text
.
├── index.html                 # 메인 프로필 / 연구 관심사 / 프로젝트
├── publications.html          # Publications
├── _config.yml                # GitHub Pages / Jekyll 설정
├── _layouts/
│   └── note.html              # Markdown note layout
├── _notes/                    # 학습 및 연구 기록 Markdown
├── notes/
│   └── index.html             # Notes 목록
├── images/
│   └── profile.jpg            # 프로필 이미지
├── stylesheets/
│   ├── styles.css             # 메인 스타일
│   └── notes.css              # Notes 스타일
└── javascripts/
    └── scale.fix.js
```

## Writing Notes

새로운 글은 `_notes/`에 Markdown 파일을 추가합니다.

예시:

```markdown
---
title: "Transformer 1회독 정리"
date: 2026-09-19
category: Deep Learning
summary: "Attention과 Multi-Head Attention을 공부하면서 정리한 내용"
---

# Transformer

본문을 Markdown으로 작성합니다.
```

GitHub Pages가 Jekyll collection을 사용해 개별 글 페이지와 `/notes/` 목록을 생성합니다.

## Development

별도 build framework 없이 HTML, CSS, JavaScript와 GitHub Pages 기본 Jekyll 기능을 사용합니다.

로컬에서 변경한 뒤:

```bash
git pull origin main
git add .
git commit -m "update site"
git push origin main
```

배포는 GitHub Pages에서 처리합니다.

## Assets

프로필과 프로젝트 이미지는 base64로 HTML에 포함하지 않고 `images/` 아래의 실제 파일로 관리합니다.

예:

```text
images/
├── profile.jpg
└── projects/
    ├── pick-and-place.jpg
    ├── towing-robot.jpg
    └── digital-twin.jpg
```
