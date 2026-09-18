---
layout: feed_note
title: "AI & Robotics Update — Gemini Robotics 2, Skild S1, OpenAI Research Acceleration"
date: 2026-09-19
channel: ai-robotics
channel_label: AI & Robotics
summary: "최근 AI/Robotics 흐름에서 눈여겨볼 세 가지: whole-body VLA, single-video robot learning, coding agent 기반 연구 가속화."
---

**한 줄 요약:** 최근 흐름은 단순한 “모델 성능 향상”보다, **더 긴 task를 수행하고, 더 적은 data로 적응하며, 연구와 개발 workflow 자체를 바꾸는 방향**으로 가고 있다.

## 1. Gemini Robotics 2 — whole-body intelligence로 확장

Google DeepMind는 Gemini Robotics 2를 공개하며 기존 tabletop manipulation을 넘어 **humanoid whole-body control, dexterous manipulation, multi-robot collaboration**까지 범위를 확장했다.

핵심은 세 모델로 나뉜다는 점이다.

- **Gemini Robotics 2**: vision-language-action model로 whole-body motion과 manipulation을 직접 제어
- **Gemini Robotics ER 2**: multi-step task planning과 embodied reasoning 담당
- **Gemini Robotics On-Device 2**: robot device에서 local inference가 가능하도록 경량화된 VLA

특히 On-Device 2는 새로운 robot embodiment에도 소량의 data로 빠르게 적응하는 방향을 강조한다.

### Why it matters

VLA가 단순히 “팔 하나를 움직이는 policy”에서 벗어나 **walking + manipulation + long-horizon planning**을 하나의 system으로 연결하는 방향으로 가고 있다는 점이 중요하다.

사용자 관점에서는 VLM/VLA 연구를 볼 때 이제 model architecture만이 아니라,  
**high-level reasoning ↔ low-level control ↔ embodiment adaptation**을 함께 봐야 한다는 의미다.

## 2. Skild S1 — single video로 새로운 task를 배우는 robot foundation model

Skild AI의 S1은 NVIDIA infrastructure를 활용해, **단 하나의 video demonstration으로 새로운 long-horizon task를 수행**하는 방향을 보여줬다.

중요한 포인트는 task마다 weight update나 별도 post-training을 하지 않고, video demonstration 자체를 context로 사용한다는 점이다.

즉:

1. 새로운 task 영상 제시
2. task structure 이해
3. 기존 model parameter를 바꾸지 않고 실행

이라는 흐름이다.

### Why it matters

robot learning에서 가장 큰 bottleneck 중 하나는 **새 task마다 data를 다시 모으고 학습해야 하는 비용**이다.

S1이 보여주는 방향은 앞으로 robot policy가 “학습이 끝난 model”이 아니라,  
**실행 시점에 demonstration을 context로 받아 즉시 적응하는 model**로 바뀔 가능성을 보여준다.

## 3. OpenAI — coding agent가 실제 연구 workflow를 바꾸고 있음

OpenAI는 내부 연구 workflow 분석을 통해 coding agent 사용이 단순한 code completion을 넘어 **실험 생성, 코드 작성, 복잡한 연구 task 수행**으로 확대되고 있다고 공개했다.

OpenAI가 강조한 변화는 다음과 같다.

- 연구자가 직접 작성하는 code의 양보다 agent가 수행하는 code 작업 비중 증가
- experiment iteration 속도 증가
- agent에게 맡기는 task의 complexity 증가
- research cycle 자체가 더 빨라지는 현상

### Why it matters

AI researcher의 생산성 도구가 notebook assistant 수준을 넘어 **experiment operator에 가까워지고 있다**는 의미다.

앞으로 개인 연구 workflow에서도:

- paper → idea extraction
- implementation scaffold
- experiment generation
- result organization
- documentation

까지 agent 기반 자동화가 자연스럽게 연결될 가능성이 높다.

## 정리

세 흐름을 묶어보면 다음과 같다.

- **Robotics**: 더 넓은 embodiment와 whole-body task로 확장
- **Robot Learning**: 적은 demonstration으로 즉시 적응
- **AI Research**: agent가 연구 workflow 자체를 가속

즉, 최근 방향은 모델 하나의 benchmark score보다 **system-level intelligence와 adaptation speed** 쪽으로 이동하고 있다.

## Sources

- Google DeepMind — Gemini Robotics 2  
  https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

- NVIDIA — Skild AI S1  
  https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/

- OpenAI — Research acceleration: The view inside OpenAI  
  https://openai.com/index/research-acceleration-view-inside-openai/
