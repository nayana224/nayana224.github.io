---
layout: feed_note
title: "Coding agent가 로봇의 실패 해결책을 VLA 학습 데이터로 바꾸기 시작했다"
date: 2026-09-29 09:10:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "EmbodiedSWE와 AdaHVLA는 long-horizon robotics에서 느린 agent reasoning과 빠른 VLA execution을 분리하고, 실패·경험을 다음 정책 개선에 다시 쓰는 방향을 보여준다."
---

로봇의 long-horizon task를 **VLA 하나에 전부 맡기는 대신, agent가 문제를 풀고 그 경험을 다시 VLA의 학습·실행 구조로 환류시키는 접근**이 구체화되고 있다.

## EmbodiedSWE: coding agent를 robot policy의 supervisor로

**EmbodiedSWE**는 coding agent가 contact-rich manipulation, deformable object, long-horizon robotics task를 직접 해결하도록 하고, 검증된 해결 과정을 다시 대규모 trajectory로 확장해 VLA 학습에 사용한다.

핵심은 agent와 policy의 역할 분리다. Coding agent는 긴 시간 동안 tool을 사용하며 시행착오를 거쳐 해결책을 찾을 수 있지만, 그 방식 자체는 느리고 task instance에 특화되기 쉽다. 연구진은 이를 **EMBODIEDSWE-GEN**으로 다양화해 빠른 VLA가 학습할 supervision으로 변환했다.

논문은 coding-agent-generated simulation demonstration만으로 fine-tuning한 VLA가 실제 로봇의 long-horizon task까지 수행할 수 있음을 보고한다. 다만 전체 결과를 일반적인 real-world robotics 성능으로 확대 해석하기에는 아직 simulation 비중과 task 범위가 크다는 제한이 있다.

이 구조는 로봇 시스템을 `LLM/agent → 계획 → 실행`의 일회성 pipeline으로만 보는 것보다 흥미롭다. **agent가 실패를 분석하고 해결책을 찾는 느린 loop와, 학습된 policy가 빠르게 행동하는 loop를 분리한 뒤 둘 사이에 data flywheel을 만드는 방식**이기 때문이다.

## AdaHVLA: VLA 바깥의 stateful harness도 경험으로 고친다

**AdaHVLA**는 다른 층을 겨냥한다. VLA의 local control 능력은 유지하면서 persistent memory와 planning을 담당하는 code-based harness를 두고, 실제 execution evidence를 이용해 이 harness 자체를 반복적으로 수정한다.

연구진은 evidence analysis, harness revision, behavioral assessment를 분리하고, execution evidence와 hypothesis, revision, observed effect를 stateful graph로 연결한다. 보고된 simulation 결과에서는 NaVILA-LH 평균 test success가 22.5%에서 최대 57.5%로 증가했고, 세 VLA backbone의 manipulation success는 초기 harness 대비 최대 30.8 percentage points 개선됐다.

두 연구를 같이 보면 최근 long-horizon robotics에서 중요한 질문이 조금 달라지고 있다. **더 큰 VLA 하나를 만드는 것뿐 아니라, VLA가 실패했을 때 무엇이 기억하고 판단하고 수정하며 그 경험을 다음 실행에 어떻게 재사용할 것인가**가 별도의 시스템 설계 문제가 되고 있다.

## Sources

- [EmbodiedSWE — arXiv](https://arxiv.org/abs/2609.27308)
- [AdaHVLA — arXiv](https://arxiv.org/abs/2609.29204)
