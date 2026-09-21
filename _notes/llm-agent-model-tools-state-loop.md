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

<div class="note-callout note-callout-primary">
  <strong>핵심 요약</strong>
  <p>LLM은 추론을 담당하는 <b>model</b>이고, Agent는 그 model을 <b>tools, runtime, state, context, loop</b>와 연결해 목표를 수행하는 <b>system</b>이다.</p>
</div>

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">MODEL</span>
    <h3>LLM</h3>
    <ul>
      <li>입력된 context를 바탕으로 추론</li>
      <li>다음 출력 또는 tool call을 제안</li>
      <li>그 자체가 외부 행동을 실행하는 것은 아님</li>
    </ul>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">SYSTEM</span>
    <h3>Agent</h3>
    <ul>
      <li>Model + Tools + Runtime + State + Loop</li>
      <li>환경에서 정보를 얻고 실제 행동 수행</li>
      <li>실행 결과를 반영하며 목표를 향해 반복</li>
    </ul>
  </div>
</div>

LLM을 사용한다고 해서 시스템이 자동으로 **Agent**가 되는 것은 아니다.

Agent를 이해할 때 핵심은 model 자체보다 **model이 어떤 실행 환경과 연결되어 있는가**를 함께 보는 것이다.

---


<!-- paper-figure:agent-runtime -->
<figure class="paper-figure">
 <div class="paper-figure-frame"><div class="paper-figure-canvas">
 <svg viewBox="0 0 760 330" role="img" aria-label="LLM Agent runtime system diagram">
  <defs><marker id="agA" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#7d858c"/></marker></defs>
  <text x="24" y="28" class="fig-kicker">AGENT SYSTEM</text>
  <rect x="40" y="125" width="120" height="58" rx="3" class="fig-box"/><text x="100" y="154" class="fig-label">User Goal</text>
  <path d="M160 154 L225 154" class="fig-arrow" marker-end="url(#agA)"/>
  <rect x="238" y="90" width="180" height="128" rx="3" class="fig-box-accent"/>
  <text x="328" y="118" class="fig-label">Agent Runtime</text>
  <text x="328" y="148" class="fig-small">context · permissions · loop</text>
  <text x="328" y="176" class="fig-label">LLM</text>
  <text x="328" y="198" class="fig-small">reason / decide</text>
  <path d="M418 126 L520 78" class="fig-arrow" marker-end="url(#agA)"/>
  <path d="M418 154 L520 154" class="fig-arrow" marker-end="url(#agA)"/>
  <path d="M418 182 L520 230" class="fig-arrow" marker-end="url(#agA)"/>
  <rect x="534" y="50" width="150" height="54" rx="3" class="fig-box"/><text x="609" y="78" class="fig-label">Tools</text>
  <rect x="534" y="127" width="150" height="54" rx="3" class="fig-box"/><text x="609" y="155" class="fig-label">State</text>
  <rect x="534" y="204" width="150" height="54" rx="3" class="fig-box"/><text x="609" y="232" class="fig-label">Environment</text>
  <path d="M608 258 C608 304, 325 304, 325 218" class="fig-arrow-accent" marker-end="url(#agA)"/>
  <text x="462" y="302" class="fig-small">observe result → update context → reason again</text>
 </svg></div></div>
 <figcaption><strong>Figure 1.</strong> Agent는 LLM 하나가 아니라 runtime, tools, state, environment를 feedback loop로 연결한 system으로 보는 편이 정확하다.</figcaption>
</figure>

## 1. Agent를 구성하는 핵심 요소

<div class="concept-grid">
  <div class="concept-card"><span class="concept-kicker">01</span><h3>Model</h3><p>추론, 계획, 다음 행동 선택을 담당한다.</p></div>
  <div class="concept-card"><span class="concept-kicker">02</span><h3>Tools</h3><p>파일, 웹, API, 터미널 등 외부 환경과 상호작용한다.</p></div>
  <div class="concept-card"><span class="concept-kicker">03</span><h3>State</h3><p>현재 작업과 환경의 상태를 시스템이 유지한다.</p></div>
  <div class="concept-card"><span class="concept-kicker">04</span><h3>Loop</h3><p>관찰 → 판단 → 행동 → 결과 반영을 반복한다.</p></div>
</div>

여기에 실제 tool 실행을 연결하고 권한·환경을 관리하는 **Runtime / Harness**가 더해진다.

---

## 2. LLM이 Tool을 직접 실행하는 것은 아니다

<div class="flow-diagram">
  <div class="flow-step">User Request</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Agent Runtime<small>context 구성 · 권한 · 실행환경 관리</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">LLM<small>다음 행동 또는 tool call 결정</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Tool / API / Computer<small>실제 행동 수행</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Result / Observation</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Runtime가 결과를 Context에 반영</div>
  <div class="flow-loop">필요하면 다시 LLM을 호출하며 반복 ↺</div>
</div>

LLM이 “이 도구를 사용해야 한다”고 판단하면 runtime이 그 요청을 해석하고 실제 tool을 호출한다.

Coding agent라면 예를 들어 <code>read_file()</code>, <code>edit_file()</code>, <code>search_code()</code>, <code>run_test()</code>, <code>run_terminal()</code> 같은 tool을 가질 수 있다.

Research agent라면 <code>search_web()</code>, <code>open_page()</code>, <code>read_document()</code>, <code>query_database()</code>처럼 구성이 달라질 수 있다.

중요한 것은 tool의 개수가 아니라 **현재 목표에 맞는 tool을 선택하고, 결과를 다시 다음 판단에 반영할 수 있는가**다.

---

## 3. Agent의 핵심은 Loop다

<div class="pipeline-row">
  <div class="pipeline-node">Observe</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Reason / Plan</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Act</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Update State</div>
</div>

<p class="note-legend">결과가 충분하지 않으면 다시 Observe 단계로 돌아간다.</p>

실제 agent는 훨씬 복잡할 수 있지만, 기본 구조는 같다.

**행동 → 결과 획득 → 새로운 정보 반영 → 다시 판단**이 반복된다.

---

## 4. State와 Context는 다르다

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">SYSTEM MEMORY</span>
    <h3>State</h3>
    <p>시스템이 현재 상황을 표현하고 유지하는 전체 정보다.</p>
    <p><small>예: branch, 수정 파일, test 상태, 완료 작업, 권한</small></p>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">MODEL INPUT</span>
    <h3>Context</h3>
    <p>그중 이번 LLM 호출에 실제 입력으로 전달되는 정보다.</p>
    <p><small>예: user request, 관련 파일, diff, terminal output, tool result</small></p>
  </div>
</div>

즉 모든 state가 매번 model에게 들어가는 것은 아니다.

Agent runtime은 state와 외부 환경에서 필요한 정보를 골라 **현재 판단에 필요한 context를 구성**한다.

---

## 5. Context Window는 Context를 담을 수 있는 범위다

<div class="flow-diagram">
  <div class="flow-step">User Request</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">관련 정보 탐색<small>source files · logs · tool results</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Context 구성</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">LLM 추론</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">정보가 부족한가?</div>
  <div class="flow-loop">Yes → 추가 탐색 → Context 갱신 → 다시 추론 ↺</div>
</div>

Context window는 모델이 한 번의 추론 흐름에서 참고할 수 있는 token 범위다.

그래서 큰 repository 전체나 모든 terminal log를 무조건 한 번에 넣는 것보다 **필요한 정보를 찾아가며 context를 갱신하는 구조**가 중요하다.

이 관점에서 tool은 행동 수단이면서 동시에 **새로운 context를 획득하는 수단**이기도 하다.

---

## 6. Planner와 Orchestrator는 역할이 다르다

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">WHAT</span>
    <h3>Planner</h3>
    <p><b>무엇을 해야 하는가?</b>를 결정한다.</p>
    <p>고수준 목표를 task로 분해하거나 다음 행동을 선택한다.</p>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">HOW / WHEN</span>
    <h3>Orchestrator</h3>
    <p><b>누구에게 언제 실행시킬 것인가?</b>를 관리한다.</p>
    <p>작업 순서, worker 호출, 결과 수집을 조정한다.</p>
  </div>
</div>

<div class="hierarchy-block">
  <div class="hierarchy-level"><span class="hierarchy-label">Goal</span><strong>고수준 목표</strong><p>사용자가 원하는 최종 결과</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">Planner</span><strong>Task decomposition</strong><p>목표를 실행 가능한 작업으로 분해</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">Orchestrator</span><strong>Execution management</strong><p>정해진 작업을 순서대로 또는 병렬로 실행</p></div>
</div>

모든 단계를 LLM이 담당할 필요는 없다. 예측 가능한 부분은 deterministic code로 두고, 불확실성이 큰 부분만 LLM에게 맡기는 방식도 충분히 agentic할 수 있다.

---

## 7. Workflow와 Agent를 구분하자

<div class="compare-grid">
  <div class="compare-card"><span class="concept-kicker">PREDEFINED</span><h3>Workflow</h3><p>A → B → C처럼 실행 경로가 대부분 미리 정해져 있다.</p></div>
  <div class="compare-card"><span class="concept-kicker">DYNAMIC</span><h3>Agent</h3><p>실행 중 관찰 결과에 따라 model이 다음 행동과 tool 사용을 동적으로 선택한다.</p></div>
</div>

Anthropic은 이 차이를 **predefined code path를 따르는 workflow**와 **LLM이 process와 tool usage를 동적으로 결정하는 agent**로 구분한다.

실제 시스템은 둘을 섞는 경우가 많다.

---

## 8. 예시: Coding Agent가 버그를 고치는 과정

<div class="hierarchy-block">
  <div class="hierarchy-level"><span class="hierarchy-label">01</span><strong>Repository 구조 확인</strong><p>어디를 봐야 하는지 탐색한다.</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">02</span><strong>관련 source / test / error log 수집</strong><p>판단에 필요한 context를 구성한다.</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">03</span><strong>LLM이 수정 방법 판단</strong><p>어떤 파일을 어떻게 바꿀지 결정한다.</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">04</span><strong>파일 수정 + test 실행</strong><p>tool이 실제 행동을 수행한다.</p></div>
  <div class="hierarchy-level"><span class="hierarchy-label">05</span><strong>실패 결과를 다시 반영</strong><p>새 결과를 context에 추가하고 다시 추론한다.</p></div>
</div>

<div class="concept-grid">
  <div class="concept-card"><h3>Model</h3><p>reasoning</p></div>
  <div class="concept-card"><h3>Repository Context</h3><p>source · tests · logs</p></div>
  <div class="concept-card"><h3>Tools</h3><p>file · terminal · git</p></div>
  <div class="concept-card"><h3>Runtime + Loop</h3><p>execute · observe · retry</p></div>
</div>

---

## 9. Agent가 항상 정답은 아니다

<div class="note-callout">
  <strong>Agent를 쓰기 전에 볼 질문</strong>
  <p>이 문제에 정말 <b>model-driven decision making</b>이 필요한가?</p>
</div>

작업이 완전히 정형화되어 있다면 일반 program이나 workflow가 더 단순하고 안정적일 수 있다.

반대로 다음과 같은 상황에서는 agent 구조의 가치가 커진다.

- 필요한 subtask를 미리 모두 예측하기 어렵다.
- 중간 결과에 따라 다음 행동이 달라진다.
- 여러 tool 중 무엇을 사용할지 판단해야 한다.
- 실패 원인을 보고 다른 접근으로 recovery해야 한다.
- 실행 도중 새로운 정보를 탐색해야 한다.

---

## 정리

| 개념 | 역할 |
| --- | --- |
| **LLM / Model** | 추론하고 다음 출력을 생성 |
| **Tool** | 외부 정보를 얻거나 실제 행동을 수행 |
| **Runtime / Harness** | model의 요청을 실제 실행과 연결 |
| **State** | 시스템이 유지하는 현재 상황 |
| **Context** | 현재 LLM 호출에 실제 전달되는 정보 |
| **Context Window** | 한 번의 추론에서 참고할 수 있는 token 범위 |
| **Planner** | 무엇을 해야 하는지 결정 |
| **Orchestrator** | 작업 실행 순서와 주체를 관리 |
| **Loop** | 관찰 → 판단 → 행동 → 결과 반영을 반복 |
| **Agent** | 위 요소들을 묶어 목표를 달성하는 시스템 |

<div class="note-callout note-callout-primary">
  <strong>한 문장으로</strong>
  <p><b>LLM은 Agent의 두뇌 역할을 할 수 있지만, Agent는 LLM보다 큰 시스템이다.</b></p>
</div>

<section class="related-notes" aria-labelledby="related-notes-title">
  <h2 id="related-notes-title">Related Notes</h2>
  <div class="related-notes-list">
    <a class="related-note-link" href="/notes/context-context-window-agent/"><strong>Context와 Context Window는 무엇이 다른가</strong><span>Agent runtime이 state에서 context를 구성하고 갱신하는 과정을 더 자세히 보기.</span></a>
  </div>
</section>

## References

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Yao et al. — ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
