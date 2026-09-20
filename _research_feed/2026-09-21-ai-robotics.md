---
layout: feed_note
title: "Claude Code Projects가 폴더에서 ‘작업 조정자’로 바뀌고 있습니다"
date: 2026-09-21 02:55:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude Code의 새 Projects beta는 하나의 대화가 작업을 여러 cloud thread로 나눠 병렬 실행하고, 프로젝트의 파일·저장소·지침·memory를 공유하는 구조로 바뀌었습니다."
---

Claude Code의 **Projects가 단순한 프로젝트 폴더에서 작업을 나눠 맡기는 coordinator로 바뀌고 있습니다.**

하나의 대화에서 할 일을 설명하면 Claude가 작업을 여러 **parallel cloud thread**로 나누고, 사용자가 노트북을 닫아도 thread는 계속 실행됩니다.

각 thread는 프로젝트의 **files, repositories, instructions, memory**를 기반으로 시작합니다.


<!-- feed-figure:claude-projects -->
<figure class="paper-figure">
  <div class="paper-figure-frame">
    <div class="paper-figure-canvas">
      <svg viewBox="0 0 760 285" role="img" aria-label="Claude Code Projects의 coordinator와 parallel cloud threads 구조">
        <defs>
          <marker id="cfp1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <path d="M0,0 L8,4 L0,8 z" fill="#7d858c"></path>
          </marker>
        </defs>
        <text x="24" y="28" class="fig-kicker">CLAUDE CODE PROJECTS — BETA</text>

        <rect x="36" y="102" width="150" height="70" rx="3" class="fig-box"></rect>
        <text x="111" y="128" class="fig-label">User request</text>
        <text x="111" y="151" class="fig-small">one top-level conversation</text>

        <path d="M186 137 L278 137" class="fig-arrow" marker-end="url(#cfp1)"></path>

        <rect x="290" y="88" width="170" height="98" rx="3" class="fig-box-accent"></rect>
        <text x="375" y="119" class="fig-label">Coordinator</text>
        <text x="375" y="143" class="fig-small">decompose · assign · track</text>
        <text x="375" y="164" class="fig-small">shared project context</text>

        <path d="M460 118 L535 72" class="fig-arrow" marker-end="url(#cfp1)"></path>
        <path d="M460 137 L535 137" class="fig-arrow" marker-end="url(#cfp1)"></path>
        <path d="M460 156 L535 202" class="fig-arrow" marker-end="url(#cfp1)"></path>

        <rect x="548" y="45" width="164" height="54" rx="3" class="fig-box"></rect>
        <text x="630" y="67" class="fig-label">Cloud thread 1</text>
        <text x="630" y="86" class="fig-small">parallel task</text>

        <rect x="548" y="110" width="164" height="54" rx="3" class="fig-box"></rect>
        <text x="630" y="132" class="fig-label">Cloud thread 2</text>
        <text x="630" y="151" class="fig-small">parallel task</text>

        <rect x="548" y="175" width="164" height="54" rx="3" class="fig-box"></rect>
        <text x="630" y="197" class="fig-label">Cloud thread n</text>
        <text x="630" y="216" class="fig-small">parallel task</text>

        <text x="376" y="254" class="fig-small">Files · repositories · instructions · memory are shared at the project level.</text>
      </svg>
    </div>
  </div>
  <figcaption><strong>Figure 1.</strong> 새 Projects의 핵심 변화는 하나의 상위 대화가 여러 cloud thread를 조정하는 구조다. Source: <a href="https://support.claude.com/en/articles/9517075-what-are-projects">Anthropic Help Center</a>.</figcaption>
</figure>


현재 새 Projects는 Claude Code를 사용하는 일부 **Pro·Max 사용자에게 beta**로 먼저 배포되고 있습니다.

이 변화가 중요한 이유는 coding agent 사용 방식이 “한 채팅에 한 작업”에서 **하나의 상위 대화가 여러 장기 작업을 조정하는 구조**로 이동하고 있다는 점입니다.

직접 여러 agent session을 열고 context를 복사해 넘기던 작업을 제품 자체가 orchestration하기 시작한 셈입니다.

## Sources

- [Anthropic Help Center — What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [The Verge — Claude Code relaunches Projects to manage multiple AI agents in the cloud](https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects)
