---
layout: feed_note
title: "TensorRT 11.0, 하나의 inference network를 여러 GPU로 확장한다"
date: 2026-09-22 10:00:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "TensorRT 11.0과 Dynamo-Triton 26.07이 single model instance의 multi-GPU inference를 정식 지원하면서, 큰 generative·multimodal workload의 serving 구조가 단순해졌다."
---

NVIDIA가 **TensorRT 11.0에서 하나의 TensorRT network를 여러 GPU에 걸쳐 실행하는 multi-device inference를 정식 지원**하기 시작했다. Dynamo-Triton 26.07에서는 하나의 `KIND_MODEL` instance가 여러 GPU를 소유하면서도 외부에는 **single gRPC endpoint**로 노출된다.

핵심은 단순히 GPU를 여러 장 쓰는 것이 아니다. TensorRT graph 안에서 NCCL-backed distributed collective를 처리하기 때문에, model serving 쪽에서 별도의 분산 inference plumbing을 직접 조립해야 하는 부담을 줄인다.

NVIDIA는 Cosmos 3 Nano video generation을 예제로 **44,160 video tokens를 최대 8개 GPU에 Ulysses context parallelism으로 분산**했다. Diffusers는 기존처럼 prompt·scheduler·postprocessing을 담당하고, TensorRT/Dynamo-Triton 쪽이 multi-GPU execution을 맡는다.

큰 VLM·world model·video model처럼 단일 GPU memory나 latency가 병목이 되는 workload에서는 `model optimization`과 `distributed serving`의 경계가 조금 더 얇아지는 변화다. Robotics 쪽에서도 대형 perception/world-model component를 server-side로 운용할 때 살펴볼 만한 infrastructure 변화다.

### Sources

- [NVIDIA Technical Blog — Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton](https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/)
