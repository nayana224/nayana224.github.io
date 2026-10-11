---
layout: feed_note
title: "Agent harness는 왜 작을수록 강해질 수 있나"
date: 2026-10-09 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "NVIDIA의 KDD Cup 사례는 agent에게 많은 도구를 주기보다 제한된 schema·tool과 상태 관리를 강조한다."
---

*전일 자료 후속 분석*

**후속 분석 · 원자료는 10월 8일 발표됐다.** NVIDIA KGMON 팀은 KDD Cup 2026 Data Agents 대회에서 2위를 기록했다고 보고했다. 단일 SQLite 데이터베이스, schema 탐색, 제한된 SQL 도구, 중간 결과의 지속 상태를 사용해 모델이 문제 해결에 집중하도록 설계했다.

로봇 agent에도 연결되는 핵심은 **모델 성능과 실행 harness의 품질을 따로 평가해야 한다**는 점이다. Planner의 tool 수를 무작정 늘리는 대신 검증 가능한 primitive와 typed interface를 제공하는 편이 진단·복구에 유리할 수 있다. 데이터 분석 대회의 결과가 직접 로봇 제어 실험을 입증하는 것은 아니다.

## Sources
- [NVIDIA KDD Cup 사례](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup)
