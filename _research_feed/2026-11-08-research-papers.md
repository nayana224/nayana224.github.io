---
layout: feed_note
title: "Concertina: 별도 action expert 없이 4.46B VLM 안에서 연속 로봇 궤적을 생성한다"
date: 2026-11-08 06:55:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "11월 5일 공개된 Concertina는 연속 로봇 행동을 diffusion VLM의 hidden token으로 표현하고 공유 Transformer 안에서 시간 블록별로 복원한다. LIBERO 98.15%, LIBERO-Plus 85.9%를 보고했지만, 제시된 수치는 벤치마크 평가이며 실물 로봇 일반화를 증명하지 않는다."
---

VLA가 장면과 지시를 이해하는 VLM과 실제 궤적을 생성하는 별도 action expert로 나뉘어 있어야 할까? 2026년 11월 5일 공개된 *Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model*은 **연속 행동의 표현·시간적 결합·물리 좌표 감독을 공유 VLM backbone 안에서 처리**하는 Embodied Vision-Language Model(eVLM)을 제안한다.

이는 앞서 소개한 ELA의 *행동 라벨 없는 영상에서 latent action을 학습하는 문제*와 다르다. Concertina의 초점은 **이미 행동이 주어진 로봇 데이터로 VLM 자체가 연속 제어 궤적을 학습·생성하도록 만드는 아키텍처**다.

## 기존 VLA에서 무엇이 분리되는가

이산 action-token 방식은 연속 좌표를 구간으로 양자화한다. 인접 구간을 잘못 예측한 경우와 멀리 떨어진 구간을 잘못 예측한 경우가 토큰 수준에서는 같은 오분류가 될 수 있다. 반대로 π₀ 계열처럼 연속 좌표를 보존하는 VLA는 별도 action expert를 통해 궤적을 생성하는 경우가 많다. 연구진은 이 분리가 VLM의 시각·언어 추론과 행동 생성 사이의 표현 및 학습 경로를 제한한다고 본다. 다만 **모든 분리형 구조가 반드시 성능이 낮다는 결론은 아니다**.

Concertina는 BARD-VL 기반 diffusion VLM의 기존 masked block reconstruction 연산을 행동에도 적용한다. 시간 단계마다 D차원 행동 벡터 하나를 작은 encoder로 d차원 연속 latent token 하나로 옮기고, 공유 Transformer가 시각·언어·상태·행동 token을 함께 처리한다. decoder는 출력 hidden state를 다시 물리 행동 좌표로 변환한다.

## 데이터는 어떻게 흐르는가

입력은 카메라 관측, 언어 지시, proprioceptive state이며, 출력은 H단계 행동 궤적이다.

`관측·지시·상태 → multimodal prefix C → 공유 Transformer + H개 연속 action token → 좌표 decoder → H×D 행동 궤적`

수식으로는 각 시간 단계의 행동 `a_i ∈ R^D`를 `z_i = E(a_i) ∈ R^d`로 사상하고, 공유 Transformer의 행동 위치 출력 `h_i`를 `â_i = D(h_i) ∈ R^D`로 복원한다. encoder와 decoder는 시간 단계별로 독립 적용되므로 **시간에 걸친 행동 간 의존성은 공유 Transformer 내부에서 학습**된다.

전체 H단계는 순서가 있는 블록으로 나뉜다. 이전 블록에는 인과적(causal)으로 의존하고, 같은 블록 안의 여러 행동은 양방향으로 정보를 주고받으며 함께 복원한다. 학습 시 손상된 행동과 정답 행동을 함께 배치하되 attention visibility를 제한해 현재 블록의 정답이 예측 입력으로 누출되지 않도록 한다. 추론에서는 블록별로 행동을 복원하고 새 관측을 받아 재계획할 수 있다.

## 실험 결과와 검증 범위

논문이 보고한 평균 성공률은 **LIBERO 98.15%**, **10,030개 과제의 LIBERO-Plus 85.9%**다. CALVIN ABC–D에서는 평균 완료 chain length **4.142**를 보고한다. 이는 서로 다른 평가 프로토콜의 수치이므로 하나의 성공률로 합치면 안 된다.

4.46B 파라미터 모델에서 행동 입출력 projection이 차지하는 활성 파라미터 비중은 **0.21%**이며, 별도의 action-generator layer는 없다. 논문이 비교한 분리형 연속 VLA의 action expert 전용 용량은 16.5~35.1% 수준이다. 이 비교는 **모델의 구조적 파라미터 비율**이지 실제 추론 지연이나 GPU 메모리가 그 비율만큼 감소했다는 뜻이 아니다.

연구진은 Action Interface Audit으로 물리 좌표 오차의 일관성, 시간 단계 간 영향이 발생하는 레이어, 행동 전용 파라미터 비중을 분석했다. 시간 간 결합이 단순 encoder/decoder가 아니라 공유 backbone의 중·후반 레이어에서 나타난다는 것이 저자 측의 분석 결과다.

## 로봇 연구에서 어떻게 검증할까

이 연구의 실무적 질문은 **action expert를 제거했을 때 모델이 단순해지는 대신 제어 주기, 온라인 메모리, 재계획 지연은 어떻게 변하는가**다. 재현 시 동일한 관측·행동 표현과 학습 데이터로 별도 expert 방식과 비교하고, 성공률 외에도 action chunk 생성 시간, 재계획 주기, 접촉 실패 후 회복률을 함께 측정해야 한다.

또한 여러 로봇의 제어 차원을 공통 폭으로 맞추고 유효 차원 mask를 적용하는 설계는 cross-embodiment 데이터 처리에 참고할 만하다. 그러나 **시뮬레이션·벤치마크의 높은 점수만으로 실물 접촉 작업의 안정성, 힘 제어, Jetson 실시간 실행을 보장할 수 없다**. 실제 배포에서는 관측 지연, 로봇별 action normalization, 제어기 인터페이스와 안전 제한을 별도로 검증해야 한다.

## 부록: 배경지식

### Action expert

- **정의:** VLM이 추출한 정보를 받아 로봇의 연속 행동을 생성하는 별도 신경망 모듈이다.
- **예시(설명용):** 카메라와 언어를 해석하는 모델 뒤에 손목의 이동량과 그리퍼 명령을 예측하는 별도 네트워크를 연결한다.
- **이 글에서의 의미:** Concertina는 별도 action generator 대신 공유 diffusion VLM backbone이 직접 궤적의 시간적 관계를 학습한다.

### Continuous latent action token

- **정의:** 연속적인 다차원 로봇 행동을 신경망의 hidden space에 담은 벡터 표현이다.
- **예시(설명용):** 한 시점의 위치 변화·회전 변화·그리퍼 값을 하나의 벡터로 인코딩한다.
- **이 글에서의 의미:** Concertina는 제어 시간 단계마다 token 하나를 두어 H단계 궤적을 H개 token으로 표현한다.

### Blockwise diffusion reconstruction

- **정의:** 연속된 여러 token을 묶어 손상된 값을 반복적으로 복원하는 생성 방식이다.
- **예시(설명용):** 접근·그리퍼 닫기·들어 올리기에 해당하는 짧은 행동 묶음을 함께 수정하면서 다음 묶음으로 넘어간다.
- **이 글에서의 의미:** 블록 내부는 양방향으로 행동을 조정하고 블록 사이에는 시간 순서를 유지해 궤적을 생성한다.

### Proprioception

- **정의:** 로봇이 자신의 관절 위치·속도 등 내부 운동 상태를 측정하는 정보다.
- **예시(설명용):** 카메라에 손끝이 가려져도 엔코더로 현재 팔 관절각을 읽는다.
- **이 글에서의 의미:** 시각·언어와 함께 공유 모델의 조건 입력에 포함되어 행동 궤적 생성에 사용된다.

## Sources

- [Concertina 원문 — arXiv:2611.07513 (2026-11-05)](https://arxiv.org/abs/2611.07513)
- [논문 전체 HTML — 모델 구조, Action Interface Audit, 실험 및 Appendix](https://arxiv.org/html/2611.07513v1)
- [연구진 공식 프로젝트 — Concertina](https://concertina.traly.org/)
