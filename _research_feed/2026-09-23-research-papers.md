---
layout: feed_note
title: "Contact-rich VLA와 실행 가능한 paper agent, 연구 interface가 바뀌고 있다"
date: 2026-09-23 10:30:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "VT-Bridge와 Opt2VLA는 contact-rich manipulation의 feedback·force interface를 확장하고, Paper2Agent는 논문·코드·데이터를 검증된 MCP tool로 바꿔 연구 결과 자체를 agent-callable interface로 만든다."
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

## 3/ Paper2Agent: 논문을 읽는 agent가 아니라, 논문의 방법을 호출하는 agent를 만든다

**Nature에 공개된 Paper2Agent는 paper·supplement·code·dataset·workflow를 분석해 자동으로 MCP server를 만들고, 원 코드의 결과와 대조하는 test까지 통과한 tool만 agent에게 노출한다.** 즉 PDF를 RAG로 검색하는 데서 멈추지 않고 논문의 방법 자체를 `tools + resources + prompts` 형태의 실행 가능한 interface로 바꾼다.

구성도 꽤 구체적이다. environment agent가 실행 환경을 만들고 extraction agent가 핵심 method를 tool로 변환한 뒤 testing agent가 expected file, numerical tolerance, figure reference 등을 검사한다. 반복 검증에 실패하는 tool은 최종 MCP에서 제외된다. 논문에 따르면 AlphaGenome 사례에서는 **22개 MCP tool을 약 45분, 약 $14의 비용으로 생성했고 전부 automated validation을 통과**했다.

이 구조에서 MCP는 단순 connector가 아니라 **연구 방법의 machine-callable boundary**가 된다. 여러 paper MCP를 하나의 chat agent에 동시에 연결할 수도 있기 때문에, 향후 scientific agent의 중요한 구성요소가 `논문을 얼마나 잘 요약하는가`보다 `어떤 검증된 method를 어떤 provenance와 함께 호출할 수 있는가`로 이동할 가능성을 보여준다.

다만 현재 주요 case study는 AlphaGenome·Scanpy·TISSUE 같은 computational biology 중심이다. robotics paper처럼 simulator, robot hardware, calibration, sensor state가 필요한 연구를 같은 수준으로 agentify할 수 있는지는 별도 문제다. 오히려 이 차이가 robotics에서 reproducible tool interface를 설계할 때 무엇을 추가로 표현해야 하는지 보여주는 좋은 기준점이다.

### Sources

- [arXiv — VT-Bridge: Bridging Pretrained Foundation VLAs to VTLAs via Lightweight Residual Adaptation](https://arxiv.org/abs/2609.22606)
- [VT-Bridge Project Page](https://hoxnocha.github.io/vt-bridge-web/)
- [arXiv — Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2609.23968)
- [Fukang Liu — Opt2VLA research overview](https://fukangl.github.io/)
- [Nature — Reimagining research papers as interactive and reliable AI agents](https://www.nature.com/articles/s41586-026-11044-y)
- [GitHub — jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent)
