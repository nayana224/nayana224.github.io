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

## SimReady 검증에서 놓치기 쉬운 단위

USD 파일이 열리고 mesh가 보이는 것은 joint origin, 축 방향, limit 단위, inertial frame과 질량이 맞다는 증거가 아니다. collision geometry가 visual mesh와 다르면 접촉 결과도 달라질 수 있다. 따라서 각 articulation을 저속으로 구동하고 limit·충돌·질량 분포를 원 CAD·URDF와 대조하는 검사가 필요하다.

NVIDIA 사례는 AI가 작성한 변환 코드를 물리 자산의 검증 절차와 결합한 시연이다. 자동화 결과는 sim-to-real의 시작점이며, 실제 로봇의 calibration과 하중·마찰 검증을 대체하지 않는다.

## Sources
- [NVIDIA — 5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models)
