---
layout: feed_note
title: "Claude Code Projects가 폴더에서 ‘작업 조정자’로 바뀌고 있습니다"
date: 2026-09-21 02:50:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude Code의 새 Projects beta는 하나의 대화가 작업을 여러 cloud thread로 나눠 병렬 실행하고, 프로젝트의 파일·저장소·지침·memory를 공유하는 구조로 바뀌었습니다."
---

Claude Code의 **Projects가 단순한 프로젝트 폴더에서 작업을 나눠 맡기는 coordinator로 바뀌고 있습니다.**

하나의 대화에서 할 일을 설명하면 Claude가 작업을 여러 **parallel cloud thread**로 나누고, 사용자가 노트북을 닫아도 thread는 계속 실행됩니다.

각 thread는 프로젝트의 **files, repositories, instructions, memory**를 기반으로 시작합니다.

현재 새 Projects는 Claude Code를 사용하는 일부 **Pro·Max 사용자에게 beta**로 먼저 배포되고 있습니다.

이 변화가 중요한 이유는 coding agent 사용 방식이 “한 채팅에 한 작업”에서 **하나의 상위 대화가 여러 장기 작업을 조정하는 구조**로 이동하고 있다는 점입니다.

직접 여러 agent session을 열고 context를 복사해 넘기던 작업을 제품 자체가 orchestration하기 시작한 셈입니다.

## Sources

- [Anthropic Help Center — What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [The Verge — Claude Code relaunches Projects to manage multiple AI agents in the cloud](https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects)
