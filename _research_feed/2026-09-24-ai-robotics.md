---
layout: feed_note
title: "Claude Opus 5.5는 agent 성능보다 cost-per-task를 더 크게 움직였다"
date: 2026-09-24 21:13:01 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude Opus 5.5는 Opus 5보다 token price를 낮추고 task당 비용을 약 40% 줄이면서 agentic coding과 computer-use 성능을 끌어올렸다. ROS 2 Lyrical의 GPU-resident transport 변화와 함께 실제 agent/robotics system에서 모델 성능 밖의 실행 비용과 data path가 중요해지는 흐름을 보여준다."
---

**Claude Opus 5.5는 Opus 5보다 input/output token 가격을 각각 $5→$4, $25→$20 per 1M tokens로 낮추면서, Anthropic 기준 실제 task당 비용은 약 40% 줄였다.** 동시에 Terminal-Bench 4.0은 **66.4%**, OSWorld 2.0은 **81.8%**, AutomationBench는 **40.0%**를 기록했다.

단순히 benchmark 점수가 오른 release라기보다 agent가 긴 작업을 수행할 때 필요한 **token·tool call·step 수를 줄이는 방향**이 더 눈에 띈다. Anthropic은 Opus 5.5가 Opus 5보다 기본 출력 속도가 30% 이상 빠르고, 별도 fast mode에서는 최대 2.5× 속도를 제공한다고 설명한다. 다만 benchmark 수치는 Anthropic 및 각 평가 주체의 특정 harness·effort 설정에서 측정된 결과이므로 서로 다른 agent runtime의 실제 latency나 비용으로 그대로 일반화하면 안 된다.

Coding agent나 high-level robot agent처럼 모델을 한 번 호출하고 끝나는 것이 아니라 observation → reasoning → tool/action → verification을 반복하는 시스템에서는 **single-call intelligence보다 `성공한 task 하나를 끝내는 데 드는 총 inference cost와 step 수`가 더 직접적인 system metric**이 된다. 모델 선택에서도 benchmark accuracy와 함께 cost-per-task, wall-clock time, tool-call count를 같이 측정할 이유가 커졌다.

---

**같은 날 robotics stack 쪽에서는 ROS 2 Lyrical의 `rosidl::Buffer`와 NVIDIA CUDA buffer backend가 GPU-resident data를 표준 ROS message 안에서 직접 전달하는 경로를 열었다.** 같은 host·CUDA device·Linux user와 지원 RMW 조건을 만족하면 co-located node 사이 payload를 host copy·serialization 없이 넘기고, 조건이 맞지 않으면 기존 CPU path로 fallback한다.

Isaac ROS 5.0도 이 upstream mechanism으로 이동하면서 기존 NITROS transport API를 deprecated하고 있다. perception-to-action pipeline에서는 model inference 시간뿐 아니라 **sensor → preprocessing → model → control 사이에서 data가 어떤 memory path로 이동하는지**까지 end-to-end latency에 포함해 봐야 한다는 변화다.

### Sources
- [Anthropic — Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
- [NVIDIA Technical Blog — Accelerating a ROS 2 Node with an AI Agent and NVIDIA Isaac ROS](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros)
- [Isaac ROS — rosidl::Buffer and Buffer Backends](https://nvidia-isaac-ros.github.io/concepts/rosidl_buffer/index.html)
- [Isaac ROS 5.0 — From NITROS to rosidl::Buffer](https://nvidia-isaac-ros.github.io/v/release-5.0/concepts/rosidl_buffer/nitros_migration.html)
