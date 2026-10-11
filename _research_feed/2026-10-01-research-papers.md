---
layout: feed_note
title: "VLA 성공률만으로는 로봇 행동의 안정성을 설명할 수 없다"
date: 2026-10-01 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "LIBERO 기반 VLA 평가에서 같은 성공률이라도 perturbation 이후 움직임과 gripper 동작이 달라질 수 있다는 연구가 나왔다."
---

## Task Success Rate 뒤에 숨은 행동 차이

10월 1일 공개된 *Is Success All You Need?*는 VLA 평가에서 **성공했는가**뿐 아니라 **어떻게 성공했는가**를 측정해야 한다고 제안한다.

연구진은 LIBERO와 LIBERO-Plus 평가를 확장해 VLA 모델 3개, LIBERO task suite 4개, perturbation 조건 7개를 비교했다. Task Success Rate(TSR)가 비슷하게 유지되어도 성공한 trajectory의 **motion smoothness, efficiency, gripper behavior와 변동성**이 달라지는 사례를 관찰했다.

Closed-loop manipulation이나 정량 파지 연구에서 이 구분은 특히 중요하다. 목표 수량을 맞춘 성공 여부와 별개로, 재파지 횟수·불필요한 움직임·힘 조절·실패 후 복구 행동을 평가할 필요가 있기 때문이다. 다만 실험 결과는 논문에서 사용한 VLA·LIBERO 설정에 해당하며 실제 얽힌 식품의 파지 성능까지 입증하지는 않는다.

## Sources
- [Higham et al. — Is Success All You Need? (arXiv:2610.01351)](https://arxiv.org/abs/2610.01351)
