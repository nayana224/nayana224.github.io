---
layout: feed_note
title: "950개 Claude agent가 21시간 genome mining으로 새 enzyme system을 찾았다"
date: 2026-09-24 22:26:12 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Anthropic은 약 950개 Claude agent가 21시간 동안 2억1천만 token을 사용해 genome database를 탐색하고, 기존에 정의되지 않았던 array-associated reverse transcriptase(ART) system을 찾아냈다고 공개했다. Claude Opus 5.5의 cost-per-task 변화와 ROS 2 GPU-resident transport까지 함께 보면 agent와 robotics 모두 단일 모델 점수보다 orchestration·실행 비용·data path가 중요한 system problem으로 이동하고 있다."
---

**약 950개의 Claude agent가 21시간 동안 2억1천만 token을 사용해 DNA sequence를 탐색하고, 기존에 정의되지 않았던 enzyme system 후보를 찾아냈다.** Anthropic의 새 life sciences 연구팀은 이 과정에서 Claude가 20만 개가 넘는 reverse transcriptase(RT)를 모으고, 3,500개 candidate system을 추린 뒤 20개까지 좁혔다고 공개했다.

그중 한 agent가 jumbo phage의 RT 주변에서 반복되는 non-coding DNA array를 발견했고, 추가 분석과 인간 연구자의 wet-lab 검증을 거쳐 이를 **array-associated reverse transcriptase(ART)**라고 명명했다. ART는 RT, 인접 partner gene, 일정 간격의 DNA repeat array로 구성되며, 초기 실험에서는 이 array가 여러 short RNA로 발현되는 것도 확인됐다. 다만 **ART의 실제 biological function은 아직 밝혀지지 않았다.** 따라서 이를 곧바로 새로운 CRISPR나 gene-editing tool로 해석하는 것은 이르다.

흥미로운 부분은 특정 biology model 하나보다 **parallel agent orchestration 자체가 discovery instrument로 사용됐다는 점**이다. 초기 prompt와 wet-lab work를 제외하면 agent들이 literature와 sequence database를 탐색하고, candidate를 비교·비판하고, human-readable report까지 생성했다. `여러 agent가 넓게 탐색 → 후보를 좁힘 → 사람이 physical experiment로 검증`하는 구조는 software agent를 넘어 실제 science workflow에서도 high-level agent와 deterministic/physical verification layer를 어떻게 분리할지 보여주는 사례다.

---

**Claude Opus 5.5는 Opus 5보다 input/output token 가격을 각각 $5→$4, $25→$20 per 1M tokens로 낮추면서, Anthropic 기준 실제 task당 비용은 약 40% 줄였다.** 동시에 Terminal-Bench 4.0은 **66.4%**, OSWorld 2.0은 **81.8%**, AutomationBench는 **40.0%**를 기록했다.

단순히 benchmark 점수가 오른 release라기보다 agent가 긴 작업을 수행할 때 필요한 **token·tool call·step 수를 줄이는 방향**이 더 눈에 띈다. Anthropic은 Opus 5.5가 Opus 5보다 기본 출력 속도가 30% 이상 빠르고, 별도 fast mode에서는 최대 2.5× 속도를 제공한다고 설명한다. 다만 benchmark 수치는 Anthropic 및 각 평가 주체의 특정 harness·effort 설정에서 측정된 결과이므로 서로 다른 agent runtime의 실제 latency나 비용으로 그대로 일반화하면 안 된다.

Coding agent나 high-level robot agent처럼 모델을 한 번 호출하고 끝나는 것이 아니라 observation → reasoning → tool/action → verification을 반복하는 시스템에서는 **single-call intelligence보다 `성공한 task 하나를 끝내는 데 드는 총 inference cost와 step 수`가 더 직접적인 system metric**이 된다. 모델 선택에서도 benchmark accuracy와 함께 cost-per-task, wall-clock time, tool-call count를 같이 측정할 이유가 커졌다.

---

**같은 날 robotics stack 쪽에서는 ROS 2 Lyrical의 `rosidl::Buffer`와 NVIDIA CUDA buffer backend가 GPU-resident data를 표준 ROS message 안에서 직접 전달하는 경로를 열었다.** 같은 host·CUDA device·Linux user와 지원 RMW 조건을 만족하면 co-located node 사이 payload를 host copy·serialization 없이 넘기고, 조건이 맞지 않으면 기존 CPU path로 fallback한다.

Isaac ROS 5.0도 이 upstream mechanism으로 이동하면서 기존 NITROS transport API를 deprecated하고 있다. perception-to-action pipeline에서는 model inference 시간뿐 아니라 **sensor → preprocessing → model → control 사이에서 data가 어떤 memory path로 이동하는지**까지 end-to-end latency에 포함해 봐야 한다는 변화다.

### Sources
- [Anthropic — Claude discovers a novel enzyme system with CRISPR-like repeats](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)
- [Anthropic — Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
- [NVIDIA Technical Blog — Accelerating a ROS 2 Node with an AI Agent and NVIDIA Isaac ROS](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros)
- [Isaac ROS — rosidl::Buffer and Buffer Backends](https://nvidia-isaac-ros.github.io/concepts/rosidl_buffer/index.html)
- [Isaac ROS 5.0 — From NITROS to rosidl::Buffer](https://nvidia-isaac-ros.github.io/v/release-5.0/concepts/rosidl_buffer/nitros_migration.html)
