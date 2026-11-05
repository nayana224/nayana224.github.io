---
layout: feed_note
title: "안전한 한 걸음이 작업 복귀를 보장하지 않는다: VLA의 CBF-QP에 우회 경로를 더하다"
date: 2026-11-06 07:00:10 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "11월 1일 공개된 Route-Guided CBF-QP Repair는 VLA 행동의 국소 충돌 회피가 작업 궤도 복귀를 보장하지 않는 문제를 다룬다. SafeLIBERO에서 AEGIS 대비 평균 SafeSuccess 47.19→49.69%를 보고했지만 실행 단계 수가 증가했고 실물 검증은 제시되지 않았다."
---

로봇이 장애물을 피해 한 번 안전하게 움직였더라도, 그 다음에 **원래 작업으로 돌아올 길**이 없으면 결국 실패한다. 2026년 11월 1일 공개된 *Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models*는 VLA 정책 뒤에 붙이는 안전 필터가 **국소적인 충돌 회피뿐 아니라 경로 복귀**까지 고려해야 한다고 제안한다.

## 기존 CBF-QP가 놓치는 것은 '그 다음 동작'이다

VLA는 현재 영상과 지시에서 짧은 action chunk를 예측한다. CBF(Control Barrier Function)-QP(Quadratic Programming)는 그중 현재 행동을 가능한 적게 수정하면서 안전 제약을 만족시키는 필터다. 그러나 장애물 앞에서 행동을 계속 옆으로 밀기만 하면 충돌은 피하더라도 정책이 기대한 궤적에서 멀어질 수 있다.

제안 방법은 action chunk의 Cartesian displacement를 누적해 **예상 이동 경로**를 만들고, 이를 타원체로 근사한 장애물 안전 영역과 비교한다. 경로가 막히면 좌우 우회 후보 각각에 **entry → exit → rejoin** waypoint를 생성한다. 후보는 장애물과의 거리, 원래 작업 진행도, 우회 길이, 원래 궤적 이탈량으로 평가한다.

## 경로는 부드러운 목표, 안전은 단단한 제약

핵심은 QP의 두 역할을 구분하는 것이다. 목적함수는 **원래 VLA 행동과의 차이** 및 **선택된 waypoint를 향한 행동과의 차이**를 함께 줄인다. 반면 CBF 안전 조건은 제약식으로 유지한다.

`u* = argmin_u [ ||u-u_VLA||²_W + β λ_r ||u_xyz-u_route||² ]`

`subject to: h_dot(x,u) + α h(x) >= 0`

여기서 `u_VLA`는 원래 행동, `u_route`는 현재 waypoint 방향의 병진 명령, `β`는 경로 유도가 필요한 때만 1이 되는 스위치다. 장애물이 없으면 기본 CBF-QP로 돌아간다. rejoin waypoint에 도달하면 우회 유도를 끄고 원래 VLA 실행으로 복귀한다.

**주의:** 수학적 CBF 조건이 존재한다는 사실만으로 실제 로봇의 모든 충돌을 막는다고 보증할 수는 없다. 모델링 오차, 장애물 감지 누락, 제어 지연, QP infeasibility에 대한 별도 검증이 필요하다.

## SafeLIBERO 평균은 개선됐지만 우회 비용도 늘었다

논문은 동일한 **π₀.₅ VLA backbone과 가중치**를 사용하는 AEGIS 대비 경로 유도의 효과를 비교했다. SafeLIBERO 네 suite(Spatial, Goal, Object, Long)에서 각 작업 10 episode를 평가했다.

| 지표 | AEGIS | Route-Guided |
| --- | ---: | ---: |
| Collision Avoidance Rate | 64.69% | 69.06% |
| Task Success Rate | 62.81% | 65.00% |
| SafeSuccess(충돌 없이 작업 성공) | 47.19% | 49.69% |
| Execution Time Steps(작을수록 좋음) | 109.87 | 118.45 |

가장 큰 차이는 **Object suite의 SafeSuccess 41.25→55.00%**였다. 그러나 Goal suite에서는 SafeSuccess가 **73.75→67.50%**로 하락했다. 따라서 모든 작업에서 일관되게 좋아졌다고 볼 수 없다. 전체 평균의 개선폭은 2.50 percentage points로 제한적이며, 우회·복귀를 위해 평균 실행 단계가 증가했다.

Ablation에서 rejoin 유도를 제거하면 평균 SafeSuccess가 **49.69→47.92%**, 경로 점수화를 제거하면 **49.69→48.15%**로 낮아졌다. 이는 복귀 waypoint와 후보 선택이 각각 기여한다는 근거다. 다만 **시뮬레이션 SafeLIBERO 결과**이며 실물 로봇의 센서 오차나 동적 장애물 환경으로 일반화됐다는 증거는 없다.

## 구현에서 무엇을 별도로 시험할까

ROS 2 조작 스택에 적용한다면 **VLA action chunk → 예측 경로 → 장애물 모델 → QP safety filter → 로봇 제어기**의 인터페이스를 분리해야 한다. 장애물 근처에서 좌우 후보가 반복적으로 바뀌는 oscillation, waypoint 전환 시 불연속, action 좌표계 불일치, 안전 제약의 infeasible 상태, 우회 중 지연 누적을 시험할 필요가 있다. 이는 논문의 보고 결과가 아니라 **실제 시스템에 적용할 때의 추가 검증 제안**이다.

## 부록: 배경지식

### Control Barrier Function (CBF)

**정의:** 시스템 상태가 안전 영역을 벗어나지 않도록 제어 입력에 조건을 부과하는 수학적 도구다. **예시(설명용):** 로봇 끝단과 장애물 사이의 거리를 일정 수준 이상 유지하도록 속도 명령을 제한한다. **이 글에서의 의미:** 우회 경로 유도가 켜져도 CBF 조건은 QP의 hard constraint로 남는다.

### Quadratic Programming (QP)

**정의:** 이차 목적함수를 선형 또는 적절히 정식화된 제약 아래 최소화하는 최적화 문제다. **예시(설명용):** 목표 속도를 최대한 유지하면서 안전 속도 범위를 만족하는 명령을 찾는다. **이 글에서의 의미:** 원래 VLA 행동과 우회 waypoint 방향 사이에서 안전한 보정 행동을 선택한다.

### Action chunk

**정의:** 미래 여러 시점의 로봇 행동을 한 번에 예측한 묶음이다. **예시(설명용):** 그리퍼가 물체로 접근하는 연속 위치 변화를 한 번의 추론으로 만든다. **이 글에서의 의미:** 묶음의 병진 변위를 누적해 장애물에 막힐 미래 경로를 추정한다.

### Rejoin waypoint

**정의:** 우회 후 원래 계획된 경로로 다시 합류하도록 지정한 중간 목표점이다. **예시(설명용):** 작업대의 장애물을 돌아간 로봇이 다시 파지 접근선에 진입하는 지점을 정한다. **이 글에서의 의미:** 국소 충돌 회피 이후 작업 진행 방향을 회복하는 핵심 단계다.

## Sources

- [Route-Guided CBF-QP Repair 원문 — arXiv:2611.01713 (2026-11-01)](https://arxiv.org/abs/2611.01713)
- [논문 전체 HTML — 방법, SafeLIBERO Table I–II, ablation 및 한계](https://arxiv.org/html/2611.01713v1)
