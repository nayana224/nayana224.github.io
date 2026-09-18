---
layout: feed_note
title: "AI & Robotics — VLA는 몸 전체로, Agent는 며칠씩 일하기 시작했습니다"
date: 2026-09-19 00:30:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Gemini Robotics 2, OpenAI Agents API, coding agent 연구 가속화까지. 최근 AI와 Robotics에서 실제 workflow가 어떻게 바뀌고 있는지 정리했습니다."
---

구글은 이제 로봇팔 하나가 아니라 **걷고, 집고, 협업하는 whole-body VLA**를 밀고 있습니다.

OpenAI는 반대로 agent를 한 번 답하고 끝나는 모델이 아니라 **며칠 동안 계속 작업하는 system**으로 확장하고 있습니다.

둘을 같이 보면 방향이 꽤 선명합니다.  
AI가 “잘 답하는 모델”에서 **실제로 오래 일하고, 몸을 움직이고, workflow를 대신 수행하는 agent**로 넘어가고 있습니다.

## 1/ Gemini Robotics 2 — VLA가 whole-body control로 넓어졌습니다

Google DeepMind의 Gemini Robotics 2는 기존 tabletop manipulation을 넘어 **whole-body control, dexterous manipulation, multi-robot collaboration**까지 범위를 넓혔습니다.

이제 VLA를 볼 때 arm trajectory만 보면 부족합니다.

walking, manipulation, reasoning, embodiment adaptation이 한 stack 안에서 어떻게 연결되는지가 더 중요해지고 있습니다.

특히 humanoid나 mobile manipulator처럼 몸 전체를 써야 하는 robot에서는 이 변화가 더 크게 느껴질 수 있습니다.

## 2/ OpenAI Agents API — agent가 “오래 실행되는 작업 단위”가 되고 있습니다

OpenAI는 Agents API를 공개하면서 context 관리, tool use, subagent coordination, long-running execution을 하나의 infrastructure로 묶었습니다.

핵심은 단순합니다.

이제 agent는 한 번 질문하고 한 번 답하는 구조보다,  
**file을 읽고, code를 수정하고, intermediate result를 저장하면서 오래 작업하는 system**으로 설계되고 있습니다.

개인 연구 workflow도 결국 같은 방향으로 갈 가능성이 큽니다.

paper reading → implementation → experiment → result organization → documentation까지 하나의 loop로 이어지는 구조입니다.

## 3/ Coding agent는 이미 research loop 안으로 들어오고 있습니다

OpenAI가 공개한 내부 연구 사례를 보면 coding agent는 code completion 수준을 넘어 experiment 작성, analysis, infrastructure troubleshooting까지 맡기 시작했습니다.

중요한 건 “코드를 더 빨리 짠다”가 아닙니다.

연구자가 동시에 더 많은 experiment를 돌리고, iteration cycle 자체를 줄일 수 있다는 점입니다.

AI researcher에게 agent는 점점 **개발 보조도구가 아니라 research operator**에 가까워지고 있습니다.

## 지금 봐야 할 포인트

최근 흐름을 세 줄로 줄이면 이렇습니다.

- Robotics는 **whole-body intelligence**로 확장
- Agent는 **long-running workflow**로 확장
- Research는 **human + agent loop**로 재구성

앞으로 VLM/VLA를 공부할 때 model architecture만 보는 것보다,  
**reasoning → action → system integration → long-running agent workflow**까지 같이 보는 게 더 중요해질 것 같습니다.

## Sources

- [Google DeepMind — Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)
- [OpenAI — Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/)
- [OpenAI — Research acceleration: The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)
