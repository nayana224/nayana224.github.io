---
layout: feed_note
title: "VLA는 이제 model보다 training·serving·deployment stack이 더 중요해지고 있습니다"
date: 2026-09-19 00:35:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "최근 VLA 연구에서 반복해서 보이는 data quality, latency-aware serving, real-world deployment 문제를 세 논문으로 정리했습니다."
---

최근 VLA 논문들을 같이 보면 한 가지 흐름이 보입니다.

**Model architecture만 좋아서는 실제 robot이 잘 움직이지 않습니다.**

같은 model이라도 어떤 data로 학습하고, 얼마나 빠르게 serve하고, controller까지 어떻게 연결하는지가 성능을 갈라놓고 있습니다.

## 1/ Offline metric이 좋아도 robot은 실패할 수 있습니다

REAL-I Challenge 분석에서는 fixed demonstration budget 안에서도 data curation, staged adaptation, checkpoint selection, action-space design에 따라 실제 성공률이 크게 달라졌습니다.

특히 **offline action-prediction metric과 closed-loop robot success가 항상 같이 움직이지 않았습니다.**

Loss만 보고 deployment 성능을 판단하기 어렵다는 뜻입니다.

## 2/ VLA도 실제 현장에 들어가면 serving system이 됩니다

Robion은 여러 robot과 여러 VLA model을 하나의 GPU server에서 동시에 serve하는 문제를 다룹니다.

여기서는 accuracy뿐 아니라 **inference latency, GPU scheduling, model placement, multi-robot load**가 바로 시스템 성능이 됩니다.

VLA가 factory나 lab에 들어가는 순간 ML model 하나가 아니라 real-time robotics infrastructure가 되는 셈입니다.

## 3/ Real-world VLA는 결국 full stack 문제입니다

Hy-Embodied-0.5-VLA는 data collection부터 pre-training, SFT, RL post-training, real-world deployment까지 전체 pipeline을 하나의 stack으로 봅니다.

Camera, action representation, policy, control interface, deployment environment가 모두 연결돼야 실제 robot이 움직입니다.

그래서 앞으로 VLA 논문을 볼 때는 **Training / Serving / Deployment** 세 축을 같이 보는 편이 훨씬 유용합니다.

## Sources

- [How to Better Train VLAs: Lessons Learned From the REAL-I Challenge at ICRA 2026](https://arxiv.org/abs/2609.13679)
- [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)
- [Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](https://arxiv.org/abs/2606.14409)
