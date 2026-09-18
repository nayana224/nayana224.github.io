---
layout: feed_note
title: "AI & Robotics Update — Gemini Robotics 2, Agents API, Research Acceleration"
date: 2026-09-19 00:30:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "whole-body robotics, long-running cloud agents, coding-agent 기반 연구 가속화까지 최근 흐름을 세 가지로 정리."
---

**한 줄 핵심:** 최근 AI/Robotics의 공통 방향은 “모델을 더 똑똑하게 만드는 것”에서 한 단계 더 나아가, **더 긴 task를 수행하고 실제 workflow 안에서 계속 일하게 만드는 것**으로 이동하고 있다.

## 1. Gemini Robotics 2 — VLA가 whole-body control로 넓어졌다

Google DeepMind는 Gemini Robotics 2를 공개하면서 robot intelligence의 범위를 tabletop manipulation에서 **whole-body control, dexterous manipulation, multi-robot collaboration**으로 확장했다.

이번 발표의 핵심은 robot이 단순히 arm trajectory를 예측하는 수준이 아니라, walking과 manipulation을 함께 다루고 서로 다른 embodiment에서 동작하는 방향을 보여줬다는 점이다.

### Why it matters

VLA를 공부할 때 이제 perception → action만 보는 것으로는 부족하다.  
앞으로는 **high-level reasoning, whole-body control, embodiment adaptation**이 하나의 stack 안에서 어떻게 연결되는지가 더 중요해질 가능성이 크다.

## 2. OpenAI Agents API — agent를 “며칠 동안 돌아가는 system”으로 제공

OpenAI는 Agents API public beta를 공개했다. 핵심은 Codex 계열 harness와 infrastructure를 API로 제공해, **context 관리, tool use, subagent coordination, long-running execution**을 개발자가 직접 구축하지 않아도 되게 만든 것이다.

단발성 request-response보다, files와 code를 다루고 intermediate result를 저장하면서 오래 실행되는 agent workflow를 전제로 한다.

### Why it matters

LLM application의 단위가 “질문에 답하는 model call”에서 **오래 실행되는 작업 단위**로 바뀌고 있다는 신호다.

Research automation이나 개인 knowledge workflow도 결국 같은 방향으로 간다.

## 3. Coding agents가 실제 AI 연구 cycle을 바꾸고 있다

OpenAI는 내부 연구 조직의 agent 사용 데이터를 공개했다. 연구자들은 coding agent를 더 자주, 더 병렬적으로 사용하고 있고, agent에게 맡기는 task도 더 길고 복잡해지고 있다고 보고했다.

특히 experiment 작성, infrastructure troubleshooting, analysis 같은 연구 과정에 agent가 깊게 들어가면서 experiment iteration 자체가 빨라지고 있다는 점을 강조한다.

### Why it matters

AI researcher에게 agent는 이제 단순 code completion 도구가 아니라 **research loop 일부**가 되고 있다.

논문 읽기 → 구현 → experiment → 결과 정리 → 문서화까지 연결하는 workflow를 미리 설계해두는 것이 점점 더 중요해질 수 있다.

## Sources

- [Google DeepMind — Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)

- [OpenAI — Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/)

- [OpenAI — Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)
