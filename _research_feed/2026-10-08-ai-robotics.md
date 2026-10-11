---
layout: feed_note
title: "CAD에서 SimReady 로봇 자산까지, 물리 검증을 포함한 자동화"
date: 2026-10-08 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "NVIDIA가 CAD를 Isaac Sim용 OpenUSD 자산으로 만드는 5단계 agent-assisted workflow를 공개했다."
---

## CAD를 USD로 변환하는 것만으로는 시뮬레이션이 되지 않는다

NVIDIA는 10월 8일 ABB YuMi 로봇의 STEP 기반 CAD 자산을 **SimReady OpenUSD**로 준비하는 5단계 워크플로를 소개했다. Geometry import뿐 아니라 시각적 외형, joint axis·limit, collision shape, 질량·마찰 등 물리 속성을 설정하고 검증한 뒤 Isaac Sim에서 pick-and-place까지 확인한다.

Frontier AI 모델은 Omniverse 도구를 호출하는 Python 코드 작성을 보조한다. 하지만 핵심은 AI가 CAD를 ‘자동 변환’했다는 주장보다 **시뮬레이터에 필요한 물리 제약을 명시하고 검증 단계를 둔다**는 점이다. 원 로봇의 datasheet와 URDF를 대조해 joint와 mass property를 설정하는 절차는 로봇 프로젝트의 sim-to-real 준비에도 직접 연결된다.

여기서 소개된 것은 자산 생성 절차의 시연이지, 모든 CAD에서 자동으로 정확한 동역학을 복원한다는 보장은 아니다.

## Sources
- [NVIDIA — 5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models)
