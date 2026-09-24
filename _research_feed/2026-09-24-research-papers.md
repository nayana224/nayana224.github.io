---
layout: feed_note
title: "Coding agent가 robot task를 풀고, 그 해법을 VLA 데이터로 바꾼다"
date: 2026-09-24 17:57:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "EmbodiedSWE는 coding agent가 long-horizon dexterous robotics task를 직접 해결하고, 검증된 solution을 대규모 trajectory로 확장해 VLA supervision으로 재사용하는 pipeline을 제안한다."
---

**EmbodiedSWE는 coding agent를 단순 robot planner가 아니라 `task solver → verified demonstration generator → VLA teacher`로 사용한다.** 새 EMBODIEDSWE-BENCH는 assembly, deformable object, liquid, cutting, loco-manipulation을 포함한 **6 suites·28 tasks·17 robot embodiments**를 제공하며, 일부 task는 약 **30분 horizon**까지 이어진다.

핵심은 coding agent가 simulator 안에서 자연어 목표를 받고 직접 solution code를 반복 작성한다는 점이다. task-specific macro primitive는 제공하지 않고 scene inspection과 IK 같은 generic controller를 이용하며, 결과는 hidden rubric으로 offline grading한다. 즉 high-level LLM이 미리 준비된 primitive 몇 개를 고르는 구조보다 한 단계 더 나아가, agent가 interaction을 통해 task-specific controller를 만들어 검증받는 setting이다.

하지만 agent solution 자체는 느리고 task-specific하다. EmbodiedSWE-Gen은 여기서 방향을 바꾼다. **한 번 검증된 solution을 scene·strategy·phase·dynamics·visual level에서 다양화해 robot trajectory dataset으로 확장**하고, 이를 VLA supervision으로 사용한다. 공개 project 결과에서 SmolVLA의 평균 success rate는 task당 demonstration을 **10개에서 400개로 늘릴 때 14% → 66%**로 상승했다. 동일한 1,000 demonstrations 비교에서도 agent-aided diversification은 held-out variation 평균 score를 **0.07 → 0.23**으로 높였다.

이 구조가 흥미로운 이유는 `LLM/coding agent`와 `VLA`의 역할을 경쟁 관계로 두지 않는다는 데 있다. 느리지만 reasoning과 tool use가 가능한 agent가 simulation에서 solution을 찾고 검증한 뒤, 그 결과를 빠른 learned policy의 training data로 넘긴다. **high-level agent의 deliberation을 real-time robot control loop에 그대로 넣지 않고 policy learning으로 distill하는 방식**으로 볼 수 있다.

다만 benchmark 결과를 곧바로 real-world autonomy 성능으로 해석하면 안 된다. 주된 agent evaluation과 data generation은 simulation에서 이뤄지며, coding-agent solve에는 상당한 iterative interaction과 시간이 필요하다. 프로젝트는 coding-agent-generated simulation demonstration만으로 fine-tune한 VLA의 real-robot long-horizon transfer 사례도 제시하지만, 이것만으로 광범위한 sim-to-real generalization이 검증됐다고 보기는 이르다.

### Sources

- [EmbodiedSWE — project page](https://embodiedswe.github.io/)
- [arXiv — EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308)
