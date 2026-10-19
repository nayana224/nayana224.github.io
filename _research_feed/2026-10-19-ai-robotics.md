---
layout: feed_note
title: "ORA: VLA 학습 없이 로봇을 제어하는 오픈소스 Agent"
date: 2026-10-19 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "Hao AI Lab의 ORA는 오픈웨이트 LLM에 관측, 파지, 이동 도구와 실행 감독기를 연결한다."
---

10월 15일 공개된 **ORA(Open Robot-Use Agents)**는 로봇 전용 VLA 학습 없이 오픈웨이트 LLM이 도구를 호출해 로봇 조작 작업을 수행하는 시스템이다. 연구진은 DeepSeek-V4.1-Flash 기반 실험에서 RoboTwin C2R 69.2%(173/250), LIBERO-Pro 81.4%(651/800)의 공식 벤치마크 성공 판정을 보고했다.

## 어떻게 동작하나

일반적인 VLA가 관측에서 행동을 직접 예측하도록 학습하는 것과 달리, ORA는 **관측 → 추론 → 도구 호출 → 결과 확인**을 반복한다. 로봇 좌표계와 그리퍼 제약, 작업 조건을 prompt에 제공하고, 영상 분할·깊이 측정·파지 후보 생성·경로 계획 도구를 호출한다. 별도의 supervisor가 명령을 검사하고 실행 결과를 반환하므로, 실패 이유를 다음 계획에 반영할 수 있다.

## 실제 활용 범위와 제약

실험 대부분은 시뮬레이션이며, 에피소드 중간값은 14~25분이다. 시뮬레이터는 모델 추론 중 멈추므로 실시간 제어 성능을 입증하지 않는다. 실제 로봇 시연은 두 건이며 매 동작에 작업자 승인이 필요했다. 연구진은 공식 성공 판정과 실제 지시 이행이 다를 수 있다고도 명시했다. 따라서 발표된 수치를 현장 자율조작 성공률로 일반화할 수 없다.

## Sources
- [ORA 공식 기술 발표](https://haoailab.com/blogs/ora/)
- [ORA 공식 GitHub 코드 및 실행 방법](https://github.com/hao-ai-lab/ORA)
