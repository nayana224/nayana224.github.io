---
layout: feed_note
title: "GPU가 스토리지에 직접 접근한다: NVIDIA cuObject·SCADA"
date: 2026-09-30 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "NVIDIA가 GPU 주도형 object storage 접근용 cuObject 및 SCADA Server SDK를 공개했다."
---

*당일 발표*

NVIDIA는 9월 30일 cuObject client/server 라이브러리와 SCADA Server SDK를 소개했다. 핵심은 GPU와 스토리지 사이의 전송에서 불필요한 CPU 경유를 줄이고, 고성능 AI 시스템에서 데이터 접근을 가속하는 것이다.

모델의 연산 성능만큼 **입출력 경로와 데이터 이동 비용**이 중요하다는 사례다. 다만 이 기술은 데이터센터용 스토리지 인프라 이야기로, Jetson의 카메라→GPU 전송에 그대로 적용된다는 의미는 아니다.

## Sources
- [NVIDIA 원문](https://developer.nvidia.com/blog/expanding-ai-storage-access-with-nvidia-cuobject-and-the-nvidia-scada-server-sdk)
