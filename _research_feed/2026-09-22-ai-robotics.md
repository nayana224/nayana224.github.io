---
layout: feed_note
title: "Google Home은 MCP를 열고, JetBrains Air는 coding agent를 하나의 system으로 묶는다"
date: 2026-09-22 22:10:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "MCP가 physical-device context로 확장되는 가운데 JetBrains는 Air를 IDE·agent·organization governance를 잇는 open agentic development system으로 확대했고, TensorRT 11.0은 대형 모델 serving을 multi-GPU로 확장했다."
---

## 1/ Google Home이 MCP를 연다

Google이 **Google Home에 Model Context Protocol(MCP) integration을 추가해 third-party AI agent가 smart-home infrastructure와 상호작용할 수 있게 했다.** Claude, OpenClaw, Hermes 같은 외부 agent가 household context를 읽고 device troubleshooting, custom dashboard 생성, camera 기반 분석 같은 작업을 수행할 수 있는 방향이다.

여기서 흥미로운 지점은 MCP의 적용 범위다. 지금까지 MCP가 coding agent와 SaaS/tool 연결에서 빠르게 확산됐다면, 이번 사례는 **agent → protocol → sensor/device environment**라는 physical-world interface에 더 가깝다. 다만 door unlocking처럼 위험도가 높은 action에는 제한이 있고, rate limit 등 safety boundary도 함께 둔다.

Robotics 관점에서도 볼 만하다. 이것이 곧 robot control protocol이라는 뜻은 아니지만, high-level agent가 표준화된 tool interface를 통해 heterogeneous physical devices와 context를 다루는 구조는 향후 embodied agent orchestration을 생각할 때 참고할 수 있다.

## 2/ JetBrains Air가 app에서 agentic development system으로 커진다

JetBrains가 **Air를 standalone agentic development app 하나가 아니라 IDE부터 team·organization governance까지 잇는 open system으로 확대**했다. 기존 Air의 parallel agent workspace에 더해 JetBrains의 현재 AI stack은 IDE-native AI, Air, organization-level agent/model governance, repository intelligence, 그리고 여러 terminal agent를 연결하는 CLI layer까지 하나의 방향으로 정리되고 있다.

핵심은 특정 coding model을 하나 고르는 문제가 아니라 **agent harness와 execution surface를 교체 가능하게 두면서 context·review·governance를 공통 infrastructure로 만드는 것**이다. Air는 ACP-compatible agent를 연결할 수 있고 Codex·Claude Agent·Gemini CLI·Junie 같은 서로 다른 agent를 같은 workflow에서 다루는 방향을 택했다.

Coding agent 경쟁이 model 성능만의 문제가 아니라 `agent ↔ context ↔ isolated execution ↔ human review ↔ organization policy`를 어떻게 묶느냐의 경쟁으로 이동하고 있다는 사례다.

## 3/ TensorRT 11.0은 하나의 inference network를 여러 GPU로 확장한다

NVIDIA가 **TensorRT 11.0에서 하나의 TensorRT network를 여러 GPU에 걸쳐 실행하는 multi-device inference를 정식 지원**하기 시작했다. Dynamo-Triton 26.07에서는 하나의 `KIND_MODEL` instance가 여러 GPU를 소유하면서도 외부에는 **single gRPC endpoint**로 노출된다.

TensorRT graph 안에서 NCCL-backed distributed collective를 처리하기 때문에 model serving 쪽에서 별도의 distributed inference plumbing을 직접 조립해야 하는 부담을 줄인다. NVIDIA는 Cosmos 3 Nano video generation의 **44,160 video tokens를 최대 8개 GPU에 Ulysses context parallelism으로 분산**하는 예제를 공개했다.

큰 VLM·world model처럼 단일 GPU memory나 latency가 병목이 되는 workload에서는 `model optimization`과 `distributed serving`의 경계가 조금 더 얇아지는 변화다. Robotics에서도 대형 perception/world-model component를 server-side로 운용할 때 살펴볼 만하다.

### Sources

- [Google Home Developers — Google Home APIs](https://developers.home.google.com/)
- [The Verge — Google will now let any AI agent run your smart home](https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date)
- [JetBrains — AI Agents for Developers](https://www.jetbrains.com/pages/ai-agents/)
- [JetBrains Blog — Air gets more agents, local models, and Java/Kotlin code intelligence](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)
- [NVIDIA Technical Blog — Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton](https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/)
