---
layout: feed_note
title: "Physical AI의 inference 위치가 robot system 설계 변수가 됐다"
date: 2026-09-23 17:10:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "FLUX 3 Action의 open-weight World Action Model, Microsoft Research의 physical-AI inference offloading, 그리고 GR00T N1.7 edge-NPU 최적화를 통해 robot intelligence의 모델과 실행 위치를 함께 본다."
---

## 1/ FLUX 3 Action은 video foundation model을 7B robot policy로 가져왔다

Black Forest Labs가 **FLUX 3 Action을 7B open-weight World Action Model로 공개했다.** 입력은 최근 camera observation, robot state, natural-language instruction이고, 다음 **32개 action과 미래 visual state를 함께 예측**한 뒤 새 observation을 받아 다시 실행하는 closed-loop 구조다.

핵심은 image/video generation에서 학습한 visual representation을 robot action prediction까지 이어간다는 점이다. FLUX 3의 multimodal pretraining과 Self-Flow 계열의 representation을 기반으로 future frame과 action을 함께 학습한다. BFL이 제공한 RoboLab-120 결과에서는 **42.92% overall success rate**를 보고했으며, 16B Cosmos3-Nano-Policy보다 작은 7B model이다. 다만 이 수치는 BFL이 제공한 release benchmark이고 공개 leaderboard와 외부 재현 결과가 아직 충분히 축적되지 않았으므로, 서로 다른 robotics benchmark의 수치와 직접 비교하면 안 된다.

실제 adaptation 쪽도 흥미롭다. 공개된 demonstration은 약 **200개 teleoperation episode**로 related pick-and-place task에 fine-tuning했고, 한 demo에서는 첫 시도 실패 뒤 다시 접근해 성공하는 recovery behavior도 보였다. 이것만으로 일반적인 self-recovery 능력이 입증된 것은 아니지만, world-model pretraining이 failure 이후의 다음 action까지 어떤 식으로 연결되는지 볼 만한 신호다.

BFL은 weights·code·fine-tuning recipe·benchmark·SO-101/LeRobot 예제를 공개하는 방향을 제시하고 있다. 생성 모델 회사가 `video를 잘 예측하는 representation → physical action`으로 확장한다는 점에서 VLA만이 아니라 **World Action Model이라는 또 다른 robot foundation model 설계 축**을 실제로 비교해볼 수 있게 됐다.

## 2/ Robot의 GPU를 빼고 inference를 edge/cloud로 보내면 오히려 성공률이 올라갈 수 있다

Microsoft Research가 **physical AI inference를 robot onboard GPU에 고정해야 한다는 전제를 정면으로 검토한 systematic study와 offloading toolchain을 공개했다.** mobile manipulation의 mapping·planning·navigation·manipulation workload를 onboard, edge, cloud GPU에서 비교하고, inference 위치 자체를 robot system의 설계 변수로 다룬다.

결과는 단순한 cloud-scale 이야기가 아니다. 작은 onboard GPU에서는 mapping/planning이 A100 대비 **최대 383% 느려졌고**, navigation의 timely obstacle detection은 **30% 감소**했다. VLA는 작은 GPU에서도 slowdown 자체는 상대적으로 작았지만, 그 latency 차이만으로 저자들의 평가에서 **accuracy가 50%까지 떨어졌다.** 즉 model checkpoint가 같아도 observation이 들어오고 action이 나오는 시간이 길어지면 physical task 성능이 달라질 수 있다는 것이다.

전력도 같은 문제다. 연구팀은 onboard GPU 대신 Raspberry Pi 5로 sensor data를 보내 remote GPU에서 inference했을 때 Stretch-3의 battery lifetime이 **100% 이상 증가할 수 있음**을 측정했다. 반대로 Jetson Thor 같은 큰 onboard compute는 해당 구성에서 battery drain을 크게 늘렸다. 물론 network latency·bandwidth·connectivity가 불안정하면 offloading이 항상 유리한 것은 아니므로, 이는 `cloud가 edge보다 낫다`는 결론이 아니라 **compute placement를 latency·power·model size와 함께 최적화해야 한다**는 결과에 가깝다.

Microsoft는 이를 Physical AI Toolchain의 기능으로 구현해 robotics workload를 containerize하고 Kubernetes로 robot·edge·cloud에 배치하도록 했다. ROS 2와 LeRobot integration을 제공하며 SO-101, UR10e 예제와 Rho model을 Jetson Thor로 offload해 Mobile ALOHA를 제어하는 사례도 공개했다.

Edge VLA 최적화와 함께 보면 흥미로운 대조가 생긴다. 앞으로의 질문은 단순히 `VLA를 robot 안에서 돌릴 수 있는가?`가 아니라 **어떤 part를 어느 compute에서, 어느 주기로 실행해야 closed-loop task success가 가장 높은가**에 더 가까워질 수 있다.

## 3/ GR00T N1.7을 GPU 없이 edge NPU에서 1.6초 → 약 230ms로 줄였다

Nota AI가 **GR00T N1.7을 Qualcomm Dragonwing IQ-9075 NPU 위에서 직접 구동해 VLA 한 사이클을 1,602.4ms에서 약 230ms까지 줄인 구현 과정**을 공개했다. 외부 GPU server에 inference를 맡기는 대신 vision·language·action pipeline을 robot-side edge processor에 내려놓은 사례다.

단순 quantization 하나로 얻은 결과는 아니다. 팀은 MolmoAct2를 포함한 **5개 VLA backbone을 같은 board에서 비교**하고, runtime과 computation graph를 직접 최적화한 뒤 최종적으로 GR00T N1.7을 선택했다. 정확도 손실을 1%p 이내로 제한하면서 최대 7.0× inference acceleration을 얻었고, KRAIN 2026의 SO-101 robot-arm demo에서는 약 **90% task success rate**를 유지했다고 보고했다.

더 흥미로운 부분은 마지막 병목이 model inference가 아니라 **camera thread**였다는 점이다. inference만 빨라져도 perception → action loop가 자동으로 빨라지는 것은 아니었고, camera pipeline과 robot control까지 함께 손봐야 실제 동작 latency가 줄었다. 이는 edge VLA에서 model compression만큼 runtime·sensor I/O·control loop를 하나의 system으로 측정해야 한다는 구체적인 사례다.

Microsoft의 offloading 결과와 방향은 반대지만 결론은 맞닿는다. **model FLOPs나 single-call latency가 아니라 observation → inference → action 전체 loop와 실제 task success를 기준으로 compute architecture를 결정해야 한다.**

### Sources

- [Black Forest Labs — FLUX 3 Action](https://bfl.ai/models/flux-3-action)
- [VentureBeat — Black Forest Labs debuts FLUX 3 Action](https://venturebeat.com/infrastructure/black-forest-labs-debuts-flux-3-action-an-open-weights-ai-robotics-model-that-tops-the-leaderboard-at-half-the-size-of-its-competition)
- [Microsoft Research — Offloaded inference for real-world physical AI robotics](https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/)
- [Microsoft — Physical AI Toolchain](https://github.com/microsoft/physical-ai-toolchain)
- [Nota AI — GPU 없이 VLA 돌리기: 퀄컴 NPU에서 1.6초를 230ms로](https://blog.nota.ai/kr/insights/vla-edge-npu-optimization)
- [Qualcomm — Dragonwing IQ-9075](https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075)
