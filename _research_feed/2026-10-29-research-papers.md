---
layout: feed_note
title: "CARD: 손가락 자세가 아니라 접촉 위치·방향·힘을 옮긴다"
date: 2026-10-29 07:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "10월 27일 공개된 CARD는 사람 손 시연을 로봇손으로 retargeting할 때 관절 자세 대신 접촉 위치·밀기 방향·힘을 보존한다. 실제 로봇의 동일 궤적 재생에서 촉각 힘 추종을 추가하자 30회 중 성공이 4회에서 25회로 늘었지만, 대규모 closed-loop 정책 성능을 입증한 결과는 아니다."
---

손가락 끝이 같은 위치에 도달해도 물체가 미끄러지면 조작은 실패한다. 기존 human-to-robot retargeting은 주로 손가락 관절각이나 fingertip 위치를 맞춘다. 하지만 손이 물체의 **어디를, 어느 방향으로, 얼마나 세게 누르는지**가 빠지면 사람의 접촉 기술이 로봇에 전달되지 않는다.

10월 27일 공개된 *CARD: Contact-Anchored Retargeting for Dexterous Manipulation*은 사람 손의 동작을 로봇손에 옮길 때 **contact force target**을 중심에 놓는다. 이 연구의 목표는 VLA를 새로 학습하는 것이 아니라, 사람 시연을 로봇에서 재생 가능한 joint trajectory와 force target으로 변환하는 것이다.

## 세 가지 접촉 정보를 공통 표현으로

CARD는 손의 각 의미 영역에 contact anchor를 부여한다. 하나의 anchor는 **접촉 위치(center of pressure), 물체를 미는 단위 방향, 힘의 크기**로 구성된다. 손가락별 distal·middle·proximal 영역과 손바닥을 공유 의미 체계로 삼아, 서로 다른 로봇손의 링크에 대응시킨다.

입력은 휴대전화 단안 영상, 촉각 장갑, motion capture와 장갑의 조합이다. 단안 영상은 힘을 직접 측정하지 못한다. 연구진은 **Vid-HACO**로 MANO 손 메시의 접촉 정점을 추정하고, 시연 전체의 grasp balance 조건으로 힘을 합성한다. 따라서 영상에서 얻은 force target은 측정값이 아니라 **모델 추정치**다.

Vid-HACO는 V-JEPA 2.1 기반 인코더를 이용해 8프레임 문맥에서 접촉을 추정한다. 12개 데이터셋의 약 155만 프레임으로 학습했으며, 학습에 포함되지 않은 HRDexDB에서는 vertex-level contact F1 **67.2**를 기록했다. 공개 HACO의 **63.3**, 같은 데이터로 재학습한 HACO-R의 **62.6**과 비교한 수치다. 이는 접촉 **분류 성능**이지 로봇 작업 성공률은 아니다.

## Retargeting은 접촉 제약을 먼저 맞춘다

사람 손 자세로 로봇 관절의 초기값을 만든 뒤, 프레임마다 로봇 손목 자세와 관절각을 최적화한다. 목적함수는 **contact reach·push direction·anti-slip**, 비접촉 손가락의 원래 자세 유지, 시간적 smoothness, self/object collision 회피를 함께 다룬다. 큰 힘을 전달해야 하는 접촉에는 더 높은 가중치를 준다.

핵심은 **물체의 CAD 모델이나 physics simulator 없이도** retargeting을 수행하도록 설계했다는 점이다. 다만 충돌 계산까지 완전히 물체 정보가 없는 것은 아니다. 영상·장갑 입력에서는 시연 전체의 contact anchor를 모아 만든 **pseudo-object의 convex hull**을 충돌장으로 사용한다.

최적화는 GPU의 sampling-based Cross-Entropy Method(CEM)를 사용한다. 논문은 RTX 5090 한 장에서 약 **10 FPS**의 retargeting 처리량을 보고했다. 이는 시연 궤적을 생성하는 처리량이며, 로봇의 실시간 저수준 제어 주파수를 뜻하지 않는다.

## 접촉 재현과 실제 작업 성공은 따로 측정했다

논문의 **contact rate**는 전체 작업 성공률이 아니다. 지정된 접촉 anchor가 올바른 손가락 안쪽 표면의 **2 mm 이내**에 도달한 anchor-frame 비율이다. 동일한 22-DoF SHARPA Wave 손으로 비교했을 때:

- 단안 영상 20개: CARD **61.4%**, DexPilot **9.7%**.
- 촉각 장갑·motion capture 66개: CARD **77.7%**, DexPilot **3.8%**.
- GRAB 시연 100개: CARD **43.1%**, DexPilot **4.9%**, 물체 메시를 사용하는 ReGrind **22.5%**.

실물 재생은 별도로 검증했다. SHARPA Wave에서 **동일한 CARD 궤적**을 위치 명령만으로 실행하면 망치 들어 올리기 1/10, 컵 들어 올리기 3/10, 머스터드 짜기 0/10이었다. 촉각 센서로 목표 힘을 추종하는 **tactile tracking controller**를 켜면 각각 **8/10, 10/10, 7/10**, 합계 **4/30 → 25/30**으로 바뀌었다.

여기서 논문이 말하는 **open-loop replay**는 물체 자세를 다시 추정하거나 학습된 policy로 재계획하지 않는다는 뜻이다. **손가락 힘에는 촉각 feedback loop가 존재한다.** 이를 모든 제어가 open-loop라고 해석하면 안 된다. 또한 CARD를 physics-based retargeting에 결합한 별도 실험에서는 GRAB strict task success가 **12% → 32%**였는데, 이는 시뮬레이션의 50개 GRAB clip 기준이며 앞선 실물 30회 결과와 다른 평가다.

## 로봇 연구에서 검증할 것

사람 시연을 모으는 단계에서는 joint pose만 저장하기보다 **contact location, force direction, force magnitude, contact onset/release**를 분리해 다루는 설계가 유용하다. 실제 장비에서는 관절 궤적 오차와 별개로 접촉 유지율, 정상 힘 오차, slip, 물체 변위, sensor dropout 때의 동작을 기록해야 한다.

다만 CARD의 재생은 물체가 크게 이동하면 스스로 복구하지 못한다. 촉각이 없는 다른 손에서는 동일한 force-tracking을 그대로 구현하지 못했고, Unitree Dex3-1에서는 grasp action을 1.2배로 조정했다. 다양한 물체와 손에 대한 **closed-loop learned policy의 일반화**는 아직 이 논문이 입증한 범위가 아니다. 따라서 CARD는 완성된 범용 조작 정책보다 **접촉을 보존하는 데이터 변환 및 실행 인터페이스**로 평가하는 편이 정확하다.

## Sources

- [CARD 원문 — arXiv:2610.36539 (2026-10-27)](https://arxiv.org/abs/2610.36539)
- [CARD 논문 HTML — 방법, Table 1–3, 실물 replay, 한계](https://arxiv.org/html/2610.36539v1)
- [CARD 연구진 공식 프로젝트 — 데모 영상, 하드웨어 및 접촉 비교](https://card-retargeting.github.io/)
