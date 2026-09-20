---
layout: feed_note
title: "Coding agent가 이제 작업을 나누고, 엔진의 공식 지식까지 직접 받기 시작했습니다"
date: 2026-09-21 04:46:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude Code Projects는 여러 cloud thread를 조정하는 구조로 바뀌었고, Unity는 Codex에 31개의 first-party engineering skills와 Unity CLI를 제공하기 시작했습니다."
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

**2/ Unity는 Codex에게 31개의 first-party engineering skills를 직접 제공하기 시작했습니다.**

9월 16일 공개된 **Official Unity Plugin for Codex**는 UI Toolkit·uGUI, 2D·Tilemap, URP·Shader Graph, audio, navigation·physics, multiplayer, web, localization 등을 다루는 **31개 skills**를 포함합니다. Unity 6+가 대상입니다.

여기에 `unity-cli`가 함께 들어가 Codex가 terminal에서 Editor 설치, project 생성·열기, package 관리까지 수행할 수 있습니다. skills는 각 기능을 담당하는 Unity 팀이 직접 작성·유지합니다.

이건 coding agent의 정확도를 모델 자체만으로 끌어올리는 방식과 다릅니다. **도메인 제공자가 최신 API와 작업 규칙을 agent의 context/tool layer에 직접 공급하는 구조**가 제품화되고 있다는 신호에 가깝습니다.

오래된 forum·tutorial을 평균내 답하는 대신, engine vendor가 관리하는 instructions와 CLI를 agent에 붙이는 방식입니다. Unity는 앞서 Claude Code용 공식 plugin도 공개했고, 그 버전에는 29개 skills와 live Editor control을 위한 MCP server가 포함되어 있습니다.

## Sources

- [Anthropic Help Center — What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Unity — The Official Unity Plugin for Codex](https://unity.com/blog/unity-plugin-codex)
- [Unity — Official Unity Plugin for Claude Code](https://unity.com/blog/unity-plugin-for-claude-code)
