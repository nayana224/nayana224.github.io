---
layout: feed_note
title: "Isaac Sim 6.2: Newton substep 누락과 Teleop의 그리퍼 명령 덮어쓰기를 고쳤다"
date: 2026-10-28 06:55:30 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "10월 22일 공개된 Isaac Sim 6.2는 Isaac Lab 3.0 지원용 안정화 릴리스다. Newton의 CUDA graph·substep 상태 누락, floating-base 목표 인덱싱, Teleop IK의 그리퍼 DOF 덮어쓰기를 수정하고 ROS 2 joint naming·센서 API·UCX 호환성에 마이그레이션 조건을 추가했다."
---

시뮬레이션이 정상 실행돼도 **물리 substep이 빠지거나 IK가 그리퍼 관절까지 덮어쓰면**, 로봇 학습 데이터의 행동 정답부터 틀어질 수 있다. 2026년 10월 22일 발표된 **Isaac Sim 6.2.0**은 Isaac Lab 3.0을 지원하기 위한 안정화 릴리스로, 이런 **제어·물리·센서 경계의 재현성 문제**를 구체적으로 수정했다.

10월 20일 정식 출시된 **Isaac Lab 3.0**이 학습 백엔드와 실행 구조를 바꾼 소식이라면, 이번 6.2는 별개의 **Isaac Sim 런타임·teleoperation·ROS 2 호환성 변경**이다. 단순히 새로운 학습 모델이나 성능 점수를 발표한 것은 아니다.

## Newton에서 사라지던 substep과 관절 목표

릴리스 노트에 따르면 Newton 백엔드는 **짝수 substep 수와 CUDA graph capture를 함께 쓰는 경우** 발생할 수 있던 물리 substep 및 tensor-view write 누락을 수정했다. Floating-base 로봇의 coordinate-layout position target 인덱싱 오류도 고쳤다.

이 문제는 학습 정책의 우열보다 **물리 적분 횟수, 관절 목표, 관측 state가 실제로 같은 시뮬레이션 시간축을 가리키는지**에 영향을 준다. GPU 가속을 켜고 끈 두 실험의 성공률이 다르다면, 정책 차이보다 먼저 substep·state-buffer 경로를 비교할 이유가 생긴다.

Newton이 모델을 다시 빌드한 뒤에는 기존 rigid-body·articulation·contact view가 무효화된다. 새 API의 `check()`가 `False`를 반환하면 **view를 다시 생성**해야 한다. 과거 view를 그대로 참조하는 코드는 버전 업그레이드 시 명시적으로 점검해야 한다.

## Teleoperation의 IK와 그리퍼는 다른 명령이어야 한다

Isaac Teleop 1.4.145 통합에서는 IK가 **팔 관절을 이름으로 찾도록** 바뀌었다. 기존에는 IK 경로가 그리퍼 DOF까지 덮어쓸 수 있었는데, 6.2에서 이를 수정했다. Robotiq 2F-85·Hand-E용 floating-gripper scene/profile도 추가됐다.

이 수정이 중요한 이유는 조작 시연의 **팔 궤적과 grasp/open 명령이 독립적으로 보존되어야** 하기 때문이다. 시연 재생 중 손가락 명령이 예상치 못하게 변한다면 데이터셋의 파지 타이밍이나 정책 문제가 아니라 IK joint mapping부터 확인해야 한다. 단, 수정이 모든 사용자 정의 로봇의 joint mapping 정확성을 자동 보장하는 것은 아니다.

## ROS 2·센서·UCX 경계에서 바뀐 계약

ROS 2 simulation control은 이제 **robot-schema joint name을 우선** 사용한다. 예전 이름 지정 방식은 당장 제거되지는 않았지만 경고가 발생하며, 마이그레이션 시 `isaac:nameOverride`에서 대소문자가 다른 `isaac:NameOverride`로 전환해야 한다. 자동 생성 simulation-interface 이름에는 절대 USD prim path가 사용된다.

센서 읽기 계약도 달라졌다. `get_sensor_reading()`은 **소유권이 있는 snapshot**을 반환하고, 갱신되는 데이터를 직접 읽어야 할 때는 read-only `get_sensor_reading_view()`를 사용한다. 이전 버전에서 반환 객체가 계속 갱신된다고 가정한 코드라면 stale data를 읽을 수 있다.

UCX는 **Holoscan protocol 2**로 바뀌었으며, 예전 Isaac OS wire codec과 호환되지 않는다. 혼합 버전 노드의 통신 실패를 모델 추론 문제로 오인하지 않도록 양쪽 peer의 프로토콜 버전을 함께 점검해야 한다. 또한 Cortex와 `RMPflowCortex` 등록은 제거됐다. 지원되는 `RMPflow` 등의 정책으로 바꾸되 상위 작업 순서는 애플리케이션이 담당해야 한다.

## 로봇 연구 환경에서 확인할 최소 회귀 테스트

업그레이드 전후 같은 USD·초기 상태·명령 시퀀스로 **(1) 물리 substep별 state와 접촉, (2) 팔 IK 실행 중 그리퍼 목표 유지, (3) ROS 2 JointState 이름과 명령 매핑, (4) 센서 snapshot/view 갱신 시점, (5) UCX peer 연결**을 따로 비교하는 것이 유용하다. URDF exporter의 collision geometry와 mimic joint 처리도 실물 모델을 옮길 때 검증 대상이다.

**주의할 범위:** 6.2의 수정 목록은 특정 버그와 API 계약에 대한 공식 릴리스 정보다. 이 문서만으로 시뮬레이션이 모든 실제 접촉을 정확히 재현한다거나 정책 성공률이 개선된다고 결론 내릴 수 없다. Teleop 번들 런타임은 Linux x86_64에 한정되며, Ubuntu 22.04 지원은 이번 버전에서는 유지되지만 향후 제거가 예고됐다. 실제 도입 시에는 사용 중인 ROS 2 배포판·드라이버·물리 백엔드 조합을 고정하고 회귀 시험을 통과시켜야 한다.

## Sources

- [Isaac Sim 6.2 공식 출시 공지 — GitHub Discussion (2026-10-22)](https://github.com/isaac-sim/IsaacSim/discussions/900)
- [NVIDIA Isaac Sim 6.2.0 공식 Release Notes — 변경·제거·마이그레이션](https://docs.isaacsim.omniverse.nvidia.com/latest/overview/release_notes.html)
