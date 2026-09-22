---
layout: feed_note
title: "Coding agent는 병렬화되고, AI 연구 자동화에는 RSI 기준이 붙기 시작했습니다"
date: 2026-09-21 22:20:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude Code Projects의 parallel cloud threads, Anthropic 내부 AI R&D의 대규모 agent 운영, 그리고 OpenAI가 제안한 automated AI research·RSI 측정 및 incident reporting 기준을 묶어 봅니다."
---

**1/ Claude Code Projects가 하나의 대화에서 여러 작업을 병렬로 조정하기 시작했습니다.**

새 Projects에서는 상위 대화가 일을 여러 **parallel cloud thread**로 나누고, 사용자가 노트북을 닫아도 thread가 계속 실행됩니다.

각 thread는 프로젝트의 **files, repositories, instructions, memory**를 공유합니다.

<figure class="paper-figure">
  <div class="paper-figure-frame">
    <div class="paper-figure-canvas">
      <svg viewBox="0 0 760 285" role="img" aria-label="Claude Code Projects의 coordinator와 parallel cloud threads 구조">
        <defs><marker id="cfp1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#7d858c"></path></marker></defs>
        <text x="24" y="28" class="fig-kicker">CLAUDE CODE PROJECTS — BETA</text>
        <rect x="36" y="102" width="150" height="70" rx="3" class="fig-box"></rect><text x="111" y="128" class="fig-label">User request</text><text x="111" y="151" class="fig-small">one top-level conversation</text>
        <path d="M186 137 L278 137" class="fig-arrow" marker-end="url(#cfp1)"></path>
        <rect x="290" y="88" width="170" height="98" rx="3" class="fig-box-accent"></rect><text x="375" y="119" class="fig-label">Coordinator</text><text x="375" y="143" class="fig-small">decompose · assign · track</text><text x="375" y="164" class="fig-small">shared project context</text>
        <path d="M460 118 L535 72" class="fig-arrow" marker-end="url(#cfp1)"></path><path d="M460 137 L535 137" class="fig-arrow" marker-end="url(#cfp1)"></path><path d="M460 156 L535 202" class="fig-arrow" marker-end="url(#cfp1)"></path>
        <rect x="548" y="45" width="164" height="54" rx="3" class="fig-box"></rect><text x="630" y="67" class="fig-label">Cloud thread 1</text><text x="630" y="86" class="fig-small">parallel task</text>
        <rect x="548" y="110" width="164" height="54" rx="3" class="fig-box"></rect><text x="630" y="132" class="fig-label">Cloud thread 2</text><text x="630" y="151" class="fig-small">parallel task</text>
        <rect x="548" y="175" width="164" height="54" rx="3" class="fig-box"></rect><text x="630" y="197" class="fig-label">Cloud thread n</text><text x="630" y="216" class="fig-small">parallel task</text>
        <text x="376" y="254" class="fig-small">Files · repositories · instructions · memory are shared at the project level.</text>
      </svg>
    </div>
  </div>
  <figcaption><strong>Figure 1.</strong> 하나의 상위 대화가 여러 cloud thread를 조정하는 구조. Source: <a href="https://support.claude.com/en/articles/9517075-what-are-projects">Anthropic Help Center</a>.</figcaption>
</figure>

현재 새 Projects는 Claude Code를 사용하는 일부 **Pro·Max 사용자에게 beta**로 먼저 배포되고 있습니다.

coding agent의 단위가 “한 채팅에 한 작업”에서 **상위 coordinator가 여러 장기 작업을 관리하는 구조**로 이동하고 있다는 점이 핵심입니다.

**2/ Anthropic은 Claude가 내부 AI R&D의 26%를 이미 ‘lead’한다고 측정했습니다.**

Anthropic의 **R&D Automation Index**에 따르면, 2026년 8월 기준 Claude가 내부 AI R&D 업무의 **26%를 AL4(“AI leads”) 수준으로 수행**하고 있습니다. AL3 이상, 즉 AI가 최소한 사람과 협업하며 큰 작업 단위를 처리하는 비율은 **90% 이상**입니다. 아직 AL5의 완전 자율 수행으로 분류된 영역은 없습니다.

규모도 눈에 띕니다. Anthropic의 가장 많이 쓰이는 내부 플랫폼에서는 research·engineering 업무를 수행하는 agent가 **동시에 약 30,000개** 동작하며, 8월 한 달 동안 이 agent들의 **10억 건이 넘는 action decision**을 분석했다고 밝혔습니다.

모든 action은 실행 전 online monitor를 거치며, 약 **0.002% — 47,000건 중 1건꼴 — 가 차단**됐습니다.

agent를 실제 조직 규모로 운영할 때 문제는 이제 “agent가 일을 할 수 있는가”만이 아닙니다. **수만 개 agent의 identity, action trace, monitoring, escalation을 어떻게 관측 가능하게 만들 것인가**가 별도의 systems problem으로 커지고 있습니다.

**3/ OpenAI는 automated AI research와 RSI를 ‘측정하고 보고해야 할 대상’으로 명시했습니다.**

OpenAI는 9월 21일 공개한 제안에서 frontier AI의 국제 technical standards에 **recursive self-improvement(RSI)**를 포함해야 한다고 밝혔습니다. 여기서 RSI는 AI가 다음 세대 AI 연구의 더 많은 부분을 맡으면서 연구 속도 자체를 끌어올리는 과정입니다.

중요한 건 단순한 정책 문구보다 제안된 **measurement layer**입니다. OpenAI는 공통 기준의 예로 **RSI-relevant AI progress와 회사 내부 autonomous research 비율 측정**, automated AI research에 대한 **human oversight trigger**, 그리고 alignment·automated-research 사고의 **severity level과 reporting threshold**를 제시했습니다.

동시에 OpenAI는 **fully autonomous RSI는 현재 일어나고 있지 않으며**, 안전성과 human control이 확보되기 전에는 추진해서는 안 된다고 명시했습니다.

Anthropic이 실제 내부 R&D에서 AI가 맡는 비율을 계량하기 시작한 것과 연결해서 보면 흐름이 선명합니다. **AI가 AI를 만드는 정도를 capability demo가 아니라 운영 지표로 측정하고, 일정 수준을 넘으면 review·incident reporting으로 연결하는 체계**가 하나의 engineering problem으로 부상하고 있습니다.

## Sources

- [Anthropic Help Center — What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Anthropic — Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development)
- [OpenAI — Building standards for the next phase of AI](https://openai.com/index/building-standards-next-phase-ai/)
