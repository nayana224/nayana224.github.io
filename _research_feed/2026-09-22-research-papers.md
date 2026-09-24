---
layout: feed_note
title: "STRIDER, humanoid loco-manipulation에서 걷기와 정밀 stepping을 한 policy로 묶는다"
date: 2026-09-22 11:30:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "STRIDER는 자연스러운 walking과 foothold-level stepping을 별도 expert로 학습한 뒤 latent alignment를 포함한 LD-PPO로 하나의 student policy에 통합해 humanoid loco-manipulation의 이동과 조작을 함께 다룬다."
---

Humanoid loco-manipulation에서는 **자연스럽게 걷는 것**과 **정확한 위치에 발을 디디는 것**이 같은 문제가 아니다. 새로 업데이트된 **STRIDER**는 이 둘을 각각의 expert로 두고, 최종적으로 하나의 실행 가능한 policy로 distill한다.

구조는 계층적이다. terrain-aware stepping logic이 stance-foot frame에서 feasible foothold를 고르고 clearance-aware swing trajectory를 만들며, AMP 기반 walking expert는 자연스러운 보행을 담당한다. 상체는 Cartesian control로 end-effector tracking을 수행한다.

흥미로운 부분은 expert들을 합치는 방식이다. **LD-PPO (Latent Distillation PPO)**는 단순히 teacher의 action만 따라 하게 하지 않고, teacher-conditioned latent alignment를 추가한다. on-policy RL과 DAgger action reconstruction에 latent representation 정렬을 함께 걸어 walking과 stepping이라는 서로 다른 skill을 하나의 student policy 안에 공유 표현으로 넣는다.

TianGong Omni 실제 하드웨어에서도 foothold와 end-effector를 함께 추적하는 multi-gait loco-manipulation을 시연했다. Robot Learning 관점에서는 여러 primitive를 high-level에서 선택하는 것뿐 아니라, **서로 다른 low-level skill의 내부 representation까지 어떻게 한 policy에 통합할 것인가**라는 문제를 보여주는 사례다.

## Sources
- [arXiv — STRIDER: Stepping-Enabled Multi-Gait Hierarchical 3D Loco-Manipulation Framework for Humanoid Robots](https://arxiv.org/abs/2609.23483)
