---
layout: note
title: "LLM Agent는 그냥 LLM이 아니다 — Model, Tools, State, Loop로 이해하기"
date: 2026-09-21
library_type: concept
category: Concepts & Theory
category_ko: 개념 & 이론
category_en: Concepts & Theory
topic: Agent Systems
topic_ko: Agent Systems
topic_en: Agent Systems
summary: "LLM과 Agent의 차이를 Model, Tools, Runtime, State, Context, Loop의 관계로 정리하고 Planner와 Orchestrator까지 구분합니다."
source_language: ko
---

LLM을 사용한다고 해서 시스템이 자동으로 **Agent**가 되는 것은 아니다.

LLM은 기본적으로 입력된 context를 바탕으로 다음 출력을 생성하는 **model**이다. 반면 Agent는 이 model을 중심으로 외부 도구를 사용하고, 실행 결과를 다시 관찰하고, 상태를 갱신하면서 목표를 향해 반복적으로 움직이는 **system**에 가깝다.

개념적으로는 다음처럼 생각하면 이해하기 쉽다.

```text
LLM
= reasoning / decision model

Agent
≈ Model
+ Tools
+ Runtime
+ State
+ Loop
```

여기서 중요한 점은 **Agent와 LLM을 같은 것으로 생각하지 않는 것**이다.

---

## 1. LLM은 Agent의 한 구성요소다

LLM은 자연어를 이해하고, 계획을 세우고, 다음 행동을 선택하는 데 사용할 수 있다.

하지만 LLM 자체가 파일을 수정하거나, 웹사이트를 클릭하거나, 터미널 명령을 실행하는 것은 아니다.

실제 시스템에서는 보통 다음과 같은 구조가 필요하다.

```text
User
  ↓
Agent Runtime
  ↓
LLM
  ↓
Tool call request
  ↓
Agent Runtime
  ↓
Tool / API / Computer
  ↓
Result
  ↓
Agent Runtime
  ↓
LLM
```

즉 LLM이 “이 도구를 사용해야 한다”고 판단하면, **runtime 또는 harness**가 그 요청을 해석하고 권한을 확인한 뒤 실제 tool을 호출한다.

그래서 Agent를 이해할 때 model만 보는 것보다 **model 주변의 실행 환경**을 같이 보는 것이 중요하다.

---

## 2. Tools는 Agent가 환경에 개입하는 방법이다

LLM만 있다면 모델은 텍스트를 생성하는 데 그친다.

Agent에 tool이 연결되면 모델의 판단을 실제 행동으로 이어갈 수 있다.

예를 들어 coding agent라면 다음과 같은 tool을 가질 수 있다.

```text
read_file()
edit_file()
search_code()
run_test()
run_terminal()
git_diff()
```

Research agent라면 구성은 달라진다.

```text
search_web()
open_page()
read_document()
query_database()
```

중요한 것은 tool의 개수가 많다는 사실이 아니다.

**현재 목표와 상태를 보고 어떤 tool을 언제 사용할지 결정할 수 있는가**가 Agent다운 동작을 만든다.

---

## 3. 핵심은 Loop다

Agent를 단순한 “LLM + Tool”보다 더 잘 설명하는 요소가 **Loop**다.

대표적인 흐름은 다음과 같다.

```text
Goal
  ↓
Observe
  ↓
Reason / Plan
  ↓
Act
  ↓
Observe result
  ↓
Update state
  ↓
다음 행동 결정
  ↺
```

이를 단순한 pseudo code로 쓰면 다음과 비슷하다.

```python
while not finished:
    observation = observe()
    action = model.decide(observation)
    result = execute(action)
    update_state(result)
```

실제 시스템은 이것보다 훨씬 복잡할 수 있지만, 핵심 구조는 같다.

**행동 → 결과 획득 → 새로운 정보 반영 → 다시 판단**이 반복된다.

ReAct 역시 reasoning과 action을 번갈아 수행하면서 외부 환경에서 새로운 정보를 얻고 계획을 갱신하는 아이디어를 보여준다.

---

## 4. State와 Context는 같은 것이 아니다

처음에는 State와 Context를 비슷하게 생각하기 쉽지만 구분하는 편이 좋다.

### State

State는 **Agent 시스템이 현재 상황을 표현하고 있는 정보**다.

예를 들면 coding agent에서는 다음이 state의 일부가 될 수 있다.

```text
현재 branch
수정된 파일
테스트 성공/실패 상태
완료된 작업
남아 있는 작업
사용 가능한 권한
```

State는 시스템 내부 파일, 데이터베이스, memory, 실행 환경 등에 존재할 수 있다.

### Context

Context는 그중 **이번 LLM 호출에서 실제로 model에게 입력으로 전달된 정보**다.

예를 들어 다음과 같은 정보가 한 번의 context에 포함될 수 있다.

```text
┌─────────────────────────┐
│ System instructions     │
├─────────────────────────┤
│ User request            │
├─────────────────────────┤
│ Relevant source files   │
├─────────────────────────┤
│ Git diff                │
├─────────────────────────┤
│ Terminal output         │
├─────────────────────────┤
│ Previous tool results   │
└─────────────────────────┘
            ↓
           LLM
```

즉 모든 state를 매번 model에게 전부 넣는 것은 아니다.

Agent runtime은 필요한 정보를 찾아서 **현재 판단에 필요한 context를 구성**한다.

이 때문에 agent system에서는 model 성능뿐 아니라 **context engineering**도 중요해진다.

---

## 5. Context Window는 Context의 최대 작업 공간이다

Context window는 모델이 한 번의 추론 흐름에서 참고할 수 있는 token 범위다.

Repository 전체, 모든 terminal log, 전체 대화 기록을 항상 넣을 수는 없다.

그래서 agent는 보통 필요한 정보를 그때그때 가져온다.

```text
User request
    ↓
관련 파일 탐색
    ↓
필요한 부분 읽기
    ↓
Context에 추가
    ↓
LLM 판단
    ↓
정보가 부족한가?
    ↓ Yes
추가 탐색
    ↓
Context 갱신
    ↺
```

이 관점으로 보면 agent의 tool 사용은 행동만을 위한 것이 아니다.

**새로운 context를 획득하는 수단**이기도 하다.

---

## 6. Planner와 Orchestrator는 역할이 다르다

Agent를 공부할 때 자주 섞이는 개념이 Planner와 Orchestrator다.

### Planner

Planner는 **무엇을 해야 하는지**를 정한다.

```text
Goal
  ↓
Planner
  ↓
Task A
Task B
Task C
```

고수준 목표를 더 작은 작업으로 분해하거나 다음 행동을 결정한다.

### Orchestrator

Orchestrator는 **정해진 작업을 누구에게, 언제, 어떤 순서로 실행시킬지 관리**한다.

```text
Plan
  ↓
Orchestrator
  ├─ Worker A 실행
  ├─ Worker B 실행
  ├─ 결과 수집
  └─ 다음 단계 진행
```

두 역할을 하나의 LLM이 모두 수행할 수도 있고, 일부는 deterministic code가 담당할 수도 있다.

따라서 “Agent니까 모든 것을 LLM에게 맡긴다”는 구조가 항상 좋은 것은 아니다.

---

## 7. Workflow와 Agent도 구분할 필요가 있다

미리 정해진 순서를 그대로 실행하는 구조와, model이 실행 중 동적으로 다음 행동을 선택하는 구조는 다르다.

### Workflow

```text
A 실행
↓
B 실행
↓
C 실행
```

실행 경로가 대부분 미리 정의되어 있다.

### Agent

```text
현재 상황 확인
↓
다음 행동 판단
↓
Tool 실행
↓
결과 확인
↓
필요하면 다른 경로 선택
↺
```

Anthropic은 이 차이를 **predefined code path를 따르는 workflow**와 **LLM이 자신의 process와 tool usage를 동적으로 결정하는 agent**로 구분해 설명한다.

실제 시스템에서는 둘을 섞는 경우가 많다.

예측 가능한 부분은 code로 고정하고, 불확실성이 큰 부분에서만 LLM에게 판단을 맡길 수 있다.

---

## 8. 예시: Coding Agent가 버그를 고치는 과정

사용자가 다음과 같이 요청했다고 하자.

```text
"이 repository에서 데이터 로딩 버그를 고쳐줘."
```

LLM에게 이 한 문장만 주면 충분하지 않다.

Agent는 먼저 필요한 정보를 수집할 수 있다.

```text
1. repository 구조 확인
2. 관련 파일 검색
3. 오류 로그 확인
4. 관련 source와 test 읽기
5. LLM이 수정 방법 판단
6. 파일 수정
7. test 실행
8. 실패하면 결과를 context에 추가
9. 다시 수정
10. test가 통과하면 종료
```

여기서 LLM은 중요한 reasoning component지만, 전체 작업은 다음이 함께 만들어낸 결과다.

```text
Model
+ Repository context
+ File tools
+ Terminal
+ Tests
+ Runtime
+ State
+ Iterative loop
```

이 전체가 coding agent에 더 가깝다.

---

## 9. Agent가 항상 정답은 아니다

Agent는 유연하지만 비용도 있다.

Tool call이 반복되면 latency와 비용이 증가하고, 실행 경로가 동적으로 변하기 때문에 debugging과 evaluation도 어려워질 수 있다.

그래서 작업이 다음처럼 완전히 정형화되어 있다면 일반 program이나 workflow가 더 적합할 수 있다.

```text
입력 검증
→ 정해진 API 호출
→ 결과 변환
→ 저장
```

반대로 다음과 같은 상황에서는 agent 구조의 가치가 커진다.

- 필요한 subtask를 미리 모두 예측하기 어렵다.
- 중간 결과에 따라 다음 행동이 달라진다.
- 여러 tool 중 어떤 것을 사용할지 판단해야 한다.
- 실패 원인을 보고 다른 접근으로 recovery해야 한다.
- 실행 도중 새로운 정보를 탐색해야 한다.

핵심은 **LLM을 쓰는 것 자체가 아니라, model-driven decision making이 실제로 필요한가**다.

---

## 정리

| 개념 | 역할 |
| --- | --- |
| **LLM / Model** | 추론하고 다음 출력을 생성 |
| **Tool** | 외부 정보를 얻거나 실제 행동을 수행 |
| **Runtime / Harness** | model의 tool 요청을 실제 실행과 연결 |
| **State** | 시스템이 유지하는 현재 상황 |
| **Context** | 현재 LLM 호출에 실제로 전달되는 정보 |
| **Context Window** | 한 번의 추론에서 참고할 수 있는 token 범위 |
| **Planner** | 무엇을 해야 하는지 결정 |
| **Orchestrator** | 작업의 실행 순서와 주체를 관리 |
| **Loop** | 관찰 → 판단 → 행동 → 결과 반영을 반복 |
| **Agent** | 위 요소들을 묶어 목표를 달성하는 시스템 |

한 문장으로 줄이면 다음과 같다.

> **LLM은 Agent의 두뇌 역할을 할 수 있지만, Agent는 LLM보다 큰 시스템이다.**

Agent를 공부할 때는 model architecture만 보는 것보다 **tool, runtime, state, context, feedback loop가 어떻게 연결되는지**를 함께 보는 것이 더 중요하다.

## References

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Yao et al. — ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
