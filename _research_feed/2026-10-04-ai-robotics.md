---
layout: feed_note
title: "주말 기술 점검: VLA와 World Action Model의 역할은 다르다"
date: 2026-10-04 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "Robot Learning에서 VLA의 action prediction과 world model 기반 예측을 구분해야 한다."
---

*기존 자료 재조명*

**주말 기술 점검 · 원자료는 8월 4일 게시됐다.** NVIDIA는 robot manipulation에서 기존 시연 데이터에 대한 행동 모방을 넘어, 환경 변화에 대응하도록 미래 상태와 행동을 함께 고려하는 World Action Model 방향을 설명했다.

Closed-loop grasping에서는 첫 동작의 정확도만이 아니라 목표 상태 관찰, 오차 추정, 후속 행동 선택이 필요하다. 따라서 거대한 VLA를 한 번 호출하는 것과 feedback monitor를 별도 구성하는 접근을 구분해서 평가할 수 있다.

10월 4일에 새 모델이 공개됐다는 뜻은 아니며, 주말 재검토를 위한 기술 해설이다.

## Sources
- [NVIDIA 기술 해설](https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/)
