---
layout: feed_note
title: "ACCRUE는 새 과제를 배우면서 이전 조작 기술을 보존하려 한다"
date: 2026-10-13 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "ACCRUE는 로봇 foundation model의 순차적 off-policy RL에 actor·critic 재사용과 소량의 이전 에피소드 증류를 결합한다."
---

새 로봇 조작 과제를 계속 학습하면 이전 기술을 잊거나, 매 과제마다 처음부터 데이터를 모아야 하는 문제가 생긴다. 10월 13일 공개된 **ACCRUE**는 이 문제를 robot foundation model의 순차적 reinforcement learning으로 다룬다.

핵심은 과제 사이에 가벼운 actor와 critic을 이어 쓰는 것이다. critic은 현재 과제의 전이 데이터에 맞추고, actor는 그 critic을 이용해 새 과제를 학습한다. 이전 행동은 보관해 둔 소수 에피소드에서 이전 actor의 출력을 따라가도록 증류해 보존한다.

저자들은 접촉이 많은 조립 과제의 시뮬레이션과 실제 로봇 실험에서, 후속 과제 학습 시간을 **31–68.5% 줄이고 이전 과제의 성능을 거의 유지했다**고 보고한다. 이는 논문에서 평가한 과제 순서와 시스템에 관한 결과다. 일반적인 배포 비용이나 모든 과제에서의 망각 방지를 보장하지는 않는다.

실제 시스템에 적용할 때는 신규 과제의 학습 속도만 보지 말고, 이전 과제 성능·로봇 상호작용 시간·저장한 재생 데이터의 양을 함께 추적해야 한다.

## Sources
- [ACCRUE 논문](https://arxiv.org/abs/2610.18596)
- [ACCRUE 논문 HTML](https://arxiv.org/html/2610.18596v1)
