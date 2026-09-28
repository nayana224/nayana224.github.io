---
layout: feed_note
title: "IROS 2026의 공통 질문이 바뀌고 있다 — VLA 다음은 verification·recovery·human-aware autonomy"
date: 2026-09-27 19:00:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "IROS 2026 첫날 워크숍들은 VLA의 action prediction 자체보다 불확실성 아래에서의 reasoning, verification, recovery, human interaction, long-horizon reliability를 전면에 놓았다. Embodied AI가 단일 policy 성능에서 closed-loop system architecture 문제로 이동하는 흐름을 보여준다."
---

## VLA가 행동을 만들 수 있다는 것과, 로봇이 오래 안정적으로 일한다는 것은 다른 문제다

**9월 27일 시작된 IROS 2026의 여러 workshop에서 공통적으로 드러난 주제는 VLA의 action prediction 이후 단계다.** ReS AI workshop은 data-driven perception·policy learning만으로는 실제 환경에서 task structure, physical constraint, safety requirement, incomplete information을 다루기 어렵다고 보고 neural learning과 symbolic reasoning의 결합을 다룬다.

Human-aware Embodied AI workshop도 비슷한 경계를 짚는다. LLM·MLLM·VLA가 navigation, object search, manipulation까지 확장됐지만, 실제 인간 환경에서는 uncertainty와 ambiguity를 계속 처리해야 한다. 이 때문에 human↔agent communication을 perception–reasoning–action cycle 안의 feedback mechanism으로 본다.

Full-Shift Robot Co-Workers workshop은 질문을 더 직접적으로 바꾼다. **“로봇이 한 번 성공할 수 있는가?”가 아니라 “8시간 동안 perceive → reason → act → recover → adapt를 반복할 수 있는가?”**를 다룬다. active perception, world model, uncertainty estimation, VLA, memory, monitoring, failure recovery가 하나의 long-horizon autonomy stack으로 묶인다.

이 흐름은 robot agent를 설계할 때 planner나 VLA 하나의 정확도만 보는 것이 부족하다는 점을 보여준다. 실제 closed-loop system에서는 observation freshness, execution prerequisite, outcome verification, recovery condition을 별도의 runtime concern으로 두는 구조가 중요해지고 있다.

## Sources
- [IROS 2026 — Embodied Neuro-Symbolic AI for Reliable and Safe Robotics](https://embodied-nesy.github.io/)
- [IROS 2026 — Human-aware Embodied AI](https://heai-iros26-workshop.github.io/)
- [IROS 2026 — Full-Shift Robot Co-Workers](https://chuchuchen.net/robotworker-26/)
- [IROS 2026 — Mobile Manipulation and Embodied Intelligence](https://mobile-manipulation.net/events/moma-iros26/)
