---
layout: feed_note
title: "FocusVLA: 다음 행동의 의도로 카메라 시점을 고른다"
date: 2026-10-26 12:05:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "10월 22일 공개된 FocusVLA는 최근 행동으로 앞으로 필요한 시각 정보를 예측하고, VLA의 action step마다 전역·손목 카메라의 기여도를 조절한다. RoboTwin 2.0에서는 π₀.₅ 대비 10.10%p 높은 평균 성공률을 보고했다."
---

로봇이 물체를 찾을 때와 집을 때 필요한 카메라는 다르다. 전체 장면을 보여주는 외부 카메라는 대상과 경로를 파악하는 데 유리하고, 손목 카메라는 물체와 그리퍼가 가까워진 접촉 단계에서 세부 정보를 제공한다. 그런데 여러 뷰를 입력받는 VLA도 실제로는 **초기에 익힌 특정 뷰에 계속 의존**할 수 있다.

10월 22일 arXiv에 공개된 *FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models*는 이 현상을 **view-dependency inertia**로 분석한다. 핵심은 카메라를 더 추가하는 대신, **앞으로 수행할 행동의 성격에 맞춰 뷰의 기여도를 바꾸는 것**이다.

## 현재 영상만 보지 않고 미래 interaction intent를 예측한다

FocusVLA는 π₀.₅ 기반의 다중 시점 VLA에 두 모듈을 붙인다.

**Future Intent Bridge**는 현재 전역·로컬 영상, 언어 지시, 로봇 상태, 짧은 행동 이력을 이용해 미래 action chunk의 각 단계가 국소 상호작용에 가까운지 예측한다. 학습에 쓰는 약한 supervision은 엔드이펙터의 이동 속도·경로 변화 및 사용 가능한 그리퍼 닫힘 신호로부터 구성하므로, 모든 시연에 사람이 작업 단계를 수작업으로 표기할 필요는 없다.

**Action-Side Dynamic Routing**은 그 예측을 각 행동 단계의 전역·로컬 뷰 가중치로 바꾼다. 논문의 핵심 융합은 다음처럼 표현된다.

\[
c^{(k)} = \alpha_g^{(k)}c_g^{(k)} + \alpha_l^{(k)}c_l^{(k)}
\]

여기서 \(k\)는 미래 action step, \(c_g\)와 \(c_l\)은 각각 전역·로컬 영상에서 뽑은 action context, \(\alpha_g\)와 \(\alpha_l\)은 합이 1인 routing weight다. 동일한 action chunk 안에서도 단계별 가중치가 달라질 수 있다. 라우팅은 이미지 인코더 자체를 바꾸는 것이 아니라 **action 생성 측에서 시각 context를 조정**한다.

## 무엇을 검증했나

저자들은 먼저 Stack Blocks Three 작업의 20회 실행씩을 비교했다. 기존 π₀.₅ 다중 뷰 정책의 성공률은 마스킹이 없을 때 85%, 계획 단계에서 전역 뷰를 가리면 65%, 로컬 뷰를 가리면 20%였다. 전역 정보를 필요로 하는 단계에서도 로컬 뷰 의존도가 크다는 진단에 힘을 싣는다. 단, attention 비율만으로 인과관계를 단정할 수 없어 마스킹 실험을 함께 사용했다.

**Key result — 논문 저자 보고**

- **RoboTwin 2.0:** 50개 작업, 작업당 100회 평가. 평균 성공률 π₀.₅ **66.82% → FocusVLA 76.92%** (**+10.10%p**).
- **실제 로봇:** 6개 조작 과제 평가에서 저자 보고 성공률 **71.7% → 85.0%** (**+13.3%p**).

저자들은 비교 모델과 FocusVLA의 시연 데이터, 최적화 step 수, 평가 seed와 프로토콜을 맞췄다고 기술한다. 따라서 결과는 단순히 추가 데이터로 학습했기 때문이라는 설명과 구분된다. 그러나 수치가 서로 다른 로봇·카메라 배치·환경에서도 유지된다는 의미는 아니다.

## Robotics R&D에서의 의미와 한계

이 연구의 유용한 관점은 **멀티카메라 입력을 고정적으로 합치는 대신, 제어 단계별로 필요한 관측 정보를 할당**한다는 것이다. 특히 물체 접근, 정렬, 파지, 운반처럼 시야 요구사항이 바뀌는 manipulation pipeline에서 확인할 가치가 있다. 구현할 때는 뷰별 attention 가중치만 그릴 것이 아니라 시점 마스킹, 물체 위치 변경, 카메라 가림, 조작 성공률을 함께 측정해야 한다.

다만 future intent label은 그리퍼와 엔드이펙터 운동의 휴리스틱에서 출발한다. 느린 자유공간 이동, 접촉 없이 멈추는 행동, 예상과 다른 실패 복구 동작에서는 단계 구분이 틀릴 수 있다. 또 논문은 제한된 시뮬레이션 및 실제 로봇 과제에서의 결과를 보고하므로, 계산 지연과 하드웨어 변경에 따른 실시간 폐루프 성능은 별도 검증이 필요하다.

이 논문은 2026년 3월 공개된 동명 *FocusVLA: Focused Visual Utilization for Vision-Language-Action Models*와 **다른 연구**다. 여기서의 기여는 시각 patch 선택 일반론이 아니라, **미래 interaction intent에 따라 전역·로컬 카메라의 action-step별 사용 비중을 조절**하는 방식이다.

## Sources

- [FocusVLA 원문 — arXiv:2610.31423 (2026-10-22)](https://arxiv.org/abs/2610.31423)
- [FocusVLA 전체 논문 HTML — 구조, 실험 표, 제한사항](https://arxiv.org/html/2610.31423v1)
- [동명의 별도 2026년 3월 FocusVLA 논문 — 연구 구분용](https://arxiv.org/abs/2603.28740)
