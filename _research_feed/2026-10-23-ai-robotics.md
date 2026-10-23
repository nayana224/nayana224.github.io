---
layout: feed_note
title: "Isaac Lab 3.0 정식 출시: Isaac Sim 없이도 로봇 학습을 실행한다"
date: 2026-10-23 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "10월 20일 공개된 Isaac Lab 3.0은 물리 엔진과 렌더러를 분리하고 Newton·OV 백엔드에서 Isaac Sim 없는 학습을 지원한다. 기존 2.x 코드에는 quaternion 순서와 데이터 접근 방식 변경이 따른다."
---

10월 20일 **Isaac Lab 3.0 정식 버전(v3.0.0)**이 공개됐다. 이번 릴리스의 핵심은 Isaac Sim을 모든 작업의 필수 실행 환경으로 두지 않는 것이다. 지원되는 로봇 학습 과제는 Newton 또는 독립형 OV 백엔드에서 실행하고, ROS bridge·XR·Kit 기반 기능이 필요할 때 전체 Isaac Sim 스택을 선택할 수 있다. 9월 Early Access에서 제시한 구조를 정식 릴리스로 안정화했으며, 공식 릴리스는 Isaac Sim 6.2를 대상으로 한다.

## 물리 엔진·렌더링·시각화를 분리한 실행 구조

Isaac Lab 3.0은 공통 task API 아래에서 물리 백엔드, 렌더러, 시각화 도구를 선택한다. 물리에는 Newton의 MuJoCo-Warp·VBD·MPM 경로와 OVPhysX, Isaac Sim PhysX 등이 있고, 시각화에는 Newton GL·Viser·Rerun·Kit 등을 사용할 수 있다. 지원 조합은 **과제마다 다르다**. 같은 환경 코드가 모든 물리 엔진에서 수정 없이 동일하게 동작하거나 같은 접촉 결과를 낸다는 의미는 아니다.

자산·센서 데이터는 `ProxyArray`로 노출된다. 예를 들어 `robot.data.joint_pos.torch`와 `robot.data.joint_pos.warp`처럼 PyTorch와 Warp 표현을 명시적으로 선택한다. 이 경로는 불필요한 변환·복사를 줄이도록 설계됐다. 학습·재생도 `uv run isaaclab train`, `uv run isaaclab play`라는 통합 명령을 사용한다. 릴리스에는 변형체·케이블·입자 시뮬레이션과 PhysX↔Newton 정책 전환 안내, 시연 기록·재생 및 정책 배포 도구도 포함된다.

## 기존 로봇 프로젝트에서 먼저 확인할 호환성

2.x에서 옮길 때 가장 놓치기 쉬운 변화는 **quaternion 순서가 WXYZ에서 XYZW로 바뀐 것**이다. 항등 회전은 `(1, 0, 0, 0)`에서 `(0, 0, 0, 1)`로 표현된다. 초기 자세·목표 pose·카메라 외부 파라미터·제어기 입력에 기존 순서를 그대로 적용하면 텐서 shape이 맞더라도 회전이 잘못될 수 있다. 기존 `.data.*`를 직접 Torch 텐서로 다루던 코드도 `.torch` 접근을 확인해야 한다. 공식 마이그레이션 문서는 별도 Python 3.12 환경에서 이전을 시작하도록 안내한다.

로봇 조작 연구에서는 동일한 과제를 여러 물리 백엔드에서 비교하고, 접촉·변형체·카메라 파이프라인을 나누어 실험할 수 있다는 점이 실용적이다. 다만 **시뮬레이터를 바꾸는 것과 sim-to-real 성능을 확보하는 것은 별개**다. 그리퍼 접촉력, 마찰, 센서 지연, action·observation 인터페이스와 실제 로봇에서의 성공률은 별도로 검증해야 한다. 이번 발표는 프레임워크와 실행 경로의 정식 출시이지, 임의의 로봇 정책이 실제 환경에서 더 잘 작동한다는 성능 입증은 아니다.

## Sources
- [Isaac Lab v3.0.0 공식 GitHub 릴리스 (2026-10-20)](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0)
- [Isaac Lab 3.0 공식 마이그레이션 가이드](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/migrating.html)
- [Isaac Lab 3.0 백엔드와 프리셋 공식 문서](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/backends_and_presets.html)
