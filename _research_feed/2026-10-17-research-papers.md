---
layout: feed_note
title: "LIBERO 점수만으로 로봇 정책의 배포 강건성을 말하기 어렵다"
date: 2026-10-17 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "LIBERO-Pro2.0은 1,648개 분포 이동 과제 인스턴스로 장면뿐 아니라 실행·로봇 상태·언어 변화까지 평가한다."
---

익숙한 LIBERO 설정에서 높은 성공률을 얻어도 카메라·실행 조건이 달라졌을 때의 강건성을 뜻하지는 않는다. 10월 17일 공개된 **LIBERO-Pro2.0**은 embodied foundation model을 분포 이동 조건에서 평가하기 위한 벤치마크다.

벤치마크는 condition, environment, observation, execution, robot-state configuration, language의 여섯 축에서 22개 정적 perturbation과 20개 runtime intervention을 구성한다. 저자들은 물리적 타당성을 검토한 **1,648개 이동 과제 인스턴스**로 17개 정책을 평가했다.

논문에서 runtime shift가 적용되자 평가 정책의 평균 성공률은 **26.5%p 하락**했고, 개별 하락 폭은 최대 32.5%p였다. 이는 해당 벤치마크의 실험 결과이지 실제 작업장 전체의 실패율 추정치는 아니다. 자료와 모델 모두 논문 연구진이 구성·선정했다는 점도 재현 평가에서 확인할 요소다.

로봇 정책을 비교할 때 nominal task 성공률과 함께 카메라·제어 주기·로봇 상태 설정·언어 지시가 바뀐 조건을 따로 보고해야 한다는 점을 구체적인 테스트 항목으로 만든 연구다.

## 벤치마크에서 분리해 볼 shift

정적 perturbation은 시작 전 조건을 바꾸고, runtime intervention은 실행 도중 조건을 바꾼다. 두 종류는 같은 distribution shift가 아니다. 평균 26.5%p 하락은 runtime shift 아래 취약성을 드러내지만, 어떤 정책이 어느 intervention에서 실패했는지를 분해해야 원인을 찾을 수 있다.

실제 로봇 검증에서는 camera viewpoint, 제어 주기, 관절 초기 상태, 언어 paraphrase를 하나씩 바꾸고 조합 변화도 추가해야 한다. LIBERO-Pro2.0은 이런 시험을 표준화하는 benchmark이며, 공장 환경의 위험률이나 실제 하드웨어의 모든 변화 범위를 직접 추정하는 자료는 아니다.

## Sources
- [LIBERO-Pro2.0 논문](https://arxiv.org/abs/2610.24587)
- [논문 HTML과 벤치마크 구성](https://arxiv.org/html/2610.24587v1)
