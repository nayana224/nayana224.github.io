---
layout: feed_note
title: "경로를 못 찾는 것과 경로가 없는 것을 구분하는 motion planning"
date: 2026-09-26 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "구성공간 obstacle 경계의 분리 구조를 추적해 경로 부재를 인증하고, infeasibility를 일으키는 장애물 후보까지 돌려주는 GPU 가속 방법이 제안됐다."
---

Sampling-based motion planner가 제한 시간 안에 경로를 찾지 못하면 두 경우를 구분하기 어렵다. **경로가 없거나, 경로가 있지만 sampler가 아직 찾지 못했거나.** 9월 26일 공개된 이 연구는 경로 탐색에 실패했다는 사실을 infeasibility로 간주하지 않고, 시작·목표 구성이 구성공간에서 서로 분리되어 있음을 기하적으로 확인하려 한다.

방법은 로봇의 forward kinematics와 obstacle signed distance function으로 구성공간의 collision boundary를 표현한다. 이 경계가 시작 구성과 목표 구성 사이를 분리하는지를 manifold tracing과 connected-component query로 판정한다. 더 나아가 경계를 만든 obstacle identity를 기록해, 어떤 장애물들이 현재 infeasible 판정에 관여하는지 식별한다. 저자들은 이를 **actionable infeasibility**라고 부른다. 장애물을 제거하면 경로가 가능해질 수 있다는 진단 단서를 주지만, 최적 경로나 최적 obstacle 제거 집합을 보장하는 것은 아니다.

### 평가 범위와 계산 비용

평가는 CUDA C++ 구현으로 4-DOF와 5-DOF 로봇의 simulation planning 장면에서 이뤄졌다. 실험 장비는 Intel Ultra 9 185H CPU와 RTX 4060 8GB GPU였고, 각 장면의 실행 시간은 10회 평균으로 보고됐다. 저자들은 기존 SVM 기반 infeasibility 방법보다 4-DOF 사례에서 약 **10배**, 5-DOF에서 약 **2배** 빠르면서 obstacle contact manifold 구조를 포착했다고 보고한다. 일부 5-DOF 장면의 경계 추적은 수 분이 걸린다.

여기서 “경로 없음”의 근거도 무조건적인 ground truth는 아니다. 논문은 고차원 장면의 정확한 infeasibility 정답을 얻기 어렵다고 밝히며, 비교용 PRM을 30분 실행해 경로가 없다는 강한 근거를 구성했다. 또 경계 추적 해상도 λ가 너무 크면 좁은 obstacle feature를 놓칠 수 있다. 저자들은 이론적 보장을 위한 추가 증명이 향후 과제로 남는다고 적었다.

MoveIt 2 같은 planning stack에서 이 접근이 겨냥하는 곳은 일반적인 “planner를 더 빨리 돌리기”가 아니다. **계획 실패를 명시적으로 설명하고, scene 수정이나 목표 재설정에 쓸 진단 정보를 제공하는 단계**다. 다만 현재 결과는 저자 구현·제한된 로봇 차원과 simulation scene에 해당하며, 실제 MoveIt planning pipeline에 바로 적용되는 플러그인이나 범용 실시간 infeasibility certificate로 읽어서는 안 된다.

## Sources
- [논문 원문 — Towards Kinematic Actionable Infeasibility Detection in Motion Planning](https://arxiv.org/abs/2609.32806)
- [논문 HTML과 평가·한계](https://arxiv.org/html/2609.32806v1)
