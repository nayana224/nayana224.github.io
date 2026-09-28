---
layout: feed_note
title: "Agent가 웹페이지를 읽고 클릭하는 대신 tool을 호출한다 — Shopify가 WebMCP를 checkout까지 확장했다"
date: 2026-09-28 19:00:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Shopify가 WebMCP 지원을 checkout까지 확장하면서 browser agent가 DOM을 해석하고 클릭을 흉내 내는 대신 구조화된 tool interface로 구매 흐름을 다룰 수 있게 했다. 같은 날 IROS에서는 3D-aware VLA와 language-enabled multi-robot planning 등 physical agent의 grounding 문제도 전면에 등장했다."
---

## 웹을 GUI가 아니라 agent-callable tool surface로 만든다

**Shopify가 9월 28일 WebMCP 지원을 checkout까지 확장했다.** 기존 storefront WebMCP는 browser agent가 catalog를 검색하고 cart를 관리할 수 있게 했는데, 이번 변화로 checkout 화면의 정보를 읽고 수정하며 사용자의 authorization 아래 주문 제출 단계까지 이어지는 구조가 추가됐다.

WebMCP의 핵심은 agent가 매번 HTML/DOM을 읽고 버튼 위치를 추론해 click을 simulation하는 대신, 웹페이지가 browser에 **structured tool interface**를 등록한다는 점이다. Shopify 문서에서도 기존 GUI 조작 방식이 느리고 오류에 취약하다는 문제를 명시하고 있다.

agent architecture 관점에서는 computer use가 모두 vision-based GUI control로 갈 필요가 없다는 사례다. 웹 애플리케이션이 agent-facing capability를 직접 노출하면 perception uncertainty를 줄이고, 입력 schema와 authorization boundary를 더 명시적으로 설계할 수 있다. 반대로 purchase처럼 side effect가 큰 tool은 authentication, user confirmation, idempotency, escalation boundary가 함께 설계되어야 한다.

---

## IROS에서는 VLA에 3D grounding을 다시 넣는 방향도 등장했다

IROS 2026의 9월 28일 프로그램에는 **OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model**이 포함됐다. Georgia Tech가 공개한 설명에 따르면 VLA의 generalization과 3D-aware policy의 robustness를 결합하는 것이 목표다.

같은 날 프로그램에는 language-enabled heterogeneous multi-robot task planning, object-centric imitation-learning representation, whole-body control 등도 함께 배치됐다. VLA를 포함한 learned policy가 커지는 동시에, 실제 robot system에서는 spatial grounding·planning·control representation을 어떻게 결합할지가 여전히 독립적인 핵심 문제라는 점을 보여준다.

## Sources
- [Shopify Developer Changelog — September 2026](https://shopify.dev/changelog)
- [Shopify — WebMCP tools](https://shopify.dev/docs/api/web-mcp)
- [Shopify — Checkout MCP](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp)
- [Georgia Tech Robotics — GT @ IROS 2026](https://robotics.gatech.edu/gt-iros-2026)
