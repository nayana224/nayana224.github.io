---
layout: feed_note
title: "한 번의 시연을 robot program으로: agent가 primitive와 검증 환경까지 만든다"
date: 2026-09-25 16:06:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "RAPID는 single visual demonstration에서 task specification, manipulation primitive, verification environment를 함께 추론해 reusable robot program을 만들고, TANDEM과 Real-Time EXPO-FT는 각각 selective demonstration과 execution-time reaction을 다룬다."
---

## 한 번 보여주면, coding agent가 robot program을 만들고 스스로 검증한다

**RAPID(Robot Agentic Programming from Demonstrations)는 single visual human demonstration 하나에서 task specification, manipulation primitive, verification environment를 모두 구성하고, candidate robot program을 실행·검증·수정한다.** 기존 agentic robotics가 success signal이나 사람이 만든 primitive, resettable simulator를 미리 제공받는 경우가 많았다면 RAPID는 이 세 요소 자체를 demonstration에서 bootstrap한다.

핵심은 demonstration trajectory를 그대로 replay하는 것이 아니다. RAPID는 push·flip 같은 primitive를 **object-level effect를 구현하는 local trajectory-optimization program**으로 만들고, primitive 사이를 object-centric relational constraint로 연결한다. 실행 시 scene geometry를 다시 계산하기 때문에 demonstrated pose나 waypoint에 고정되지 않는다.

저자들은 8개의 contact-rich nonprehensile manipulation task에서 task당 **single demonstration → 50개 novel scene**으로 generalization을 평가했다. RAPID의 simulation 평균 success는 **75.9%**, scene-variant verification을 제거하면 **53.2%**였으며, 비교한 CaP-Agent0 계열은 14.6% 이하에 머물렀다. LIBERO-Pro에서도 6개 setting 중 5개에서 가장 높은 success를 기록했다.

실제 Franka Research 3에서도 같은 8개 nonprehensile task를 task당 10개 scene으로 평가했다. 중요한 점은 agent가 단순 high-level plan만 출력하는 것이 아니라 **demonstration → primitive construction → simulated verification → failure diagnosis/revision → reusable strategy**라는 engineering loop를 닫는다는 것이다.

이 구조는 deterministic primitive와 high-level agent를 결합하는 robotics architecture를 더 자동화하는 방향으로 볼 수 있다. 특히 contact-rich manipulation에서 primitive library를 사람이 전부 미리 설계해야 한다는 가정을 줄인다는 점이 흥미롭다.

다만 현재 formulation은 quasi-static rigid-body manipulation을 중심으로 하고, deployment에서도 RGB-D scene reconstruction과 trajectory optimization에 의존한다. deformable·entangled object나 빠른 dynamic interaction까지 같은 방식으로 일반화됐다고 보기는 이르다.

## 사람이 전체 task를 시연하지 않고, planner가 막힐 때만 개입한다

**TANDEM은 long-horizon demonstration 수집을 planner가 할 수 있는 구간과 사람이 필요한 구간으로 나눈다.** TAMP(Task and Motion Planning)가 가능한 단계는 자동으로 수행하고, planning domain에 없는 단계에서만 human teleoperator를 on-demand capability처럼 호출한다.

human intervention point를 task마다 미리 hard-code하지 않는다. pretrained vision-language model을 이용해 missing predicate와 사람이 실행할 magic operator를 planning domain에 추가하고, human stage가 끝나면 scene을 다시 perception해 intended effect가 성립했는지 확인한 뒤 autonomous planning을 이어간다.

저자 실험의 대표 long-horizon task에서는 같은 human intervention time으로 full-task teleoperation 대비 **2.9× 많은 demonstrations**를 수집했다. pretrained **π₀.₅-DROID**를 task당 20개의 TANDEM demonstration으로 fine-tune했을 때 다섯 long-horizon task의 평균 success는 **0% → 60%**로 증가했다.

robot learning 관점에서는 사람이 모든 trajectory를 처음부터 끝까지 제공하는 대신, **autonomy가 실패하는 boundary에서만 demonstration을 요청하는 방식**으로 볼 수 있다. deterministic primitive/planner와 learned VLA를 함께 쓰는 system에서는 어디까지 automation하고 어디서 human data를 요청할 것인가를 data-collection 단계부터 설계할 수 있다는 점이 중요하다.

다만 논문은 현재 under review이며 평가는 다섯 long-horizon manipulation task에 한정된다. planner의 domain coverage와 perception error가 달라질 때 human-efficiency gain이 얼마나 유지되는지는 더 넓은 평가가 필요하다.

## 느린 VLA는 그대로 두고, 실행 직전 action만 빠르게 고친다

**Real-Time EXPO-FT는 큰 VLA의 느린 inference를 없애려 하지 않고, 최신 observation을 보는 lightweight edit policy를 별도로 둔다.** base VLA가 expressive action chunk를 천천히 생성하는 동안 fast policy가 실행 시점의 state를 보고 그 action을 수정하며, Q-function이 candidate chunk를 선택한다.

문제는 단순 throughput이 아니다. VLA inference에 시간이 걸리면 action을 계산할 때 본 observation과 실제 실행 시점의 state가 달라지는 **stale-observation distribution shift**가 생긴다. 이 연구는 slow deliberation과 fast reaction을 두 timescale로 분리해 latency 자체를 policy training 문제로 다룬다.

Kinetix에서는 delayed policy가 delayed/non-delayed 비교를 포함한 **10개 환경 모두에서 최고 성능**을 기록했다. 네 dynamic real-world task—object passing, ball balancing, table-soccer kicking, dynamic object picking—에서는 online robot data를 task당 최대 10분만 사용해 평균 performance를 **42%에서 97%**로 높였다고 보고한다. human intervention 없이 RL로 adaptation한다.

이 구조는 VLA deployment에서 model latency를 단순히 더 빠른 GPU로 해결해야 하는 비용 문제로만 보지 않게 한다. **느린 high-level action prior + 최신 state를 반영하는 fast residual/edit layer**라는 분리는 움직이는 물체나 contact 변화처럼 execution 중 state가 계속 바뀌는 closed-loop manipulation에 특히 직접적인 설계 선택지다.

다만 실세계 평가는 네 dynamic task이고 online RL을 요구한다. fast edit policy가 base VLA의 잘못된 semantic plan이나 irreversible contact failure까지 복구한다고 볼 수는 없다.

## Sources
- [arXiv — RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249)
- [Project page — RAPID](https://yuyaoliu.me/projects/rapid)
- [arXiv — TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](https://arxiv.org/abs/2609.28314)
- [arXiv — Reinforcement Learning for Real-Time Vision-Language-Action Policies](https://arxiv.org/abs/2609.18207)
- [Project page — Real-Time EXPO-FT](https://pd-perry.github.io/real-time-expo-ft/)
