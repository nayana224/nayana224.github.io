---
layout: note
title: "Context와 Context Window는 무엇이 다른가 — Coding Agent를 예로 이해하기"
date: 2026-09-21
library_type: concept
category: Concepts & Theory
category_ko: 개념 & 이론
category_en: Concepts & Theory
topic: Agent Systems
topic_ko: Agent Systems
topic_en: Agent Systems
summary: "Agent가 State에서 필요한 정보를 골라 Context를 만들고, Context Window 안에서 LLM에게 전달하는 과정을 Coding Agent 예시로 정리합니다."
source_language: ko
---

<div class="note-callout note-callout-primary">
  <strong>핵심 요약</strong>
  <p><b>State</b>는 시스템이 알고 있는 전체 현재 상태, <b>Context</b>는 이번 LLM 호출에 실제 전달되는 정보, <b>Context Window</b>는 그 Context를 담을 수 있는 모델의 token 범위다.</p>
</div>

<div class="concept-grid">
  <div class="concept-card"><span class="concept-kicker">SYSTEM</span><h3>State</h3><p>시스템이 유지하는 현재 상황 전체</p></div>
  <div class="concept-card"><span class="concept-kicker">MODEL INPUT</span><h3>Context</h3><p>이번 추론에서 LLM에게 실제 보여주는 정보</p></div>
  <div class="concept-card"><span class="concept-kicker">CAPACITY</span><h3>Context Window</h3><p>한 추론 흐름에서 참고 가능한 token 범위</p></div>
  <div class="concept-card"><span class="concept-kicker">PROCESS</span><h3>Context Engineering</h3><p>필요한 정보를 선택·구성·갱신하는 과정</p></div>
</div>

이 세 개념은 서로 연결되어 있지만 같은 것은 아니다.

특히 coding agent를 보면 차이가 명확해진다.

---

## 1. State는 시스템이 알고 있는 전체 현재 상태다

예를 들어 coding agent가 repository를 수정하고 있다고 하자.

시스템은 다음과 같은 정보를 가지고 있을 수 있다.

<div class="hierarchy-block">
  <div class="hierarchy-level"><span class="hierarchy-label">REPOSITORY</span><strong>현재 branch와 파일 상태</strong><p>어떤 파일이 존재하고 무엇이 수정되었는가</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">EXECUTION</span><strong>Test / build 상태</strong><p>무엇이 성공했고 어디서 실패했는가</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">PROGRESS</span><strong>완료·미완료 작업</strong><p>어떤 단계까지 진행되었는가</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">ENVIRONMENT</span><strong>권한과 실행 환경</strong><p>어떤 tool과 자원에 접근할 수 있는가</p></div>
</div>

이 전체를 매번 LLM에게 그대로 보낼 필요는 없다.

State는 **system-level representation**이고, LLM 입력보다 넓은 개념이다.

---

## 2. Context는 이번 호출에서 실제로 보여주는 정보다

<div class="flow-diagram">
  <div class="flow-step">System / Repository State</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Relevant information selection</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Context 구성<small>instructions · request · files · logs · tool results</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">LLM</div>
</div>

예를 들어 사용자가 다음과 같이 요청했다고 하자.

> "이 repository에서 데이터 로딩 버그를 고쳐줘."

이 문장만 LLM에게 주면 충분하지 않을 수 있다.

Agent runtime은 판단에 필요한 정보를 추가로 모은다.

<div class="concept-grid">
  <div class="concept-card"><h3>Instructions</h3><p>코딩 규칙, API 유지 조건, 테스트 정책</p></div>
  <div class="concept-card"><h3>User Request</h3><p>현재 해결해야 할 목표</p></div>
  <div class="concept-card"><h3>Source Files</h3><p>관련 구현과 test 코드</p></div>
  <div class="concept-card"><h3>Execution Evidence</h3><p>Git diff, error log, 이전 tool 결과</p></div>
</div>

이렇게 선택된 정보 묶음이 현재 LLM 호출의 **Context**가 된다.

---

## 3. Context Window는 입력 정보의 최대 작업 공간이다

<div class="note-callout">
  <strong>Context Window ≠ Memory</strong>
  <p>Context Window는 모델이 학습 과정에서 기억한 지식 전체가 아니라, <b>현재 추론 흐름에서 참고할 수 있는 token 범위</b>다.</p>
</div>

Model weights와 context는 역할이 다르다.

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">TRAINING</span>
    <h3>Model Weights</h3>
    <p>학습을 통해 모델이 이미 갖게 된 일반적인 능력과 패턴.</p>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">INFERENCE</span>
    <h3>Context</h3>
    <p>지금 이 순간의 작업을 위해 호출 시점에 같이 전달되는 정보.</p>
  </div>
</div>

Context window가 크다고 해서 repository 전체를 무조건 넣는 것이 좋은 전략은 아니다.

불필요한 정보가 많아지면 중요한 정보가 묻히고, 비용과 latency도 늘어난다.

---

## 4. Agent는 Context를 한 번만 만들지 않는다

<div class="flow-diagram">
  <div class="flow-step">User Request</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">관련 파일 탐색</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">필요한 부분만 읽기</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">LLM 추론</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">추가 정보가 필요한가?</div>
  <div class="flow-loop">Yes → 다른 파일 / 로그 / tool result 획득 → Context 갱신 ↺</div>
</div>

Agent는 보통 **행동하면서 context를 갱신한다.**

즉 다음 루프가 반복된다.

<div class="pipeline-row">
  <div class="pipeline-node">Act</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">New Information</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Update Context</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Reason Again</div>
</div>

이 구조 때문에 tool은 단순한 실행 수단뿐 아니라 **정보 획득 수단**이 된다.

---

## 5. 왜 Context Engineering이 중요한가

Context engineering은 단순히 prompt를 예쁘게 쓰는 것보다 범위가 넓다.

핵심 질문은 다음과 같다.

<div class="hierarchy-block">
  <div class="hierarchy-level"><span class="hierarchy-label">SELECT</span><strong>무엇을 넣을 것인가?</strong><p>현재 판단에 실제로 필요한 정보 선택</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">ORDER</span><strong>어떤 구조로 전달할 것인가?</strong><p>instructions, evidence, history를 이해 가능한 형태로 구성</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">REMOVE</span><strong>무엇을 버릴 것인가?</strong><p>중복되거나 오래된 정보 제거</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">UPDATE</span><strong>언제 다시 가져올 것인가?</strong><p>tool 결과와 환경 변화에 맞춰 context 갱신</p></div>
</div>

좋은 model을 사용하더라도 잘못된 context를 주면 잘못된 판단을 할 수 있다.

반대로 필요한 source, error log, test 결과를 적절히 구성하면 같은 model도 훨씬 안정적으로 작업할 수 있다.

---

## 6. Context Compression은 왜 필요한가

대화와 tool 결과가 계속 쌓이면 context는 커진다.

따라서 장시간 동작하는 agent에서는 오래된 내용을 그대로 계속 유지하기보다 **요약, 압축, 재검색**하는 전략이 필요하다.

<div class="compare-grid">
  <div class="compare-card"><h3>Keep</h3><p>현재 목표, 중요한 결정, 핵심 오류, 변경된 파일</p></div>
  <div class="compare-card"><h3>Compress / Drop</h3><p>중복 로그, 이미 해결된 세부 과정, 반복된 tool output</p></div>
</div>

Context compression의 목적은 모든 과거 정보를 보존하는 것이 아니라, **다음 판단에 필요한 정보를 잃지 않으면서 token 사용을 줄이는 것**이다.

---

## 7. Coding Agent 관점에서 다시 보면

<div class="flow-diagram">
  <div class="flow-step">User Request<small>"데이터 로딩 버그를 고쳐줘"</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Repository 탐색</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Relevant Source + Test + Error Log</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Context 구성 → LLM 판단</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Edit / Test 실행</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">새 결과를 State와 Context에 반영</div>
  <div class="flow-loop">실패하면 추가 탐색 후 반복 ↺</div>
</div>

이 과정에서 repository 전체는 **State / Environment**에 존재하지만, 실제 LLM에게는 그 순간 필요한 일부만 **Context**로 전달된다.

---

## 정리

| 개념 | 한 문장으로 |
| --- | --- |
| **State** | 시스템이 현재 상황에 대해 유지하는 전체 정보 |
| **Context** | 현재 LLM 호출에 실제 입력으로 전달되는 정보 |
| **Context Window** | 한 추론 흐름에서 참고 가능한 token 범위 |
| **Context Engineering** | 필요한 정보를 선택·구성·갱신하는 과정 |
| **Context Compression** | 다음 판단에 필요한 핵심은 남기고 과거 정보를 압축하는 과정 |

<div class="note-callout note-callout-primary">
  <strong>핵심 관계</strong>
  <p><b>State → 필요한 정보 선택 → Context → Context Window 안에서 LLM 추론 → Tool 결과로 State/Context 갱신</b></p>
</div>

## References

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
