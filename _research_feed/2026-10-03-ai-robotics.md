---
layout: feed_note
title: "주말 기술 점검: ROS 2 GPU 가속은 커널보다 데이터 흐름"
date: 2026-10-03 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "GPU kernel 속도만 높여서는 ROS 2 시스템의 end-to-end latency가 줄지 않는다."
---

*기존 자료 재조명*

**주말 기술 점검 · 재조명한 자료는 9월 22일 공개됐다.** NVIDIA는 ROS 2 node의 GPU 가속 사례에서 계산 커널뿐 아니라 메시지 전달·복사·동기화 등 전체 graph 경로를 살펴야 한다고 설명했다.

로봇에서는 카메라 입력→전처리→인식→추론→행동 출력까지 함께 측정해야 한다. GPU 단계만 빨라도 serialization이나 CPU-GPU copy가 병목이면 체감 반응속도는 개선되지 않을 수 있다.

이는 10월 3일 신규 발표가 아니라, 자동화 공백을 보충하며 선택한 기존 기술자료의 후속 해설이다.

## Sources
- [NVIDIA ROS 2 기술 글](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros)
