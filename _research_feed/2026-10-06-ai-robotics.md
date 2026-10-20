---
layout: feed_note
title: "AI agent의 Computer Use, 계약 업무 평가로 확장"
date: 2026-10-06 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "OpenAI가 Ironclad와 협력해 복잡한 계약 업무를 컴퓨터 사용 에이전트의 학습·평가 문제로 전환한다."
---

## 복잡한 업무를 ‘화면 클릭’이 아니라 검증 가능한 작업으로

OpenAI는 Ironclad와 협력해 전문 계약 소프트웨어에서 AI agent의 computer use를 학습하고 평가한다고 10월 6일 공개했다. 단순한 웹 조작 데모를 넘어, 회사별 업무 규칙을 이해하고 여러 단계를 실행한 뒤 **원래 요구사항을 만족했는지 검증**하는 작업이 핵심이다.

이는 로봇 에이전트에도 참고할 만하다. LLM planner가 행동을 제안하는 것과 실제 실행 결과가 목표 조건을 충족했는지를 확인하는 것은 별개의 문제이기 때문이다. 다만 발표는 연구 협력의 방향을 설명한 것이며, 범용 성공률이나 배포 성능을 입증한 결과로 해석해서는 안 된다.

## 로봇 평가로 옮길 때 필요한 대응물

계약 업무에서 요구사항을 충족했는지 확인하듯, 조작 agent에도 task 완료 조건을 실행 가능한 predicate로 둬야 한다. 예컨대 물체가 목표 영역에 놓였는지뿐 아니라 안정적으로 놓였는지, 그리퍼가 해제됐는지, 다음 동작의 전제조건이 성립하는지를 센서로 확인한다.

이 접근의 핵심은 성공률 숫자가 아니라 업무 규칙과 검증 가능한 결과를 평가에 포함하려는 연구 방향이다. 발표는 협력 계획을 설명할 뿐 실험 표본, 독립 benchmark, 계약 agent의 일반 성능을 공개하지 않았다.

## Sources
- [OpenAI — Advancing computer use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad/)
