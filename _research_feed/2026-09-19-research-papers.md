---
layout: feed_note
title: "Research Papers Update — VLA Scaling, Lifelong Learning, Real-Robot Deployment"
date: 2026-09-19
channel: research-papers
channel_label: Research Papers
summary: "VLA 연구에서 지금 눈여겨볼 세 가지 축: 대규모 data scaling, lifelong adaptation, 실제 robot deployment의 system-level 문제."
---

**한 줄 요약:** 최근 VLA 연구를 보면 **scale, continual adaptation, real-world deployment** 세 축이 점점 더 중요해지고 있다.

## 1. Xiaomi-Robotics-1 — 100K+ hours real-world trajectories로 VLA scaling

Xiaomi Robotics는 **100,000시간이 넘는 real-world manipulation trajectory**를 활용한 VLA model을 공개했다.

이 연구의 핵심은 단순히 dataset이 크다는 점보다, scale이 실제 robot performance로 이어지는지를 확인했다는 데 있다.

주요 특징:

- 대규모 real-world trajectory pre-training
- natural language auto-labeling pipeline
- pre-training → post-training 2-stage recipe
- unseen environment에서 zero/few-shot adaptation
- downstream dexterous task에 data-efficient fine-tuning

### Why it matters

LLM/VLM에서 확인된 scaling law가 robotics에서도 어느 정도 성립하는지 보는 대표적인 흐름이다.

특히 robot learning에서는 data collection 비용이 매우 크기 때문에,  
**어떤 data를 얼마나 모아야 generalization이 생기는가**가 핵심 연구 문제가 된다.

## 2. LifelongVLA — 새로운 task를 배우면서 이전 skill을 잊지 않기

LifelongVLA는 VLA의 continual/lifelong learning 문제를 다룬다.

robot이 deployment 이후 계속 새로운 task를 배워야 한다면 두 가지가 동시에 필요하다.

- **plasticity**: 새로운 task를 잘 배워야 함
- **stability**: 기존 task를 잊지 않아야 함

이 논문은 이를 위해:

- short-term / long-term adaptation을 나누는 dual-timescale LoRA
- task-aware gating
- memory-efficient replay

를 사용한다.

### Why it matters

실제 robot은 한 번 학습하고 끝나는 system이 아니다.

공장, 실험실, 가정처럼 환경과 task가 계속 바뀌는 곳에서는  
**continual adaptation이 없는 VLA는 deployment 단계에서 한계가 생길 수밖에 없다.**

## 3. VLA on a real UR5 platform — model보다 pipeline이 문제일 수 있다

UR5e 실제 robot에서 OpenVLA 계열을 fine-tuning하고 deployment한 연구는 매우 실용적인 포인트를 보여준다.

offline metric이 좋아도 실제 closed-loop robot에서는 불안정할 수 있으며, 그 원인이 단순한 model capacity가 아닐 수 있다는 것이다.

논문이 강조하는 system-level 요소:

- action representation
- coordinate frame convention
- temporal alignment
- image preprocessing consistency
- dataset coverage
- control interface

### Why it matters

이건 실제 robotics를 해본 사람에게 특히 중요한 메시지다.

VLA를 실제 robot에 올릴 때는:

**model → action → coordinate → controller → physical robot**

전체 pipeline이 정확히 맞아야 한다.

즉 VLA deployment는 단순 ML problem이 아니라 **robot system integration problem**이기도 하다.

## 정리

세 논문은 서로 다른 문제를 다루지만 연결하면 다음과 같다.

1. **Scale** — 더 많은 real-world data로 generalization 확대
2. **Adaptation** — deployment 이후 새로운 skill을 계속 학습
3. **Integration** — 실제 robot에서 data-model-control pipeline을 안정화

현재 VLA 연구를 공부할 때는 architecture만 보지 말고 이 세 축을 같이 보면 전체 흐름을 잡기 좋다.

## Sources

- Xiaomi-Robotics-1  
  https://arxiv.org/abs/2607.15330

- LifelongVLA  
  https://arxiv.org/abs/2607.14852

- Vision-Language-Action Models: Experimental Insights from a Real-World UR5 Platform  
  https://arxiv.org/abs/2606.30456
