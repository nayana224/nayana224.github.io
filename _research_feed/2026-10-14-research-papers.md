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

## Sources
- [Cracking Mobile Manipulation 논문](https://arxiv.org/abs/2610.19600)
- [논문 HTML과 실험 결과](https://arxiv.org/html/2610.19600v1)
