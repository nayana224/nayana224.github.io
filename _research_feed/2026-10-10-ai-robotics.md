---
layout: feed_note
title: "주말 기술 점검: Robot agent는 관측과 제어를 분리해 설계한다"
date: 2026-10-10 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "NVIDIA의 조립 사례에서 고수준 task와 실시간 perception·control primitive의 역할 구분을 살펴본다."
---

*기존 자료 재조명*

**주말 기술 점검 · 원자료는 10월 7일 발표됐다.** NVIDIA는 GB300 tester tray 조립에서 FoundationPose, waypoint planning, Lissajous-curve manipulation primitive, impedance controller를 결합한 busbar 조립 시스템을 소개했다.

여기서 주목할 점은 foundation model 하나가 전체 로봇 행동을 만들어내지 않았다는 것이다. **물체 pose 추정, 경로 설계, 접촉 제어, 성공 판정**이 분리되어 있다. Auto Lab과 같은 agent architecture에서도 느린 planning과 빠른 control loop 사이의 인터페이스를 명확히 해야 한다.

이는 당일 신규 발표가 아니라 기존 조립 사례의 설계 관점 재검토다.

## Sources
- [NVIDIA 로봇 조립 원문](https://developer.nvidia.com/blog/the-machines-that-make-the-machines/)
