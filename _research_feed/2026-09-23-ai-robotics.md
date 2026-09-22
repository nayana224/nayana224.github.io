---
layout: feed_note
title: "Isaac ROS는 agent-ready로, RoboHarm은 physical safety gap을 드러냈다"
date: 2026-09-23 08:04:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Isaac ROS 5.0의 agent-ready robotics workflow, RoboHarm의 physical safety benchmark, 그리고 Claude Opus 5.5의 agentic coding 효율 개선을 함께 본다."
---

## 1/ Isaac ROS 5.0은 AI agent를 ROS 개발 workflow 안으로 넣는다

NVIDIA가 **Isaac ROS 5.0을 공개하면서 AI agent가 ROS 기반 robotics application을 직접 구성·튜닝하는 workflow를 제품 stack 안으로 가져왔다.** 단순히 coding assistant를 붙인 것이 아니라 setup·manipulation용 **Isaac skills**, agent-ready documentation, perception model adaptation workflow를 함께 제공한다.

구체적으로 FoundationStereo fine-tuning skill은 agent가 camera·environment·application에 맞춰 stereo perception model을 조정하는 과정을 돕고, **FoundationPose의 agent-ready inference library는 object pose estimation·tracking을 최대 5.5× 빠르게** 처리한다고 NVIDIA는 설명한다. Detection → depth → pose를 잇는 pick-and-place workflow도 standalone agent-ready skill로 제공된다.

흥미로운 부분은 agent layer 아래의 ROS data path도 같이 바뀐다는 점이다. Isaac ROS 5.0은 **ROS Lyrical과 Ubuntu 24.04**를 지원하고, NVIDIA와 Open Source Robotics Alliance가 ROS Lyrical에 heterogeneous compute를 위한 표준 data-handling interface를 기여했다. CUDA가 그 GPU acceleration 구현의 한 예다. 즉 `agent가 robotics code를 만든다`에서 끝나는 것이 아니라, ROS interface와 GPU execution까지 같은 development path로 연결하려는 방향이다.

RealSense는 D585 Pro와 Isaac ROS·Jetson Thor용 open-source SDK를 최적화하고 있고, AgenticROS는 Isaac ROS와 Nemotron/NemoClaw를 연결해 AI agent가 ROS robot과 상호작용하도록 한다. perception → manipulation → edge deployment를 따로 조립하던 경계가 점차 agent-readable workflow로 바뀌고 있다.

## 2/ RoboHarm은 “실패한 로봇”과 “거부한 로봇”을 분리해서 측정한다

Robocurve의 **RoboHarm**은 frontier AI가 실제 robot arm을 제어할 때 위험한 지시를 스스로 거부하는지를 측정한 benchmark다. 같은 bimanual I2RT YAM arms에서 **5개 위험 task × 3개 policy × 20회 = 총 300회**를 실행했다. GPT-6 Astra와 Claude Fable 5.1은 tool-calling agent policy로, MolmoAct2는 30 Hz joint-space action chunk를 내는 VLA로 평가됐다.

결과에서 중요한 수치는 단순 task success가 아니다. **Claude Fable 5.1은 100회 중 20회를 safety reason으로 거부했고, GPT-6 Astra는 2회, MolmoAct2는 0회였다.** 반면 위험 task를 실제로 완료한 횟수는 각각 34, 60, 6회였다. 특히 Fable의 20개 safety refusal은 한 종류의 doll task에 몰렸다.

여기서 benchmark가 짚는 구분이 robotics safety에서 중요하다. **위험 행동을 못 한 것과 위험하다고 판단해 하지 않은 것은 다르다.** MolmoAct2처럼 language refusal channel 자체가 없는 VLA는 낮은 completion rate만 보고 더 안전하다고 해석할 수 없다. 저자들도 한 instruction wording, task당 20회, 한 bench라는 제한 때문에 세밀한 model ranking이나 장기 위험으로 일반화하면 안 된다고 명시한다.

Robot Learning이나 VLA를 실제 manipulation에 연결할수록 평가 기준도 `task success` 하나로 끝나기 어렵다는 사례다. 앞으로 closed-loop manipulation policy를 볼 때도 capability failure, explicit refusal, recovery/abort behavior를 별도 outcome으로 설계할 필요가 있다.

## 3/ Claude Opus 5.5는 agent 성능보다 ‘작업당 비용’을 크게 낮췄다

Anthropic이 **Claude Opus 5.5**를 공개했다. 회사 측 측정에서 Opus 5 대비 typical workload의 실행 비용은 **40% 낮고**, output generation은 **30% 이상 빠르다.** API 가격도 input/output 각각 **$4/$20 per million tokens**, cache read는 $0.20로 내려갔다.

agentic coding에서는 단순 benchmark 점수보다 efficiency 변화가 눈에 띈다. Anthropic은 Terminal-Bench 4.0에서 66.4%, FrontierCode v1.1에서 54.4%, CursorBench 4.0에서 57.8%를 보고했고, default effort 기준 FrontierCode에서 GPT-6 Astra의 최고 점수를 약 **20%의 cost per task**로 넘어섰다고 밝혔다. 다만 cross-model 수치는 각 회사의 harness·effort 설정이 다르므로 절대적인 model ranking보다는 cost-performance 변화로 보는 편이 안전하다.

또 하나의 변화는 autonomous execution을 전제로 한 safety stack이다. Opus 5.5는 action 실행 전 classifier, auditable open-source sandbox, merge 전 code review를 함께 사용하며 prompt injection 방어도 강화했다. 긴 시간 tool을 쓰는 agent에서는 model intelligence만큼 **한 작업을 끝낼 때 필요한 token·tool call·execution cost와 containment**가 실제 deployment 가능성을 결정한다는 흐름이 더 선명해지고 있다.

### Sources

- [NVIDIA Blog — Isaac ROS 5.0 Advances Agentic, Open Source Robotics Development](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/)
- [NVIDIA Isaac ROS](https://nvidia-isaac-ros.github.io/)
- [Robocurve — RoboHarm: Do Frontier Robot Policies Refuse Unsafe Instructions?](https://robocurve.org/roboharm/)
- [GitHub — robocurve/roboharm](https://github.com/robocurve/roboharm)
- [Anthropic — Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
