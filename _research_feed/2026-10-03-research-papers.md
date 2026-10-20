---
layout: feed_note
title: "VLA의 미래 예측을 실제 action 계획에 묶는 ForeAct3D"
date: 2026-10-03 19:00:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "ForeAct3D는 VLA가 낼 action chunk에 조건화된 미래 3D 장면을 학습 신호로 사용한다. LIBERO·CALVIN과 Franka 실험에서 기준 정책보다 높은 결과를 보고했지만, 미래 예측은 학습 때만 쓰인다."
---

로봇이 물체를 밀거나 삽입할 때 중요한 것은 다음 영상이 그럴듯한지가 아니라, **정책이 실제로 실행하려는 행동 뒤에 물체와 접촉 상태가 어떻게 바뀔지**다. 10월 3일 공개된 **ForeAct3D**는 미래 장면 예측을 VLA의 action chunk와 직접 연결한다.

모델은 정책 표현으로부터 현재·미래의 깊이, semantic segmentation, 카메라 pose를 포함한 3D scene state를 복원한다. 미래 상태를 예측할 때는 policy가 제안한 action chunk를 조건으로 사용한다. 배경은 정지하고 같은 물체는 강체로 움직인다는 consistency 조건을 두며, wrist camera pose는 end-effector kinematics와 맞춘다. 이 구조로 미래 예측이 실행할 행동과 분리되지 않도록 학습한다.

저자들은 robot pretraining 없이 LIBERO 평균 성공률 **98.3%**, CALVIN 평균 task length **3.73**을 보고했고, 세 real-robot 과제에서는 base policy의 평균 성공률 **6.7%에서 37.8%**로 개선됐다고 밝혔다. 논문은 semantic 3D supervision, 물리 일관성, action conditioning의 ablation도 제시한다. 특히 action conditioning이 미래 물체 위치 예측을 개선했다는 결과는 행동과 예측 표현을 함께 학습하는 설계를 뒷받침한다.

배포 시에는 미래 장면 예측을 실행하지 않는다. 예측 목표가 학습 중 shared representation을 형성하는 supervision으로 쓰인다는 점에서, 이 접근은 world model을 매 제어 주기마다 호출하는 설계와 다르다. 따라서 실시간 추론 비용을 줄일 가능성은 있지만, 실행 중 미래 상태를 검증하거나 잘못된 예측을 이용해 action을 차단하는 verifier는 아니다.

실기 수치도 세 과제에 대한 결과다. 실제 robot 기반 개선은 의미 있는 증거지만 다양한 물체·센서·그리퍼나 긴 작업에 대한 일반화까지 입증하지 않는다. 후속 평가에서는 action-conditioned 예측이 접촉·삽입 실패를 실제로 줄이는지, 그리고 그 이득이 카메라 pose나 물체 물성 변화에서도 유지되는지를 확인해야 한다.

## Sources
- [ForeAct3D 논문 원문과 실험 결과](https://arxiv.org/abs/2610.04607)
- [ForeAct3D 논문 HTML](https://arxiv.org/html/2610.04607v2)
