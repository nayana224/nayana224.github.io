---
layout: feed_note
title: "AI & Robotics — Claude가 Anthropic R&D의 26%를 이끌고, frontier AI 평가는 회사 안으로 들어갑니다"
date: 2026-09-19 11:30:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Anthropic 내부 AI R&D 자동화와 embedded evaluation, Jetson Orin Nano 2, Spirit AI의 real-world embodied AI까지 주요 변화를 정리했습니다."
---

Claude가 이제 Anthropic AI R&D 작업의 **26%에서 lead 역할**을 맡고 있습니다. 2026년 2월에는 1% 미만이었는데, 8월 기준으로 4분의 1을 넘어섰습니다.

그리고 Anthropic은 frontier AI 평가 방식 자체도 바꾸려 하고 있습니다. Accenture와 함께 외부 evaluator를 회사 내부에 상주시켜 **직원에 준하는 접근권한으로 model을 평가하는 embedded evaluation**을 시작합니다.

Robotics 쪽에서는 edge compute와 real-world data가 동시에 전진하고 있습니다. Jetson Orin Nano 2는 이전 세대 대비 **2배 inference performance**를 제시했고, 중국 Spirit AI는 약 1,000명의 contractor가 수집한 real-world data로 humanoid의 physical intelligence를 학습하고 있습니다.

## 1/ Claude가 Anthropic R&D의 26%를 lead하고 있습니다

Anthropic이 공개한 내부 측정에서 Claude는 AI R&D의 **26%에서 lead 역할**을 맡고 있으며, 90%가 넘는 작업에서 적어도 collaborator로 참여하고 있습니다.

이 수치가 중요한 이유는 frontier model 개발에서 AI가 단순 coding assistant를 넘어 **다음 세대 AI를 만드는 research workflow 자체**로 들어가고 있기 때문입니다.

Anthropic은 그래서 AI가 차기 model 개발에 얼마나 관여하는지, 사람이 agent를 얼마나 감독·개입할 수 있는지, 더 강한 model을 만드는 데 어떤 resource가 쓰이는지를 정기적으로 측정해야 한다고 제안했습니다.

## 2/ Anthropic × Accenture — frontier model 평가자가 회사 안으로 들어갑니다

Anthropic과 Accenture는 향후 5년 동안 **각각 최소 10억 달러**를 투입해 embedded evaluation 역량을 구축하기로 했습니다.

기존 external evaluation과 가장 다른 점은 접근권한입니다. embedded evaluator는 Anthropic 내부에서 직원에 준하는 접근권한을 가지고 model evaluation, red-teaming, alignment assessment, safeguard testing을 수행하게 됩니다.

Frontier model이 더 강해질수록 출시 후 외부에서 시험하는 것만으로는 부족하다는 판단에 가깝습니다. **evaluation이 model development lifecycle 안으로 더 깊게 들어가는 변화**라는 점을 볼 필요가 있습니다.

## 3/ Jetson Orin Nano 2 — compact robot에서 inference가 2배 빨라졌습니다

NVIDIA Jetson Orin Nano 2는 **78 TOPS, 8GB memory, 8-core Arm CPU**를 제공하며 Jetson Orin Nano Super 대비 inference performance를 2배로 높였습니다.

같은 performance 기준 15W mode에서는 전력 소비도 40% 줄었다고 합니다. 동일한 compact form factor에서 더 큰 VLM과 generative AI workload를 edge에서 돌릴 여지가 커진 셈입니다.

Robot에서 cloud round-trip 없이 perception과 reasoning을 local inference로 처리하려면 compute budget이 직접적인 제약이 됩니다. 그래서 이 변화는 단순 spec upgrade보다 **on-device Physical AI의 실행 범위를 넓히는 변화**에 가깝습니다.

## 4/ Spirit AI — humanoid의 병목은 body보다 brain이라는 주장입니다

Spirit AI는 Reuters 인터뷰에서 structured environment의 simple task에서 약 **90% success rate**를 달성했다고 밝혔고, mid-2027을 embodied AI의 중요한 breakthrough 시점으로 보고 있습니다.

흥미로운 건 학습 방식입니다. simulator보다 약 1,000명의 contractor가 모으는 **real-world robot data**를 중심으로 학습하고 있으며, Moz1 humanoid 수십 대가 CATL과 JD.com 생산 현장에서 이미 사용되고 있다고 설명했습니다.

아직 household robot까지 바로 이어진다는 뜻은 아닙니다. structured industrial task와 open-ended home task 사이에는 큰 gap이 남아 있습니다.

하지만 VLA/Robot Learning 관점에서는 다시 같은 질문으로 돌아옵니다. **더 큰 model인가, 더 좋은 real-world data인가, 아니면 둘을 연결하는 control stack인가?**

## 지금 봐야 할 포인트

AI 연구에서는 **AI가 AI 개발 loop 안으로 얼마나 깊게 들어오는지**와 함께, 그 속도를 따라가기 위해 **evaluation 자체가 development loop 안으로 얼마나 깊게 들어오는지**를 같이 볼 필요가 있습니다.

Robotics에서는 **real-world data + edge inference + closed-loop control**이 얼마나 빠르게 묶이는지가 계속 핵심입니다.

## Sources

- [Anthropic — Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development)
- [Anthropic — Partnering with Accenture on embedded evaluation](https://www.anthropic.com/news/accenture-embedded-evaluation)
- [NVIDIA Jetson Orin Nano 2 — product details reported September 18](https://roboticsandautomationnews.com/2026/09/18/nvidia-unveils-jetson-orin-nano-2-for-robotics-and-edge-ai/104918/)
- [Reuters — Spirit AI sees robot-brain breakthrough as soon as 2027](https://www.reuters.com/world/asia-pacific/founder-chinese-startup-spirit-ai-says-robot-brains-set-2027-breakthrough-2026-09-18/)
