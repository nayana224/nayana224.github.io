---
layout: feed_note
title: "GPT-6가 agent 성능보다 cost curve를 다시 밀었다"
date: 2026-09-23 17:35:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "GPT-6 Sol/Luna의 agent·coding·computer-use cost efficiency, FLUX 3 Action의 open-weight World Action Model, 그리고 Microsoft Research의 physical-AI inference offloading을 함께 본다."
---

## GPT-6 Sol·Luna는 frontier intelligence의 가격을 절반으로 낮췄다

OpenAI가 **GPT-6 Sol과 GPT-6 Luna를 공개하면서 API 가격을 GPT-5.6의 promotional pricing 대비 50% 낮췄다.** Sol은 input/output이 각각 **$2/$10 per 1M tokens**, Luna는 **$0.10/$0.50**다. 단순히 작은 모델을 싸게 내놓은 것이 아니라 agent workflow, coding, computer use에서 이전 세대보다 높은 성능을 더 낮은 task cost로 가져가는 데 초점이 맞춰져 있다.

OpenAI가 공개한 AutomationBench 1.0.6에서는 GPT-6 Sol xhigh가 **33.2%를 $0.27/task**에 기록했다. 같은 표에서 Claude Opus 5 max는 26.9%였고 task cost는 Sol의 11.1배였다. DeepSWE 1.1에서는 Sol max가 **68.8%**, Luna max가 **66.6%**를 기록했고, OSWorld 2.0 offline에서는 Sol xhigh가 **60.5%**였다. 다만 이 비교는 OpenAI가 선택한 model effort와 API price를 기준으로 한 vendor evaluation이므로, 독립 benchmark에서 동일한 cost/performance ordering이 재현되는지는 별도로 봐야 한다.

agent 관점에서 더 중요한 변화는 inference와 caching 최적화가 긴 workflow의 경제성으로 직접 연결된다는 점이다. coding agent나 research agent가 수십~수백 번 model call을 반복하면 single-call benchmark보다 **성공한 workflow 하나당 비용과 latency**가 실제 배포 한계를 결정한다. frontier model 경쟁이 최고 점수뿐 아니라 `어느 정도의 intelligence를 얼마에 반복 호출할 수 있는가`로 이동하고 있다는 신호다.

## FLUX 3 Action은 video foundation model을 7B robot policy로 가져왔다

Black Forest Labs가 **FLUX 3 Action을 7B open-weight World Action Model로 공개했다.** 입력은 최근 camera observation, robot state, natural-language instruction이고, 다음 **32개 action과 미래 visual state를 함께 예측**한 뒤 새 observation을 받아 다시 실행하는 closed-loop 구조다.

핵심은 image/video generation에서 학습한 visual representation을 robot action prediction까지 이어간다는 점이다. FLUX 3의 multimodal pretraining과 Self-Flow 계열의 representation을 기반으로 future frame과 action을 함께 학습한다. BFL이 제공한 RoboLab-120 결과에서는 **42.92% overall success rate**를 보고했으며, 16B Cosmos3-Nano-Policy보다 작은 7B model이다. 다만 이 수치는 BFL이 제공한 release benchmark이고 공개 leaderboard와 외부 재현 결과가 아직 충분히 축적되지 않았으므로, 서로 다른 robotics benchmark의 수치와 직접 비교하면 안 된다.

실제 adaptation 쪽도 흥미롭다. 공개된 demonstration은 약 **200개 teleoperation episode**로 related pick-and-place task에 fine-tuning했고, 한 demo에서는 첫 시도 실패 뒤 다시 접근해 성공하는 recovery behavior도 보였다. 이것만으로 일반적인 self-recovery 능력이 입증된 것은 아니지만, world-model pretraining이 failure 이후의 다음 action까지 어떤 식으로 연결되는지 볼 만한 신호다.

BFL은 weights·code·fine-tuning recipe·benchmark·SO-101/LeRobot 예제를 공개하는 방향을 제시하고 있다. 생성 모델 회사가 `video를 잘 예측하는 representation → physical action`으로 확장한다는 점에서 VLA만이 아니라 **World Action Model이라는 또 다른 robot foundation model 설계 축**을 실제로 비교해볼 수 있게 됐다.

## Robot의 GPU를 빼고 inference를 edge/cloud로 보내면 오히려 성공률이 올라갈 수 있다

Microsoft Research가 **physical AI inference를 robot onboard GPU에 고정해야 한다는 전제를 정면으로 검토한 systematic study와 offloading toolchain을 공개했다.** mobile manipulation의 mapping·planning·navigation·manipulation workload를 onboard, edge, cloud GPU에서 비교하고, inference 위치 자체를 robot system의 설계 변수로 다룬다.

작은 onboard GPU에서는 mapping/planning이 A100 대비 **최대 383% 느려졌고**, navigation의 timely obstacle detection은 **30% 감소**했다. VLA는 작은 GPU에서도 slowdown 자체는 상대적으로 작았지만, 그 latency 차이만으로 저자들의 평가에서 **accuracy가 50%까지 떨어졌다.** 즉 model checkpoint가 같아도 observation이 들어오고 action이 나오는 시간이 길어지면 physical task 성능이 달라질 수 있다는 것이다.

전력도 같은 문제다. 연구팀은 onboard GPU 대신 Raspberry Pi 5로 sensor data를 보내 remote GPU에서 inference했을 때 Stretch-3의 battery lifetime이 **100% 이상 증가할 수 있음**을 측정했다. 반대로 network latency·bandwidth·connectivity가 불안정하면 offloading이 항상 유리한 것은 아니다. 결론은 `cloud가 edge보다 낫다`가 아니라 **compute placement를 latency·power·model size·control loop와 함께 최적화해야 한다**는 쪽에 가깝다.

Microsoft는 이를 Physical AI Toolchain의 기능으로 구현해 robotics workload를 containerize하고 Kubernetes로 robot·edge·cloud에 배치하도록 했다. ROS 2와 LeRobot integration을 제공하며 SO-101, UR10e 예제도 포함한다. VLA deployment에서도 model FLOPs나 single-call latency가 아니라 **observation → inference → action 전체 loop와 실제 task success를 기준으로 compute architecture를 결정해야 한다**는 시스템 관점이 중요해지고 있다.

## Sources
- [OpenAI — Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [Black Forest Labs — FLUX 3 Action](https://bfl.ai/models/flux-3-action)
- [VentureBeat — Black Forest Labs debuts FLUX 3 Action](https://venturebeat.com/infrastructure/black-forest-labs-debuts-flux-3-action-an-open-weights-ai-robotics-model-that-tops-the-leaderboard-at-half-the-size-of-its-competition)
- [Microsoft Research — Offloaded inference for real-world physical AI robotics](https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/)
- [Microsoft — Physical AI Toolchain](https://github.com/microsoft/physical-ai-toolchain)
