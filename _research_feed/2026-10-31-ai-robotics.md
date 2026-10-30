---
layout: feed_note
title: "FineART 공개: 양팔 로봇 4만 시연에 53만 개의 단계별 언어를 붙였다"
date: 2026-10-31 07:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "Scale AI와 Hugging Face가 10월 29일 FineART 데이터셋·FineART-VLA를 공개했다. 40,543개 양팔 시연에 533,913개 subtask를 시간 구간별로 주석 처리해 장기 작업의 계획과 제어를 함께 학습하지만, 보고된 성공률은 제한된 실물 평가 조건에 속한다."
---

로봇에게 “상자를 열고 물건을 꺼내라”는 한 문장만 붙여 학습시키면, **상자 절개·덮개 펼치기·내용물 꺼내기 중 어느 단계에서 무엇을 해야 하는지**는 시연 영상과 행동에서 스스로 찾아야 한다. 2026년 10월 29일 Scale AI와 Hugging Face LeRobot이 공개한 **FineART**는 이 중간 단계를 데이터셋의 명시적인 학습 신호로 만든다.

*FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation* 논문 자체는 **9월 29일 arXiv에 제출**됐다. 이번 소식의 시점은 새 논문 제출이 아니라 **10월 29일 데이터·모델·LeRobot 학습 경로의 공개 발표**다.

## Episode 하나에 문장 하나가 아니라 시간축을 붙인다

FineART는 **40,543개 teleoperation episode, 1,718시간, 151개 작업**으로 구성된다. 각 episode에는 전체 작업 설명과 별도로 시작 시각이 지정된 **533,913개 subtask 주석**이 있다. 평균 약 13개의 단계가 하나의 episode에 연결된다.

수집 장비는 Trossen Stationary AI(ALOHA 계열) 양팔 로봇이다. 공개 데이터 카드 기준으로 **14차원 joint·gripper state/action**, 상단·하단·좌우 손목의 **RGB 카메라 4대**, **30 fps** 영상이 LeRobot v3 형식에 담긴다. 주석은 teleoperator와 다른 사람이 작성하고 제3팀이 검수했다고 발표했다.

전체 시간의 약 **77%는 pick-and-place·sorting**, 나머지 약 **23%는 천·케이블·도구·정밀 삽입** 등의 접촉이 중요한 작업이다. 따라서 “다양한 로봇 embodiment에서 수집한 데이터”가 아니라 **하나의 양팔 플랫폼에서 수집한 다양한 작업 데이터**로 읽어야 한다.

## FineART-VLA: 다음 단계를 언어로 예측하고 행동으로 실행

기존의 단일 task-level label은 관측과 최종 목표를 직접 action에 연결한다. FineART-VLA는 한 정책 안에서 **System 2의 subtask 언어 예측**과 **System 1의 저수준 행동 생성**을 결합한다. 시점에 맞는 subtask를 학습 중 예측하도록 중간 학습(mid-training)을 수행한 뒤, 예측한 단계에 조건화해 행동을 생성한다.

데이터에는 각 프레임의 `language_persistent`에 episode 전체 subtask 목록과 시작 timestamp가 들어 있다. 현재 프레임의 `timestamp`보다 작거나 같은 가장 최근 subtask를 활성 단계로 선택할 수 있다. 반면 `language_events`는 이 데이터에서 비어 있다. 즉 **언어 주석의 시간 정렬**이 핵심이며, 단순히 episode 설명 문장을 여러 개로 늘린 것과 다르다.

## 실물 결과는 무엇을 비교했나

저자들은 **실물 평가 3,400 rollout**을 수행했다고 발표하고, 다음과 같은 제한된 과제별 비교를 제시했다.

- **공간 지시 구별** 과제: subtask mid-training 전후 성공률 **32% → 100%**.
- **처음 보는 장기 작업**: 사람이 다음 subtask를 단계별로 알려주는 조건에서 **16% → 76%**. 이는 사람의 도움 없이 같은 성공률을 달성했다는 뜻이 아니다.
- **다른 로봇(YAM)으로 전이**: mid-training한 모델이 비교 기준선과 유사한 성능에 도달하는 데 필요한 fine-tuning 데이터가 약 **10분의 1**이라고 보고했다.

수치는 논문과 공개팀의 평가 설정에 한정된다. 세 결과는 서로 다른 과제·보조 조건의 실험이므로 하나의 범용 성공률로 합칠 수 없다. 새로운 물체·카메라·그리퍼에 대한 독립 재현 결과나 장기 운영 안정성을 증명하지도 않는다.

## 로봇 연구자가 바로 검증할 것

데이터셋은 `LeRobotDataset`으로 episode 일부만 불러오거나 streaming 방식으로 다룰 수 있다. 전체가 단일 train split이므로, **episode·task·물체 조합 기준으로 별도 held-out split을 만들고**, 프레임 단위 무작위 분할에 따른 누수를 피해야 한다. Subtask가 활성화되는 경계와 실제 action 변화가 맞는지, 실패 episode에도 주석 품질이 유지되는지 확인하는 것이 우선이다.

실험 설계에서는 **task-level instruction만 학습한 정책**과 **시간 정렬된 subtask를 추가한 정책**을 같은 데이터 예산으로 비교해야 한다. 실행 중에는 subtask 전환 오류와 저수준 제어 실패를 따로 기록해야 어떤 계층이 성능을 바꾸는지 알 수 있다.

특히 수집 로봇이 하나이고 작업 비율이 불균형하므로, 접촉 작업이나 다른 로봇으로 일반화할 때는 **action dimension·좌표계·그리퍼 의미·카메라 구성**을 다시 맞춰야 한다. 이번 공개의 의의는 모델 점수 하나보다, **언어 단계와 물리적 행동을 시간축에서 연결한 대규모 공개 데이터·학습 경로**를 제공한다는 점이다.

## Sources

- [Scale AI 공식 발표 — FineART 데이터·모델 공개 (2026-10-29)](https://labs.scale.com/blog/fineart)
- [Hugging Face LeRobot — FineART 데이터 카드·필드·주석·사용법](https://huggingface.co/datasets/lerobot/FineART)
- [FineART 원 논문 — arXiv:2609.36416 (2026-09-29)](https://arxiv.org/abs/2609.36416)
- [FineART-VLA 공개 모델 카드](https://huggingface.co/lerobot/FineART-VLA-subtask-midtrained)
