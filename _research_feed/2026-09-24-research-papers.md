---
layout: feed_note
title: "VLA를 54-DoF dexterous hand에 맞추는 post-training pipeline"
date: 2026-09-24 14:22:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "High-DoF dexterous manipulation에서 pretrained VLA의 action interface를 temporal hand-action codec으로 확장하고, SFT·buffered DAgger·latent residual RL을 연결한 실물 로봇 post-training pipeline이 제안됐다."
---

**새 연구는 pretrained π₀.₅를 54-dimensional bimanual arm-hand control에 연결하기 위해, raw finger joint를 직접 예측하는 대신 learned temporal hand-action codec을 사이에 둔다.** 그 위에 supervised fine-tuning, buffered DAgger, real-world residual RL을 순차적으로 적용했고, 저자들이 평가한 다섯 real-world dexterous task에서 최종 policy는 각 task 20회 기준 **100% success**를 보고했다.

문제는 pretrained VLA가 dexterous hand의 높은 DoF를 그대로 다루기 어렵다는 데 있다. 논문의 target robot은 두 arm의 14차원과 두 hand의 40차원을 합쳐 frame당 **54 joint-position command**가 필요하지만, 출발점인 π₀.₅의 action interface는 32차원이다. 저자들은 hand trajectory를 저차원 temporal latent로 압축하는 codec을 먼저 학습해, VLA가 개별 finger joint가 아니라 coordinated hand motion을 예측하도록 바꿨다.

그 다음 단계도 실물 manipulation에서 자주 생기는 failure mode를 직접 겨냥한다. DAgger takeover에서는 human operator와 policy의 pose mismatch 때문에 command discontinuity가 생길 수 있어 **buffered rollback, pose alignment, smooth command blending**을 사용한다. 마지막 residual RL 역시 raw joint space 전체를 탐색하지 않고 codec latent 안에서 correction을 학습해 exploration을 제한한다.

이 논문의 핵심은 새로운 foundation model 자체보다 **generalist VLA를 특정 high-DoF embodiment에서 신뢰할 수 있는 policy로 만드는 adaptation stack**에 있다. `pretrained prior → compact action representation → targeted human correction → residual RL`이라는 단계 분리는 dexterous manipulation뿐 아니라 embodiment-specific post-training을 설계할 때 비교해볼 만하다.

다만 결과를 일반적인 dexterous VLA 성능으로 해석하면 안 된다. 평가는 하나의 bimanual platform, 다섯 short-horizon task, checkpoint당 20 trials에 한정되며 초기 조건도 수동 reset했다. 저자들도 residual RL은 reference policy가 최소한의 competence를 확보한 뒤 더 안정적으로 이득을 보였다고 보고한다.

### Sources

- [arXiv — Towards High-DoF Dexterous Manipulation through VLA Post-Training](https://arxiv.org/abs/2609.19666)
