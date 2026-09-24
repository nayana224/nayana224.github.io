---
layout: feed_note
title: "ROS 2가 GPU 메모리를 표준 메시지 안으로 가져왔다"
date: 2026-09-24 19:49:36 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "ROS 2 Lyrical의 rosidl::Buffer와 NVIDIA CUDA backend는 표준 ROS 메시지를 유지하면서 조건이 맞을 때 GPU-resident payload를 host copy와 serialization 없이 노드 사이에 전달한다."
---

**ROS 2 Lyrical의 `rosidl::Buffer`와 NVIDIA의 CUDA buffer backend가 GPU-resident data를 표준 ROS message 안에서 직접 전달할 수 있게 됐다.** 같은 host·CUDA device·Linux user와 지원되는 RMW 조건을 만족하면 co-located node 사이의 payload가 **host copy와 serialization 없이** 이동하고, 조건이 맞지 않으면 기존 CPU path로 자동 fallback한다.

핵심은 별도의 NVIDIA 전용 message type을 만드는 방식이 아니라는 점이다. 예를 들어 기존 `.msg`의 `uint8[] data` 정의는 그대로 두면서 generated C++ representation을 `rosidl::Buffer<uint8_t>`로 사용한다. 기본 backend는 기존 `std::vector`처럼 CPU storage를 쓰고, 필요할 때 CUDA Virtual Memory Management 기반 backend를 끼울 수 있다. 즉 **ROS interface와 node boundary를 유지한 채 memory domain만 바꿀 수 있는 구조**다.

이 변화에 맞춰 **Isaac ROS 5.0의 모든 node가 CUDA buffer backend를 사용하도록 업데이트됐고, 기존 NITROS 계열 transport API는 deprecated되어 향후 제거될 예정이다.** NVIDIA가 ROSCon 2026에서 소개한 Accelerated Memory Transports도 이 upstream 구조를 중심으로 tensors·point clouds처럼 큰 payload의 hardware-accelerated transport를 다룬다.

실제 robotics pipeline에서는 model inference 시간만 줄여도 sensor → preprocessing → inference → downstream node 경계에서 CPU↔GPU copy와 serialization이 반복되면 end-to-end latency가 남는다. 이번 변화는 perception-to-action pipeline 최적화에서 **`모델이 몇 ms인가`뿐 아니라 `데이터가 node 사이를 어떤 memory path로 이동하는가`도 직접 봐야 한다**는 점을 ROS 2 자체의 abstraction으로 끌어올렸다는 데 의미가 있다.

다만 zero-copy path는 항상 보장되는 것이 아니다. 현재 CUDA backend의 optimized path는 동일 host/device/user와 지원 RMW 등 runtime 조건을 요구하므로, 실제 시스템에서는 profiler로 transport path와 fallback 여부를 확인해야 한다.

### Sources
- [NVIDIA Technical Blog — Accelerating a ROS 2 Node with an AI Agent and NVIDIA Isaac ROS](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros)
- [Isaac ROS — rosidl::Buffer and Buffer Backends](https://nvidia-isaac-ros.github.io/concepts/rosidl_buffer/index.html)
- [Isaac ROS 5.0 — From NITROS to rosidl::Buffer](https://nvidia-isaac-ros.github.io/v/release-5.0/concepts/rosidl_buffer/nitros_migration.html)
- [NVIDIA at ROSCon 2026 — Accelerated Memory Transports](https://www.nvidia.com/en-us/events/roscon/)
