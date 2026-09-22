---
layout: feed_note
title: "AI 연구는 agent scale로, Physical AI는 full-stack safety로 이동하고 있습니다"
date: 2026-09-21 23:40:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Anthropic의 대규모 AI R&D agent 운영, OpenAI의 automated-research·RSI 측정 기준, 그리고 NVIDIA가 공개한 Physical AI full-stack safety architecture를 묶어 봅니다."
---

**1/ Anthropic은 Claude가 내부 AI R&D의 26%를 이미 ‘lead’한다고 측정했습니다.**

Anthropic의 **R&D Automation Index**에 따르면, 2026년 8월 기준 Claude가 내부 AI R&D 업무의 **26%를 AL4(“AI leads”) 수준으로 수행**하고 있습니다. AL3 이상, 즉 AI가 최소한 사람과 협업하며 큰 작업 단위를 처리하는 비율은 **90% 이상**입니다. 아직 AL5의 완전 자율 수행으로 분류된 영역은 없습니다.

규모도 눈에 띕니다. Anthropic의 가장 많이 쓰이는 내부 플랫폼에서는 research·engineering 업무를 수행하는 agent가 **동시에 약 30,000개** 동작하며, 8월 한 달 동안 이 agent들의 **10억 건이 넘는 action decision**을 분석했다고 밝혔습니다.

모든 action은 실행 전 online monitor를 거치며, 약 **0.002% — 47,000건 중 1건꼴 — 가 차단**됐습니다.

agent를 실제 조직 규모로 운영할 때 문제는 이제 “agent가 일을 할 수 있는가”만이 아닙니다. **수만 개 agent의 identity, action trace, monitoring, escalation을 어떻게 관측 가능하게 만들 것인가**가 별도의 systems problem으로 커지고 있습니다.

**2/ OpenAI는 automated AI research와 RSI를 ‘측정하고 보고해야 할 대상’으로 명시했습니다.**

OpenAI는 9월 21일 공개한 제안에서 frontier AI의 국제 technical standards에 **recursive self-improvement(RSI)**를 포함해야 한다고 밝혔습니다. 여기서 RSI는 AI가 다음 세대 AI 연구의 더 많은 부분을 맡으면서 연구 속도 자체를 끌어올리는 과정입니다.

중요한 건 단순한 정책 문구보다 제안된 **measurement layer**입니다. OpenAI는 공통 기준의 예로 **RSI-relevant AI progress와 회사 내부 autonomous research 비율 측정**, automated AI research에 대한 **human oversight trigger**, 그리고 alignment·automated-research 사고의 **severity level과 reporting threshold**를 제시했습니다.

동시에 OpenAI는 **fully autonomous RSI는 현재 일어나고 있지 않으며**, 안전성과 human control이 확보되기 전에는 추진해서는 안 된다고 명시했습니다.

Anthropic이 실제 내부 R&D에서 AI가 맡는 비율을 계량하기 시작한 것과 연결해서 보면 흐름이 선명합니다. **AI가 AI를 만드는 정도를 capability demo가 아니라 운영 지표로 측정하고, 일정 수준을 넘으면 review·incident reporting으로 연결하는 체계**가 하나의 engineering problem으로 부상하고 있습니다.

**3/ NVIDIA는 Physical AI safety를 robot model 하나가 아니라 전체 stack의 문제로 정의했습니다.**

NVIDIA가 9월 21일 공개한 **Halos** 설명에서 robotics safety stack을 구체적으로 펼쳤습니다. **IGX Thor + Halos Core**가 compute와 fault detection·monitoring을 맡고, **Holoscan Sensor Bridge**가 sensor data와 safety processing을 연결하며, **Isaac Lab + Omniverse**가 simulation·edge-case validation을 담당합니다. 여기에 외부 camera와 vision AI agent로 작업 공간을 감시하는 **Outside-In Safety Blueprint**도 포함됩니다.

핵심 변화는 safety를 policy의 마지막 guardrail로 붙이는 방식이 아니라 **hardware → runtime/software → sensing → simulation/validation → facility-level monitoring**에 걸친 lifecycle 문제로 다룬다는 점입니다. 모델이나 task가 업데이트되면 material change에 맞춰 safety testing도 다시 수행해야 한다는 전제입니다.

실제 deployment도 이 stack과 연결되고 있습니다. NVIDIA는 Agility Robotics가 **Digit 5**의 safety system에 IGX Thor와 Halos Core를 통합하고 있으며, Einride를 포함한 autonomous-vehicle 업체들은 Hyperion 기반 Level 4-ready platform을 구축하고 있다고 밝혔습니다.

Robot Learning 관점에서는 policy 성능만큼 중요한 질문이 하나 더 생깁니다. **학습된 policy가 실패해도 독립적인 sensing·runtime·facility layer가 안전 경계를 유지할 수 있는가?** Physical AI가 demo에서 실제 deployment로 넘어갈수록 이 separation이 시스템 설계의 핵심이 될 가능성이 큽니다.

## Sources

- [Anthropic — Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development)
- [OpenAI — Building standards for the next phase of AI](https://openai.com/index/building-standards-next-phase-ai/)
- [NVIDIA — Why Deploying Physical AI at Scale Demands Safety at Every Layer](https://blogs.nvidia.com/blog/physical-ai-halos-safety/)
- [NVIDIA — Halos Outside-In Safety Blueprint](https://github.com/NVIDIA-Holoscan/halos-outside-in-safety)
