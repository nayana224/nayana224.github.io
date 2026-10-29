---
layout: feed_note
title: "LEAP 손의 물체 낙하 16→4회: 목표 달성과 안전을 분리한 residual filter"
date: 2026-10-30 06:55:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "10월 27일 공개된 dexterous manipulation 연구는 시뮬레이션에서 학습한 16-DoF LEAP 손의 6D 물체 자세 제어에 별도 residual safety filter를 결합했다. 실제 로봇 4,800개 목표 평가에서 state policy의 낙하는 16→4회로 줄었지만 목표 도달률도 95.2→91.5%로 낮아져 성능·안전 trade-off가 드러났다."
---

손안에서 물체를 회전시키는 로봇손이 **원하는 위치와 방향으로 물체를 옮기면서도 떨어뜨리지 않을 수 있을까?** 성공률만 측정하면 물체를 자주 떨어뜨리는 정책도 좋은 점수를 받을 수 있다. 2026년 10월 27일 공개된 *Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well*은 **목표 자세 도달과 물체 낙하 방지**를 분리해 학습하고, 실물 로봇에서 그 교환관계를 직접 측정한다.

## 회전만이 아니라 손 기준 6D 자세를 목표로

연구진은 16-DoF **LEAP hand**에서 물체의 위치와 방향을 손 좌표계 기준으로 지정하는 in-hand object pose reaching을 다룬다. 손목이 위·아래·옆을 향해도 연속된 목표를 수행해야 하므로, 손바닥에 물체를 얹고 회전시키는 작업보다 어렵다.

학습은 사람 시연 없이 **MuJoCo Warp 기반 시뮬레이션**에서 수행한다. 생성한 grasp 데이터셋으로 초기 상태와 목표를 다양화하고, 손가락 마찰을 비현실적으로 높은 값에서 실제에 가까운 범위로 낮추는 **adaptive friction curriculum**을 적용한다. 모터 응답과 명령 지연을 system identification으로 맞춘 뒤, PPO로 학습한 privileged teacher를 DAgger로 배포 가능한 정책에 증류한다.

배포 정책은 두 종류다. **State policy**는 외부 motion capture로 물체 자세를 읽는다. **Depth policy**는 손목에 장착한 depth camera와 관절 상태만 사용한다. 두 정책을 같은 성능으로 간주하면 안 된다. 시뮬레이션의 정책 주기는 **20 Hz**, 물리 계산은 **120 Hz**이며, 물체마다 별도 정책을 학습한다.

## 안전 정책은 원래 행동을 고치는 별도 층

기존 task policy를 다시 학습하지 않고 고정한 뒤, **ResSafe 기반 residual safety filter**를 추가한다. 실행 행동은 다음처럼 구성된다.

`a_executed = clip(a_nominal + δ, -1, 1)`

여기서 `a_nominal`은 목표 자세를 향한 기존 정책의 행동, `δ`는 안전 필터가 제안하는 보정이다. 필터는 물체를 떨어뜨리지 않고 오래 유지하는 보상을 받되, 원래 행동에서 크게 벗어나는 보정에는 비용을 부과한다. 보정 강도는 배포 시 조절할 수 있다.

이 구조는 **task success와 drop avoidance를 서로 다른 평가 축으로 유지**한다는 점에서 중요하다. 단, 학습된 필터는 물리적 안전을 수학적으로 보증하는 Control Barrier Function이 아니다. 훈련 분포 밖의 접촉이나 센서 오류에서 낙하가 불가능해진다는 뜻도 아니다.

## 실물 4,800개 목표에서 확인한 결과

실험은 전구·고무오리·칼·와인잔 네 물체, 여섯 손목 방향, 두 관측 정책(state/depth), 필터 유무를 조합했다. **총 96회 실행 × 연속 목표 50개 = 4,800개 목표**, 목표당 최대 10초로 **13.3시간의 실물 평가 구간**을 기록했다. 각 관측 정책의 필터 유무 비교는 각각 **1,200개 목표**에 대한 것이다.

**주요 실물 결과 — coarse success 기준: 위치 오차 ≤2 cm, 방향 오차 ≤0.4 rad**

| 정책 | 필터 없음 | 필터 적용 |
| --- | --- | --- |
| State policy 목표 도달 | 95.2% | 91.5% |
| State policy 물체 낙하 | 16회 | 4회 |
| Depth policy 목표 도달 | 71.8% | 66.7% |
| Depth policy 물체 낙하 | 88회 | 46회 |

따라서 논문의 **낙하 75% 감소**는 state policy의 16→4회를 가리킨다. 모든 관측 설정에서 동일한 75% 개선을 보였다는 뜻은 아니다. 더 엄격한 **precise success(≤1 cm, ≤0.2 rad)**는 state policy에서 필터 적용 전후 **75.6→67.2%**로 감소했다. 안전 필터의 이득과 작업 성능 비용을 동시에 보고해야 한다.

Depth policy의 한계도 뚜렷하다. 전구·고무오리는 필터 없이 각각 약 95%, 88%의 coarse success를 보였지만, 칼·와인잔은 약 54%, 50%에 머물렀다. 저자들은 이 두 물체에서 **실제 depth 관측의 pose estimation 오차가 시뮬레이션보다 큰 점**을 원인 후보로 제시한다.

## 응용 데모와 안전성 검증의 경계

연구진은 손목 카메라만 사용해 전구를 소켓에 돌려 끼우거나 물체를 뒤집는 다단계 작업도 보였다. 하지만 이 데모에서 **팔 움직임과 상위 목표는 미리 작성된 명령**이다. 또한 더 강한 필터 설정을 적용한 downstream task에서는 오히려 전구 조립 성공이 **4/5→3/5**, 고무오리 자세 변경·배치 성공이 **7/10→3/10**으로 낮아졌다. 낙하를 줄이는 필터가 모든 접촉 작업의 성공을 높인다고 일반화할 수 없다.

로봇 조작 연구에 적용할 핵심은 모델 이름보다 **평가 프로토콜**이다. 목표 도달률과 별도로 물체 낙하 횟수, 첫 낙하까지의 시간, 낙하 전 연속 성공 목표 수, 보정량을 기록해야 한다. 같은 목표·손목 방향·물체 조합에서 필터 유무를 비교하고, 시각 오차와 접촉 실패를 분리해야 개선 원인을 설명할 수 있다.

이 연구는 **물체별로 정책과 필터를 학습한 단일 LEAP 손 플랫폼**의 결과다. 다양한 물체를 하나의 정책으로 다루거나, 변형체·예측하지 못한 외력·안전 인증 요구사항을 해결했다는 증거는 아니다. 그럼에도 성공률 하나로 평가하던 dexterous policy에 **안전–성능 Pareto trade-off**를 명시적으로 추가했다는 점은 실물 로봇 연구에 유용하다.

## Sources

- [원문 논문 — Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well (arXiv:2610.37652, 2026-10-27)](https://arxiv.org/abs/2610.37652)
- [논문 HTML — 학습 구조, Table II 실물 결과 및 제한사항](https://arxiv.org/html/2610.37652v1)
- [공식 프로젝트 — 4,800개 목표 실험 영상과 인터랙티브 데모](https://ian-chuang.github.io/dexsafe/)
