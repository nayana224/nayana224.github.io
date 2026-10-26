---
layout: feed_note
title: "RLinf v0.4: 로봇 강화학습에서 드라이버·추론·제어 경로를 분리한다"
date: 2026-10-26 12:30:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "10월 20일 공개된 RLinf v0.4는 실물 로봇의 드라이버·작업 계층을 분리하고, 다음 action chunk 추론과 현재 chunk 실행을 겹치는 RTC, 센서·통신 지연을 주입하는 테스트 경로를 확장했다."
---

로봇 강화학습에서 시뮬레이션 성공률이 높아도 실제 장비에 배포하기는 어렵다. 팔·그리퍼·카메라 드라이버가 작업 코드와 얽혀 있고, 다음 행동을 추론하는 동안 제어가 멈추거나 통신 지연이 생긴다. **10월 20일 공개된 RLinf v0.4**는 새로운 단일 정책보다는 이처럼 데이터 수집부터 실물 실행까지 이어지는 **robot learning 시스템 경로**를 확장한 릴리스다.

## 드라이버와 task를 다른 계층으로

새로운 **rlinf.robotics** 인터페이스는 로봇 팔, dexterous hand·그리퍼, 멀티뷰 카메라, 이동 플랫폼과 teleoperation 장치를 조합한다. 하드웨어 드라이버, task 정의, 환경 wrapper를 분리하는 것이 핵심이다. 목표는 하드웨어나 노드 배치를 변경해도 task·policy 코드를 그대로 재사용하는 것이다.

공식 릴리스는 양팔 Franka의 PICO VR teleoperation 및 HG-DAgger, PyTorch OpenPI π₀.₅ 학습·배포 경로, 단일 Franka의 개입 기록과 LeRobot 데이터셋 저장, 그리고 YAM·AgileX Piper·SO-101 지원을 소개한다. 이는 **해당 통합 경로가 구현되었다**는 의미이며, 임의의 로봇이 같은 성능으로 동작한다는 보증은 아니다.

## Action chunk 추론과 실행을 겹치기

**RTC(Real-Time Control)**는 현재 action chunk를 실행하면서 다음 chunk 추론을 수행하고, chunk 경계에 soft/hard masking을 적용해 행동의 급격한 변화를 완화한다. 개발팀은 LIBERO 및 실제 Franka 설정을 포함한 자체 실험에서 rollout의 **inference wait를 초 단위에서 약 2 ms로 축소**, episode time을 최대 **7.4초 단축**했다고 보고했다.

이때 2 ms는 VLA 모델이 전체 action chunk를 2 ms 만에 생성했다는 수치가 아니다. 추론과 실행을 중첩한 뒤 **제어 경로에서 기다린 시간**이다. 실물 적용에서는 카메라 획득→추론→명령 전송의 전체 지연, 실행 주기, chunk 경계의 jerk, 접촉 중 안정성을 따로 계측해야 한다.

같은 릴리스에는 RLT(압축된 제어용 표현 기반 2단계 온라인 RL), STEAM(시연 프레임의 시간 순서로 학습한 진척도 평가), OPD(학생의 on-policy rollout에 교사 모델이 밀도 높은 평가를 제공하는 distillation)도 포함됐다. OPD가 LIBERO-Spatial에서 OpenVLA-OFT student의 성공률을 **67%에서 96% 이상**으로 올렸다는 결과는 릴리스의 특정 **30-step** 조건에 한정된다. 이를 현장 로봇의 일반적인 성공률 향상으로 해석하면 안 된다.

## 실물 링크의 지연을 재현해 시험하기

RLinf v0.4의 real-world simulator는 센서 지연과 클러스터·클라우드/엣지 네트워크의 대역폭 및 지연을 주입한다. Env→Rollout 이미지 전송에는 **XOR-delta와 LZ4/Zstd를 조합한 무손실 압축**을 추가했다. 개발팀은 이미지 payload가 원본의 **36~41%**로 줄면서 복원 결과는 bit-exact라고 보고한다. 하지만 전송량 감소가 동일한 비율의 robot control latency 감소를 뜻하지는 않는다.

Robotics R&D에서 이 기능을 활용하려면 task·reset·카메라 조건을 고정한 뒤 지연, packet loss, 통신 중단과 chunk 경계 불연속을 각각 주입해 비교할 필요가 있다. 성공률뿐 아니라 deadline miss, intervention rate, recovery, emergency-stop 반응을 측정해야 시스템이 실제 배포에 적합한지 판단할 수 있다.

## 마이그레이션과 실험 결과의 한계

기존 v0.3 환경을 그대로 재활용할 수 없다. 기본 스택이 PyTorch 2.11로 바뀌었고 이전 real-world 인터페이스는 **rlinf.robotics / rlinf.envs.real**로 이동했다. 새 JAX-aligned PyTorch OpenPI 구현을 사용하려면 이전 community PyTorch checkpoint를 변환해야 한다.

릴리스가 열거한 성공률·처리량 수치는 **각기 다른 모델, 로봇, 학습 데이터, 시뮬레이션 설정의 개발팀 측정**이다. 단일 통일 벤치마크가 아니며, 임의 로봇에서 실시간성이나 안전성이 검증됐다는 의미도 아니다. 실물 장비의 외부 안전 제어와 실패 시 정지 경로는 별도 검증 대상이다. 이 릴리스의 실질적 가치는 모델 하나의 점수보다 **데이터 수집→학습→비동기 실행→실물 재현 테스트를 모듈화했다는 점**에 있다.

## Sources

- [RLinf v0.4 공식 GitHub 릴리스·테스트·마이그레이션 안내 (2026-10-20)](https://github.com/RLinf/RLinf/releases/tag/v0.4)
- [RLinf 공식 코드](https://github.com/RLinf/RLinf)
- [RLinf 공식 문서](https://rlinf.readthedocs.io/)
