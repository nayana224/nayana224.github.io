---
layout: feed_note
title: "Research Papers Update — VLA Training, Serving, Real-World Stack"
date: 2026-09-19 00:35:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "최근 VLA 연구에서 눈여겨볼 세 축: fixed-data training, latency-aware serving, end-to-end real-world robot learning stack."
---

**한 줄 핵심:** 최근 VLA 논문들을 묶어 보면 architecture 하나보다 **data를 어떻게 쓰는지, 실제 robot에서 어떻게 serve하는지, 전체 learning stack을 어떻게 구성하는지**가 점점 중요해지고 있다.

## 1. REAL-I Challenge — 같은 demonstration budget에서도 학습 방식이 중요하다

How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026은 fixed demonstration budget에서 robot policy를 어떻게 더 잘 학습시킬 수 있는지를 실제 challenge 결과로 분석한다.

참가팀들은 pretrained VLA와 imitation policy를 사용했지만, 성능 차이는 단순 model 선택뿐 아니라 다음 요소에서도 크게 나타났다.

- data curation
- staged adaptation
- checkpoint selection
- action-space design
- deployment environment adaptation

특히 offline action-prediction metric이 실제 closed-loop 성공률을 충분히 예측하지 못한다는 점도 강조한다.

### Why it matters

VLA 실험을 할 때 “loss가 낮다”와 “robot이 task를 성공한다”는 같은 말이 아니다.  
실제 deployment에서는 **data quality와 closed-loop evaluation**이 훨씬 중요할 수 있다.

## 2. Robion — VLA도 serving system이 필요하다

Efficient Vision-Language-Action Management and Serving for Robot Factories는 여러 robot과 여러 VLA model을 GPU server에서 동시에 serve하는 문제를 다룬다.

VLA inference는 latency constraint가 강하고, VLM stage와 action generation stage의 계산 특성도 다르다. 이 논문은 GPU resource scheduling과 model placement를 조정해서 여러 robot request를 SLO 안에서 처리하는 system을 제안한다.

### Why it matters

VLA를 실제 현장에 배포하려면 model accuracy만으로 끝나지 않는다.

**latency, GPU scheduling, multi-robot load, reliability**까지 포함한 serving problem이 robotics에서도 중요해지고 있다는 의미다.

## 3. Hy-Embodied-0.5-VLA — model이 아니라 전체 robot learning stack을 본다

Hy-Embodied-0.5-VLA는 data collection부터 model design, continued pre-training, supervised fine-tuning, RL post-training, real-world deployment까지 **full robot learning stack**을 하나의 system으로 다룬다.

### Why it matters

VLA를 실제 robot에 적용하는 관점에서는 단일 architecture보다 전체 pipeline을 보는 것이 더 현실적이다.

특히 지금처럼 robotics system integration 경험에서 learning-based robotics로 넘어갈 때는 이 관점이 중요하다.

## Sources

- [How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026](https://arxiv.org/abs/2609.13679)

- [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)

- [Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](https://arxiv.org/abs/2606.14409)
