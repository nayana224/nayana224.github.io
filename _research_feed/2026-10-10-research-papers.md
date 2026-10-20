---
layout: feed_note
title: "힘 센서는 접촉이 시작될 때만 VLA의 중심으로 들어온다"
date: 2026-10-10 19:00:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "DEFT-VLA는 비접촉 접근과 접촉 조작에 서로 다른 expert를 두고 힘 정보의 역할을 접촉 단계에 집중한다. 세 실기 과제에서 강한 baseline보다 20–40%p 높은 성공률을 보고했다."
---

접촉 조작에서 힘 정보는 항상 유용한 입력이 아니다. 물체에 접근하고 위치를 맞출 때는 vision과 proprioception이 핵심인 반면, 접촉 뒤에는 힘이 미끄러짐·끼임·압력을 알려준다. **DEFT-VLA**는 이 단계별 차이를 하나의 정책 입력에 억지로 섞지 않고 expert를 나눠 다룬다.

Dual-Expert Force-specialized Training은 비접촉 행동에 task-adapted base expert를 유지하고, 중요한 접촉 구간에는 force-aware contact expert를 둔다. 학습 과정은 접촉 expert에 force-attending post-training을 적용한 뒤 시각 정보를 점진적으로 복원하고 state token을 마스킹한다. 저자들의 의도는 힘 신호를 접촉이 필요한 순간에 학습시키면서, 장면의 우연한 시각 단서나 상관된 robot state가 지름길이 되는 것을 줄이는 것이다.

실제 로봇 평가는 pipette tip 부착, 양손 pipette aspiration, whiteboard wiping 세 과제에서 이뤄졌다. 논문은 각 과제의 가장 강한 baseline보다 전체 task success가 **20–40 percentage points** 개선됐으며, held-out grasp height에서도 robustness를 유지했다고 보고한다. 이는 force feedback이 전체 동작에서 동일한 가치를 갖는 것이 아니라, 단계에 따라 다른 정보를 제공한다는 주장을 뒷받침한다.

조작 시스템에서 이 결과를 재현하려면 힘 측정의 frame·방향·영점 보정과 vision/proprioception의 timestamp 정렬이 중요하다. 접촉 전후를 나누는 기준이 흔들리면 두 expert의 전환 자체가 실패 원인이 될 수 있다. 논문 초록은 세 과제의 개선 범위를 제시하지만, 다양한 센서와 embodiment에서의 전환 안정성이나 장시간 마모 조건까지 입증하지는 않는다.

따라서 DEFT-VLA는 “힘 센서를 추가하면 더 강건하다”는 일반 주장보다, **힘이 정보가 되는 구간을 학습 구조 안에서 국소화**한 연구로 읽는 편이 정확하다. 다음 비교에서는 전체 성공률뿐 아니라 접촉 단계별 실패, expert 전환 시점, force sensor 제거·노이즈 ablation을 함께 확인할 필요가 있다.

## Sources
- [DEFT-VLA 논문 원문과 실험 결과](https://arxiv.org/abs/2610.14854)
- [DEFT-VLA 논문 HTML](https://arxiv.org/html/2610.14854v1)
