---
layout: feed_note
title: "FLUX 3 Action이 7B open-weight World Action Model로 공개됐다"
date: 2026-09-23 08:04:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "FLUX 3 Action의 open-weight World Action Model 공개, Isaac ROS 5.0의 agent-ready robotics workflow, 그리고 GR00T N1.7의 edge-NPU 최적화를 함께 본다."
---

## 1/ FLUX 3 Action은 video foundation model을 7B robot policy로 가져왔다

Black Forest Labs가 **FLUX 3 Action을 7B open-weight World Action Model로 공개했다.** 입력은 최근 camera observation, robot state, natural-language instruction이고, 다음 **32개 action과 미래 visual state를 함께 예측**한 뒤 새 observation을 받아 다시 실행하는 closed-loop 구조다.

핵심은 image/video generation에서 학습한 visual representation을 robot action prediction까지 이어간다는 점이다. FLUX 3의 multimodal pretraining과 Self-Flow 계열의 representation을 기반으로 future frame과 action을 함께 학습한다. BFL이 제공한 RoboLab-120 결과에서는 **42.92% overall success rate**를 보고했으며, 16B Cosmos3-Nano-Policy보다 작은 7B model이다. 다만 이 수치는 BFL이 제공한 release benchmark이고 공개 leaderboard와 외부 재현 결과가 아직 충분히 축적되지 않았으므로, 서로 다른 robotics benchmark의 수치와 직접 비교하면 안 된다.

실제 adaptation 쪽도 흥미롭다. 공개된 demonstration은 약 **200개 teleoperation episode**로 related pick-and-place task에 fine-tuning했고, 한 demo에서는 첫 시도 실패 뒤 다시 접근해 성공하는 recovery behavior도 보였다. 이것만으로 일반적인 self-recovery 능력이 입증된 것은 아니지만, world-model pretraining이 failure 이후의 다음 action까지 어떤 식으로 연결되는지 볼 만한 신호다.

BFL은 weights·code·fine-tuning recipe·benchmark·SO-101/LeRobot 예제를 공개하는 방향을 제시하고 있다. 생성 모델 회사가 `video를 잘 예측하는 representation → physical action`으로 확장한다는 점에서 VLA만이 아니라 **World Action Model이라는 또 다른 robot foundation model 설계 축**을 실제로 비교해볼 수 있게 됐다.

## 2/ Isaac ROS 5.0은 AI agent를 ROS 개발 workflow 안으로 넣는다

NVIDIA가 **Isaac ROS 5.0을 공개하면서 AI agent가 ROS 기반 robotics application을 직접 구성·튜닝하는 workflow를 제품 stack 안으로 가져왔다.** 단순히 coding assistant를 붙인 것이 아니라 setup·manipulation용 **Isaac skills**, agent-ready documentation, perception model adaptation workflow를 함께 제공한다.

구체적으로 FoundationStereo fine-tuning skill은 agent가 camera·environment·application에 맞춰 stereo perception model을 조정하는 과정을 돕고, **FoundationPose의 agent-ready inference library는 object pose estimation·tracking을 최대 5.5× 빠르게** 처리한다고 NVIDIA는 설명한다. Detection → depth → pose를 잇는 pick-and-place workflow도 standalone agent-ready skill로 제공된다.

흥미로운 부분은 agent layer 아래의 ROS data path도 같이 바뀐다는 점이다. Isaac ROS 5.0은 **ROS Lyrical과 Ubuntu 24.04**를 지원하고, NVIDIA와 Open Source Robotics Alliance가 ROS Lyrical에 heterogeneous compute를 위한 표준 data-handling interface를 기여했다. CUDA가 그 GPU acceleration 구현의 한 예다. 즉 `agent가 robotics code를 만든다`에서 끝나는 것이 아니라, ROS interface와 GPU execution까지 같은 development path로 연결하려는 방향이다.

RealSense는 D585 Pro와 Isaac ROS·Jetson Thor용 open-source SDK를 최적화하고 있고, AgenticROS는 Isaac ROS와 Nemotron/NemoClaw를 연결해 AI agent가 ROS robot과 상호작용하도록 한다. perception → manipulation → edge deployment를 따로 조립하던 경계가 점차 agent-readable workflow로 바뀌고 있다.

## 3/ GR00T N1.7을 GPU 없이 edge NPU에서 1.6초 → 약 230ms로 줄였다

Nota AI가 **GR00T N1.7을 Qualcomm Dragonwing IQ-9075 NPU 위에서 직접 구동해 VLA 한 사이클을 1,602.4ms에서 약 230ms까지 줄인 구현 과정**을 공개했다. 외부 GPU server에 inference를 맡기는 대신 vision·language·action pipeline을 robot-side edge processor에 내려놓은 사례다.

단순 quantization 하나로 얻은 결과는 아니다. 팀은 MolmoAct2를 포함한 **5개 VLA backbone을 같은 board에서 비교**하고, runtime과 computation graph를 직접 최적화한 뒤 최종적으로 GR00T N1.7을 선택했다. 정확도 손실을 1%p 이내로 제한하면서 최대 7.0× inference acceleration을 얻었고, KRAIN 2026의 SO-101 robot-arm demo에서는 약 **90% task success rate**를 유지했다고 보고했다.

더 흥미로운 부분은 마지막 병목이 model inference가 아니라 **camera thread**였다는 점이다. inference만 빨라져도 perception → action loop가 자동으로 빨라지는 것은 아니었고, camera pipeline과 robot control까지 함께 손봐야 실제 동작 latency가 줄었다. 이는 edge VLA에서 model compression만큼 runtime·sensor I/O·control loop를 하나의 system으로 측정해야 한다는 구체적인 사례다.

VLM/VLA를 제한된 GPU·NPU 환경에 올릴 때 중요한 기준도 여기서 보인다. `모델이 메모리에 들어가는가`만 볼 것이 아니라 **end-to-end observation → inference → action latency와 실제 task success를 함께 측정**해야 한다.

### Sources

- [Black Forest Labs — FLUX 3 Action](https://bfl.ai/models/flux-3-action)
- [VentureBeat — Black Forest Labs debuts FLUX 3 Action](https://venturebeat.com/infrastructure/black-forest-labs-debuts-flux-3-action-an-open-weights-ai-robotics-model-that-tops-the-leaderboard-at-half-the-size-of-its-competition)
- [NVIDIA Blog — Isaac ROS 5.0 Advances Agentic, Open Source Robotics Development](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/)
- [NVIDIA Isaac ROS](https://nvidia-isaac-ros.github.io/)
- [Nota AI — GPU 없이 VLA 돌리기: 퀄컴 NPU에서 1.6초를 230ms로](https://blog.nota.ai/kr/insights/vla-edge-npu-optimization)
- [Qualcomm — Dragonwing IQ-9075](https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075)
