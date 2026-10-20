---
layout: feed_note
title: "카메라를 움직인 뒤 정책이 낯선 상태를 만나면"
date: 2026-10-16 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "ActiveAlign은 active perception 종료 시점의 관측·로봇 상태에 맞춰 VLA 학습 데이터를 정렬한다."
---

가려진 물체를 보기 위해 카메라를 움직이면 조작 정책은 더 잘 보이는 영상을 얻는다. 하지만 카메라 이동 뒤의 로봇 자세와 관측은 기존 조작 시연과 달라질 수 있다. 10월 16일 공개된 **ActiveAlign**은 이 분포 차이를 active perception과 VLA 사이의 연결 문제로 다룬다.

학습 시 viewpoint module이 만든 카메라 궤적의 끝점에서 기존 시연 궤적에 closed-loop로 정렬하고, 그 뒤 성공적으로 이어진 조작 구간을 정책 fine-tuning에 사용한다. 배포 때는 같은 viewpoint module이 먼저 움직이고, 이어서 정렬된 관측 상태에 맞춰 학습한 VLA가 조작한다.

저자들은 40개 LIBERO 과제에서 π₀가 70.7%, π₀.₅가 72.7% 성공해 각 표준 학습 baseline보다 40.0%p와 26.4%p 높았다고 보고한다. 실제 가림 조건에서는 90회 중 성공이 35회에서 83회로 증가했다. 이 값은 논문이 평가한 특정 과제와 가림 설정에 한정된다.

핵심은 카메라 동작 자체보다 **그 동작이 끝난 뒤의 관측·상태 분포까지 정책 학습에 맞추는 것**이다. 실제 RGB-D 조작 파이프라인에서도 시점 변경 전후의 카메라-로봇 정합과 시작 상태를 별도 검증할 이유가 있다.

## viewpoint module과 조작 정책의 연결부

카메라 이동은 관측 영상만 바꾸지 않는다. 외부 파라미터, robot pose, 가림 구조와 경우에 따라 grasp 접근 경로도 함께 바뀐다. ActiveAlign의 학습은 카메라 궤적 종료 상태에서 demonstration으로 재정렬하므로, viewpoint module이 만든 상태가 학습 분포에 포함되는지가 핵심이다.

실제 RGB-D 시스템에서는 카메라 extrinsic 변화, depth 품질, robot-camera timestamp, 종료 pose 편차를 기록해야 한다. 논문 수치의 가림 설정을 넘어서 임의의 카메라 장착·캘리브레이션 오차까지 해결했다고 볼 수는 없다.

## Sources
- [ActiveAlign 논문](https://arxiv.org/abs/2610.23378)
- [ActiveAlign 논문 HTML과 평가 설정](https://arxiv.org/html/2610.23378v1)
