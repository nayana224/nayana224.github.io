---
layout: feed_note
title: "VLA를 다시 만들지 않고, tactile residual로 contact-rich manipulation을 보정한다"
date: 2026-09-23 08:22:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "VT-Bridge는 pretrained VLA에 0.98M-parameter tactile residual adapter를 붙여 contact-rich manipulation을 고주파로 보정하고, 최대 50개 demonstration으로 평균 task completion을 11.7%에서 62.9%로 높였다."
---

## VT-Bridge: pretrained VLA 위에 tactile residual correction을 얹는다

**VT-Bridge는 π₀, π₀.₅, SmolVLA 같은 pretrained VLA의 backbone architecture를 바꾸지 않고, 0.98M-parameter residual adapter로 tactile feedback을 action에 반영한다.** 논문에서 task당 필요한 vision-tactile demonstration은 최대 50개였고, 네 가지 contact-rich manipulation task에서 task-level VLA fine-tuning만 사용했을 때 평균 completion rate 11.7%가 VT-Bridge 적용 후 **62.9%**로 올라갔다.

핵심은 tactile signal을 VLA 자체에 대규모로 다시 학습시키는 대신, pretrained policy가 낸 action을 **robot execution frequency에서 residual하게 보정**한다는 점이다. adapter topology는 세 VLA backbone에서 동일하고 backbone별 weight만 학습한다. Foundation VLA를 semantic·coarse action prior로 유지하면서 접촉 이후 필요한 correction을 별도 feedback layer가 담당하는 구조다.

이 구분은 contact-rich manipulation에서 특히 흥미롭다. vision만으로는 접촉이 시작된 뒤 실제 force·slip·alignment 상태를 완전히 관찰하기 어렵고, foundation policy 전체를 다시 학습하는 것은 data와 compute 비용이 크다. VT-Bridge는 이 문제를 `큰 VLA를 교체한다`가 아니라 **`실행 주기의 tactile residual policy가 action delta를 수정한다`**로 재정의한다.

다만 62.9%는 저자들이 선택한 세 backbone과 네 task에서 얻은 평균이며, 모든 tactile manipulation으로 일반화할 수 있는 수치는 아니다. 그럼에도 **pretrained generalist policy + 빠른 feedback correction**이라는 분리는 closed-loop grasping이나 deformable/entangled object manipulation을 설계할 때 직접 비교해볼 만한 architecture pattern이다.

### Sources

- [arXiv — VT-Bridge: Bridging Pretrained Foundation VLAs to VTLAs via Lightweight Residual Adaptation](https://arxiv.org/abs/2609.22606)
- [VT-Bridge Project Page](https://hoxnocha.github.io/vt-bridge-web/)
