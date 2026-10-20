---
layout: feed_note
title: "27B 모델을 7.89GB로 줄인 Saluki, 도구 호출은 어떻게 남겼나"
date: 2026-10-12 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "Saluki는 Qwen3.8-27B를 2-bit IQ2-mix GGUF로 공개했다. 제작사 평가에서는 BFCL 도구 호출 점수가 원본보다 높았지만, 수학 성능과 실행 메모리는 따로 봐야 한다."
---

10월 8일 공개된 **Underdog Saluki 27B 1.0**은 Qwen3.8-27B를 기반으로 한 2-bit IQ2-mix 모델이다. 모델 파일은 7.89GB이며, 일반적인 llama.cpp 배포 형식을 사용한다.

Underdog은 자체 평가에서 BFCL v4 기반 120개 도구 호출 과제 중 Saluki가 88개, 같은 조건으로 실행한 Qwen3.8-27B가 84개를 통과했다고 보고했다. 별도의 병렬 호출 평가에서는 100개 중 각각 42개와 35개였다. 이는 특정 호출 과제에서의 결과이지, Saluki가 원본보다 전반적으로 우수하다는 뜻은 아니다.

같은 모델 카드의 다른 수치에서는 수학 벤치마크 점수가 원본보다 낮다. 평가도 제작사가 구성한 비교이므로 독립 재현으로 볼 수 없다. 또한 7.89GB는 가중치 파일 크기다. 컨텍스트와 KV cache를 포함한 실행 시 메모리 사용량을 뜻하지 않는다.

로컬 추론을 검토할 때는 **가중치 용량, 실제 peak memory, 도구 호출 형식 안정성, 작업별 품질**을 분리해 측정해야 한다.

## Sources
- [Underdog Saluki 27B 공식 모델 카드와 벤치마크 조건](https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0)
- [Underdog Saluki 공개 발표](https://underdog.ai/saluki)
