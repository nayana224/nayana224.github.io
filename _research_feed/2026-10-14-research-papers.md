---
layout: feed_note
title: "모바일 조작은 VLA보다 실패가 쌓이는 지점을 먼저 봐야 한다"
date: 2026-10-14 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "고정된 subtask VLA를 바꾸지 않고 계획·베이스 위치·국소 조작의 실패를 진단해 단계별 개입을 추가한 연구다."
---

원자적 조작 과제에서는 80% 성공하던 subtask VLA가 이동 베이스와 여러 단계를 연결한 모바일 조작에서는 19%에 그쳤다. 10월 14일 공개된 **Cracking Mobile Manipulation**은 이 차이를 더 큰 정책을 학습하는 문제로만 보지 않고, 실행 중 어느 단계에서 실패가 누적되는지 추적한다.

연구진은 실패를 task planning, navigation/base positioning, local manipulation으로 나누고, 각 단계에 시연 기반 계획 가이드·시각 메모리·베이스 위치 조정·말단 조정 같은 개입을 추가했다. underlying subtask VLA는 고정했다. 단계별 개입을 더한 시스템의 성공률은 RoboCasa365 개발 에피소드에서 19%에서 47%로 올랐고, 설계를 고정한 held-out seed에서는 18%에서 49%로 올랐다.

논문은 BEHAVIOR-1K 다섯 과제에서 14%→37%, 두 실제 로봇 과제에서 20회 중 5회→13회도 보고한다. 실제 로봇 표본은 20회이고, 이는 제한된 평가다. 따라서 이 결과를 범용 모바일 매니퓰레이션 성능으로 일반화하기보다, **실패 원인별 개입을 분리해 검증하는 실험 설계**에 주목할 만하다. 코드는 논문 공개 시점에 아직 공개 예정 상태였다.

## 단계별 개입의 인과효과를 읽기

기반 VLA를 고정한 상태에서 planning·navigation·manipulation 개입을 더한 비교는 개선이 policy 재학습 때문인지 system correction 때문인지 구분하는 데 유용하다. held-out seed와 실제 로봇 결과가 함께 있다는 점은 simulation 개발 성능만 제시하는 것보다 강한 근거지만 실물 두 과제, 20회 평가라는 한계는 남는다.

현장 재현에서는 실패를 같은 taxonomy로 분류하고 개입 하나씩 제거하는 ablation이 필요하다. 베이스 위치 오차가 말단 조작 실패로 전파되는 경우처럼 원인과 최종 증상이 다를 수 있어, 단일 task success만으로 어떤 개입이 효과를 냈는지 알기는 어렵다.

## Sources
- [Cracking Mobile Manipulation 논문](https://arxiv.org/abs/2610.19600)
- [논문 HTML과 실험 결과](https://arxiv.org/html/2610.19600v1)
