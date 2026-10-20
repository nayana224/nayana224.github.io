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

## 로컬 배포에서 메모리 예산을 다시 계산하기

7.89GB 파일은 모델 가중치의 저장 크기다. 실행 중에는 runtime buffer와 context에 따른 KV cache, batch concurrency가 추가되며, GPU offload 설정에 따라 host RAM과 VRAM의 분배도 달라진다. 실제 배포 적합성은 목표 context length와 동시 요청 수에서 peak memory를 측정해야 한다.

도구 호출 모델로 평가할 때는 구문상 JSON을 내는지뿐 아니라 schema 준수, 잘못된 인자 회복, 여러 도구를 잇는 성공률을 함께 시험해야 한다. 제작사 BFCL 차이는 공개된 120문항의 제한된 실험이며 독립 재현 전에는 후보 탐색 신호로 보는 편이 맞다.

## Sources
- [Underdog Saluki 27B 공식 모델 카드와 벤치마크 조건](https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0)
- [Underdog Saluki 공개 발표](https://underdog.ai/saluki)
