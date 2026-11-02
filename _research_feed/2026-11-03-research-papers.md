---
layout: feed_note
title: "281개 로봇 정책을 실물로 시험하니, validation loss보다 좌표계와 action 표현이 중요했다"
date: 2026-11-03 06:59:10 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "10월 29일 공개된 실물 로봇 비교 연구는 RJ45 커넥터 파지·삽입에 281개 모방학습 정책과 약 1,700회 시험을 사용했다. ROI crop·로봇 기준 좌표계·절대 action 같은 표현 선택의 효과가 컸고, 67개 offline 지표 중 일부만 단일 정책 계열의 삽입 성공과 상관했다."
---

로봇 정책의 validation loss가 낮아졌는데도 실제 로봇은 커넥터를 꽂지 못할 수 있다. 10월 29일 공개된 *From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation*은 이 불일치를 실물 실험으로 조사했다. **7개 정책 계열, 281개 정책, 약 1,700회 실제 로봇 시험**을 비교한 결과, 모델의 세부 optimizer보다 **관측·행동 표현**이 성패를 크게 바꿨다.

실험 장비는 **Franka Research 3 팔과 Tesollo DG5F-M 다섯 손가락 손**이다. 작업은 RJ45 케이블 커넥터를 잡아 기존 소켓에서 빼고 다른 소켓에 삽입하는 것이다. 연구진은 고정된 위치 사이의 이동은 기존 motion planning으로 처리하고, 접촉이 중요한 **grasp와 insert만 별도 학습 정책**으로 구성했다. Teleoperation 시연은 30 Hz로 수집하고 정책은 10 Hz로 실행했다.

## 모델 크기보다 입력과 출력의 정의가 먼저였다

Diffusion Policy, DP3, iDP3, Flow Matching, ACT, π₀.₅ 등을 비교하면서 가능한 경우 한 설정만 바꾼 paired ablation을 수행했다. 특히 point cloud를 입력받는 정책에서는 **관심 영역(ROI) 자르기, robot-base frame 사용, PointNet 내부 정규화**가 결정적이었다.

논문에 제시된 대표적인 실물 비교는 다음과 같다.

- iDP3의 ROI crop 추가: 커넥터 **pick 성공률 0%→100%**.
- PointNet 내부 각 층의 normalization 적용: DP3 **insert 성공률 0%→70%**.
- 두 카메라를 쓰는 π₀.₅에서 6D rotation 표현과 함께 상대 action을 절대 action으로 변경: **insert 성공률 30%→100%**.

이 값은 논문에 기록된 **특정 설정 쌍의 시험 결과**다. 모든 정책과 물체에서 70–100%p가 재현된다는 뜻이 아니다. 일부 비교는 한 번에 여러 조건이 바뀌어 원인을 하나로 분리할 수 없으며, 개별 성공률의 신뢰구간도 넓다.

## 접촉 작업을 나누면 무엇이 달라지는가

커넥터를 집는 단계와 정밀하게 꽂는 단계는 필요한 관측과 데이터 분포가 다르다. 파지는 초기 위치 변화에 강해야 하지만, 삽입은 좁은 목표 영역과 접촉 오차를 정밀하게 다뤄야 한다.

연구진의 **grasp→이동→insert 분리 파이프라인** 중 최상위 iDP3와 π₀.₅ 구성은 두 지그 조건에서 실험한 삽입 시도에 모두 성공했다. 반면 단일 end-to-end grasp-and-insert 정책은 **최대 10%** 삽입 성공에 그쳤다. 다만 연구진도 **skill 분리만의 인과 효과는 다른 변경과 독립적으로 분리되지 않았다**고 명시한다.

추론 메모리 측면에서는 iDP3 구성 약 **1 GB**, 비교 π₀.₅ 구성 약 **8 GB**로, 이 작업에서 작은 point-cloud 정책이 큰 VLA와 비슷한 최상위 성공률을 얻었다. 이 역시 범용 모델 성능 비교가 아니라 **특정 정밀 삽입 작업의 시스템 설계 trade-off**다.

## Offline 지표 67개 중 실제 성공을 예측한 것은?

정책마다 실제 로봇을 반복 시험하기 어렵기 때문에, 연구진은 validation episode에 정책을 실행하지 않고 action만 예측시키는 **offline proxy**를 조사했다. Validation loss, 예측 경로 오차, end-effector 속도·jerk·경로 길이, encoder 안정성 등 **67개 지표**를 비교했다.

그중 통계적 다중 검정 보정과 leave-one-policy-out 검사까지 통과한 지표는 **5개**였다. 그러나 이 결과는 **두 지그에서 시험한 iDP3 삽입 정책 21개 checkpoint 내부**에만 해당했다. 평균 속도·경로 길이·경로 길이 비율·jerk·spectral power가 삽입 성공과 **Pearson r = -0.70~-0.80**으로 상관했다. 지표끼리도 높은 상관을 보여 사실상 비슷한 '짧고 부드러운 경로' 특성을 측정했다.

**서로 다른 정책 계열을 함께 비교하거나 grasp 성공률을 예측할 수 있는 공통 offline 지표는 발견되지 않았다.** 같은 iDP3 checkpoint 집합에서 최저 validation loss와 삽입 성공률의 상관은 **r=+0.08(p=0.72)**이었다. 따라서 offline 점수는 같은 정책 계열 안에서 후보를 줄이는 보조 수단일 뿐, 실물 평가를 대체하지 못한다.

## Robotics R&D에서 바로 바꿔 볼 검증 순서

모방학습 정책이 실패하면 우선 learning rate를 조정하기보다 **카메라 시야와 ROI, 좌표계 정의, 절대/상대 action, 회전 표현, 학습 시연과 실행 주기의 일치**부터 확인할 가치가 있다. 특히 ROS 2의 TF frame과 로봇 드라이버가 받아들이는 pose command의 의미가 다르면 학습 성능과 무관한 실행 오차가 생길 수 있다. 이는 논문의 실험에서 직접 검증한 ROS 2 결과가 아니라, 연구 결과를 시스템 통합에 적용한 **공학적 해석**이다.

그다음 grasp와 insert를 별도로 채점하고, checkpoint별 예측 경로의 smoothness를 기록한 뒤, 동일한 초기 물체 위치·조명·소켓 공차에서 실제 로봇 시험을 해야 한다. 이 논문은 **한 종류의 케이블·손·팔·정밀 삽입 작업**을 깊게 평가했으므로, 변형체 일반 조작이나 다른 embodiment에서의 보편적 우열로 확대할 수 없다.

## 부록: 배경지식

### Offline proxy(오프라인 대리지표)

**정의:** 로봇을 실제로 움직이지 않고 기록된 데이터에서 정책의 품질을 간접 추정하는 지표다. **예시(설명용):** validation 영상에 대한 예측 action이 얼마나 매끄러운지 측정해 실물 시험 후보를 고른다. **이 글에서의 의미:** 67개 후보 중 일부가 같은 iDP3 계열의 삽입 성공과 상관했지만, 서로 다른 정책을 공정하게 순위 매기지는 못했다.

### ROI cropping(관심 영역 자르기)

**정의:** 카메라 영상이나 point cloud에서 작업에 필요한 부분만 남기는 전처리다. **예시(설명용):** 넓은 작업대 대신 커넥터와 로봇손 주변 점군을 모델에 입력한다. **이 글에서의 의미:** iDP3의 파지 성공률이 크게 바뀐 원인 중 하나로 분리 시험된 입력 표현 선택이다.

### Absolute action과 relative action

**정의:** absolute action은 기준 좌표계에서의 목표 pose를, relative action은 현재 pose에 더할 변화량을 나타낸다. **예시(설명용):** '로봇 기준 x=0.40 m로 이동'은 절대 명령, '현재 위치에서 x로 0.02 m 이동'은 상대 명령이다. **이 글에서의 의미:** π₀.₅의 특정 삽입 설정에서 절대 action과 6D rotation 조합이 상대 action보다 높은 성공률을 보였다. 예시의 좌표값은 논문 측정치가 아니다.

### Pearson correlation(피어슨 상관계수)

**정의:** 두 수치가 함께 증가하거나 감소하는 선형 관계를 -1에서 +1 사이로 나타낸다. **예시(설명용):** 경로의 jerk가 작은 checkpoint일수록 성공률이 높다면 음의 상관이 나올 수 있다. **이 글에서의 의미:** r=-0.70~-0.80은 제한된 iDP3 삽입 checkpoint 집합에서 나타난 상관이지, 경로를 매끄럽게 만들면 반드시 성공률이 오른다는 인과관계는 아니다.

## Sources

- [From Teleoperation to Long-Horizon Dexterity — arXiv:2610.40828 (2026-10-29)](https://arxiv.org/abs/2610.40828)
- [논문 전체 HTML — 실물 ablation, Table 1, offline 지표 검증과 Appendix](https://arxiv.org/html/2610.40828v1)
