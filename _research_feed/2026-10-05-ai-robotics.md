---
layout: feed_note
title: "생성 AI 텍스트에 워터마크: 무엇을 증명하고 무엇을 못 하나"
date: 2026-10-05 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "OpenAI가 textGrain 텍스트 워터마킹 접근과 EU 적용 계획을 공개했다."
---

*당일 발표*

OpenAI는 10월 5일 **textGrain**을 이용한 텍스트 워터마킹과 탐지기 접근 계획을 설명했다. API 이용자에게는 일부 모델의 워터마킹을 opt-in으로 제공하고, EU의 적격 ChatGPT·Codex 출력에는 단계적으로 적용할 계획이라고 밝혔다.

워터마크는 통계적 신호이며 사용자의 신원, 문장의 정확성, 저작권 소유관계를 증명하지 않는다. 짧거나 편집·번역된 텍스트에서는 false positive/negative 문제가 남는다. AI agent의 로그·평가 보고서를 다룰 때 **provenance와 factual verification을 분리**해야 하는 이유다.

## 워터마크 판정이 허용하는 결론

통계적 워터마크 검출은 텍스트 생성 과정에 특정 패턴이 들어갔을 가능성을 추정하는 신호다. 문장을 사람이 많이 고치거나 번역하면 신호가 약해질 수 있고, 짧은 문장에서는 판정력이 낮아질 수 있다. 반대로 검출 결과만으로 작성자를 특정할 수도 없다.

연구 기록에서는 원본 생성 로그, 모델·버전, 편집 이력, 실험 데이터 출처를 함께 보존해야 provenance가 재현 가능해진다. textGrain 발표가 말하는 watermark는 이 기록 체계를 대체하지 않으며, factual correctness는 원자료와 별도로 확인해야 한다.

## Sources
- [OpenAI 공식 발표](https://openai.com/index/eu-text-provenance/)
