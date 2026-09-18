---
layout: feed_note
title: "Research Papers — VLA는 이제 모델보다 학습·서빙·배포가 중요해지고 있습니다"
date: 2026-09-19 00:35:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "최근 VLA 논문을 묶어보면 data quality, latency-aware serving, real-world robot learning stack이 핵심 주제로 올라오고 있습니다."
---

VLA는 이제 **모델 구조만 잘 만든다고 끝나는 분야가 아닌 것 같습니다.**

최근 논문들을 보면 같은 방향을 반복해서 말합니다.

**어떤 data로 학습시키는지, 실제 robot에서 얼마나 안정적으로 serve하는지, 전체 deployment pipeline을 어떻게 구성하는지**가 성능만큼 중요해지고 있습니다.

## 1/ REAL-I Challenge — offline metric이 좋아도 robot은 실패할 수 있습니다

REAL-I Challenge 분석은 fixed demonstration budget 안에서 VLA를 어떻게 더 잘 학습시킬 수 있는지를 실제 competition 결과로 봅니다.

팀별 차이는 model architecture만으로 설명되지 않았습니다.

- data curation
- staged adaptation
- checkpoint selection
- action-space design
- deployment environment adaptation

같은 요소들이 실제 성공률에 크게 영향을 줬습니다.

특히 눈에 띄는 건 **offline action-prediction metric과 closed-loop robot success가 꼭 같이 가지 않는다는 점**입니다.

loss가 낮아졌다고 robot task가 잘 되는 건 아니라는 이야기입니다.

## 2/ Robion — VLA도 결국 serving system이 필요합니다

Robion은 여러 robot과 여러 VLA model을 GPU server에서 동시에 serve하는 문제를 다룹니다.

이 단계에 오면 model accuracy보다 다른 문제가 보입니다.

- inference latency
- GPU scheduling
- model placement
- multi-robot load
- service-level objective

즉 VLA가 실제 factory나 lab에 들어가면 ML model 하나가 아니라 **real-time serving system**이 됩니다.

Robotics에서 system integration 경험이 중요한 이유도 여기서 다시 드러납니다.

## 3/ Hy-Embodied-0.5-VLA — 결국 full stack 문제입니다

Hy-Embodied-0.5-VLA는 data collection부터 pre-training, supervised fine-tuning, RL post-training, real-world deployment까지 전체 pipeline을 하나의 stack으로 봅니다.

이 관점이 중요한 이유는 실제 robot에서는 model만 따로 존재하지 않기 때문입니다.

camera, action representation, control interface, dataset, policy, deployment 환경이 전부 맞물려야 합니다.

VLA deployment는 결국 **learning problem이면서 동시에 robotics system problem**입니다.

## 지금 봐야 할 포인트

최근 VLA 연구를 세 축으로 보면 정리가 쉽습니다.

1. **Training** — 같은 data에서도 어떻게 더 잘 학습할 것인가  
2. **Serving** — 실제 robot에 얼마나 빠르고 안정적으로 제공할 것인가  
3. **Deployment** — model부터 controller까지 전체 stack을 어떻게 맞출 것인가

앞으로 논문을 읽을 때 architecture만 따라가기보다 이 세 축을 같이 보면, 실제 robot에 연결되는 흐름이 더 잘 보일 것 같습니다.

## Sources

- [How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026](https://arxiv.org/abs/2609.13679)
- [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)
- [Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](https://arxiv.org/abs/2606.14409)
