---
layout: feed_note
title: "양손 손가락 조작을 106개 과제로 나눈 BiDex-100"
date: 2026-10-18 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "BiDex-100은 고자유도 양손 dexterous manipulation의 일반화·지시 이행·데이터 효율·장기 작업·기억을 시뮬레이션에서 평가한다."
---

양손 dexterous manipulation을 여러 VLA 모델이 같은 기준으로 비교할 수 있는 벤치마크는 많지 않다. 10월 18일 공개된 **BiDex-100**은 두 종류의 손 로봇 embodiment를 대상으로 106개 시뮬레이션 과제를 구성했다.

과제는 일반화, 언어 지시 이행, 제한된 시연, 장기 작업, 기억의 다섯 역량 축으로 나뉜다. 각 과제에는 시각 또는 공간 조건을 바꾼 out-of-domain 변형이 있고, 데이터셋에는 성공 여부를 검증한 teleoperation 시연 8,080개, 총 625만 프레임이 포함된다. 논문은 일곱 VLA를 통일된 프로토콜로 비교해 기준선을 제공한다.

이는 실로봇 성능 향상을 보인 결과가 아니라 **시뮬레이션 benchmark와 데이터셋의 제안**이다. 시뮬레이션에서의 양손 손가락 조작 점수를 실제 접촉·촉각·하드웨어 성능으로 일반화하면 안 된다. 실물 플랫폼으로 옮길 때는 embodiment별 action space, 접촉 모델, teleoperation 데이터의 편향을 별도로 검증해야 한다.

## 양손 benchmark를 실기 기준으로 옮길 때

106개 과제를 다섯 역량 축으로 나눈 구성은 단순 물체 집기 점수보다 기억·장기 실행·지시 이행을 분리해 비교할 수 있게 한다. 다만 8,080개 검증 시연은 benchmark 내 policy 성능의 상한이나 실제 teleoperation 비용을 바로 알려주지 않는다.

실물 평가로 이어가려면 양손 간 동기화, 손가락 접촉·미끄럼 감지, object handoff, 실패 후 재파지와 안전한 정지 조건을 별도 설계해야 한다. BiDex-100 자체는 simulation 평가라 촉각 센서와 실제 actuator dynamics의 영향을 입증하지 않는다.

## Sources
- [BiDex-100 논문](https://arxiv.org/abs/2610.25459)
- [BiDex-100 프로젝트 페이지](https://bidex-100.github.io/)
