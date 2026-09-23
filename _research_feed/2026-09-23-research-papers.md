---
layout: feed_note
title: "Contact-rich VLA에서 edge inference까지, robot policy의 실행 계층이 바뀌고 있다"
date: 2026-09-23 12:10:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "VT-Bridge와 Opt2VLA는 contact-rich manipulation의 feedback·force interface를 확장하고, rMuscle은 반복 robot execution의 내부 유사성을 cache해 VLA inference 자체를 가속한다."
---

## 1/ VT-Bridge: pretrained VLA 위에 tactile residual correction을 얹는다

**VT-Bridge는 π₀, π₀.₅, SmolVLA 같은 pretrained VLA의 backbone architecture를 바꾸지 않고, 0.98M-parameter residual adapter로 tactile feedback을 action에 반영한다.** 논문에서 task당 필요한 vision-tactile demonstration은 최대 50개였고, 네 가지 contact-rich manipulation task에서 task-level VLA fine-tuning만 사용했을 때 평균 completion rate 11.7%가 VT-Bridge 적용 후 **62.9%**로 올라갔다.

핵심은 tactile signal을 VLA 자체에 대규모로 다시 학습시키는 대신, pretrained policy가 낸 action을 **robot execution frequency에서 residual하게 보정**한다는 점이다. Foundation VLA를 semantic·coarse action prior로 유지하면서 접촉 이후 필요한 correction을 별도 feedback layer가 담당한다.

다만 62.9%는 저자들이 선택한 세 backbone과 네 task에서 얻은 평균이며 모든 tactile manipulation으로 일반화할 수 있는 수치는 아니다. 그럼에도 **pretrained generalist policy + 빠른 feedback correction**이라는 분리는 closed-loop manipulation에서 직접 비교할 만한 architecture pattern이다.

## 2/ Opt2VLA: VLA가 trajectory뿐 아니라 contact force까지 명시적으로 출력한다

**Opt2VLA는 humanoid contact-rich manipulation에서 VLA의 action interface 자체를 확장해 geometric motion goal과 continuous contact-force reference를 함께 예측한다.** 기존 humanoid VLA가 주로 geometric target을 만들고 whole-body controller가 motion tracking을 담당했다면, 여기서는 task context에 따라 필요한 interaction force도 high-level policy의 명시적 output이 된다.

예측된 motion·force reference는 task-specific RL whole-body controller가 추종한다. 학습 supervision은 explicit force reference를 포함한 whole-body trajectory optimization으로 생성해 dynamically feasible하고 contact-consistent한 trajectory를 만들며, 저자들은 세 contact-rich humanoid task에서 motion-only control보다 force regulation이 더 정확하고 일관됐다고 보고한다. Closed-loop evaluation에서는 simulation뿐 아니라 humanoid hardware에서도 **language-conditioned force modulation**을 보였다.

VT-Bridge와 나란히 보면 차이가 선명하다. VT-Bridge가 `기존 VLA action + tactile residual correction`으로 실행 단계의 feedback을 보강한다면, Opt2VLA는 `VLA → motion + force reference → whole-body controller`처럼 **force를 policy-control interface의 일부로 올린다.** 접촉 이후 상태를 어떻게 피드백할지뿐 아니라, 상위 policy가 애초에 힘을 어느 수준까지 의도해야 하는지도 contact-rich manipulation의 중요한 설계 축이라는 신호다.

Opt2VLA의 결과 역시 세 task에 대한 저자 평가이므로 general-purpose force-aware VLA로 일반화해서 해석하면 안 된다. 특히 task-specific controller와 trajectory-optimization supervision에 얼마나 의존하는지는 더 넓은 object/task generalization에서 확인할 부분이다.

## 3/ rMuscle: 반복되는 robot execution을 VLA의 'muscle memory'로 cache한다

**rMuscle은 VLA inference에서 반복 robot execution 사이의 유사성을 이용해 visual-token output과 neuron activation pattern을 재사용하는 dual-phase cache를 제안한다.** Context Cache는 visual-token computation을 줄이고, Action Cache는 denoising 과정에서 반복되는 activation pattern을 이용해 weight access를 줄인다.

중요한 점은 단순 KV cache를 더 크게 두는 접근이 아니라 **robot workload 자체의 반복성**을 inference optimization 대상으로 삼았다는 것이다. 저자들은 LIBERO, RoboTwin과 physical manipulation task에서 RTX 4090과 Jetson Thor를 평가했고, 기존 success rate를 유지하면서 **1.29–1.42× speedup**을 보고한다. Cache overhead를 줄이기 위해 online cache recomputation, sliding-window retrieval, consecutive denoising step 사이의 mask sharing도 사용한다.

이 결과는 VLA deployment에서 model compression만 볼 필요가 없다는 신호다. 공장·랩 자동화처럼 비슷한 scene과 task가 반복되는 환경이라면 `현재 observation → 매번 전체 VLA 계산` 대신 **이전 execution의 내부 state를 어디까지 안전하게 재사용할 수 있는가**가 별도의 system-design 축이 된다. 특히 edge robot에서는 model latency뿐 아니라 cache memory footprint와 stale-state failure를 함께 봐야 한다.

수치는 저자들이 평가한 model·hardware·task 조합에 한정된다. 반복성이 낮은 open-world manipulation에서도 같은 cache hit와 speedup이 유지되는지는 추가 검증이 필요하다.

### Sources

- [arXiv — VT-Bridge: Bridging Pretrained Foundation VLAs to VTLAs via Lightweight Residual Adaptation](https://arxiv.org/abs/2609.22606)
- [VT-Bridge Project Page](https://hoxnocha.github.io/vt-bridge-web/)
- [arXiv — Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2609.23968)
- [Fukang Liu — Opt2VLA research overview](https://fukangl.github.io/)
- [arXiv — rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference](https://arxiv.org/abs/2609.19104)
