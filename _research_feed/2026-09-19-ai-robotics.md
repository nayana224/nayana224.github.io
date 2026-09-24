---
layout: feed_note
title: "Claude가 Anthropic R&D의 26%를 맡고, AI 평가는 회사 안으로 들어갑니다"
date: 2026-09-19 11:30:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Claude의 Anthropic R&D 참여, embedded evaluation, 그리고 Physical AI의 edge compute·real-world data 변화를 짧게 정리했습니다."
---

Claude가 Anthropic AI R&D 작업의 **26%에서 lead 역할**을 맡고 있습니다. 2026년 2월에는 1% 미만이었습니다.

동시에 Anthropic은 외부 evaluator를 회사 안으로 들여 **직원에 준하는 접근권한으로 frontier model을 평가**하기 시작합니다.

AI가 연구 workflow 안으로 깊게 들어갈수록, evaluation도 같은 속도로 개발 loop 안에 들어오는 모습입니다.

<!-- feed-figure:three-shifts -->
<figure class="paper-figure">
 <div class="paper-figure-frame"><div class="paper-figure-canvas">
 <svg viewBox="0 0 760 280" role="img" aria-label="AI R&D evaluation and physical AI shifts">
  <text x="24" y="28" class="fig-kicker">THREE SYSTEM-LEVEL SHIFTS</text>
  <rect x="36" y="76" width="196" height="126" rx="3" class="fig-box-accent"/>
  <text x="134" y="105" class="fig-label">AI in R&D</text><text x="134" y="135" class="fig-small">model as collaborator</text><text x="134" y="158" class="fig-small">→ lead role in some work</text>
  <rect x="282" y="76" width="196" height="126" rx="3" class="fig-box"/>
  <text x="380" y="105" class="fig-label">Embedded Evaluation</text><text x="380" y="135" class="fig-small">evaluation moves</text><text x="380" y="158" class="fig-small">inside development loop</text>
  <rect x="528" y="76" width="196" height="126" rx="3" class="fig-box"/>
  <text x="626" y="105" class="fig-label">Physical AI</text><text x="626" y="135" class="fig-small">edge compute +</text><text x="626" y="158" class="fig-small">real-world robot data</text>
  <text x="380" y="238" class="fig-small">The common theme is system integration, not model capability alone.</text>
 </svg></div></div>
 <figcaption><strong>Figure 1.</strong> 9월 19일 업데이트의 공통점은 AI capability 자체보다 연구·평가·배포 loop 안으로 AI가 더 깊이 들어간다는 점이다. Sources are linked below.</figcaption>
</figure>

## Claude가 AI를 만드는 과정에 직접 들어오고 있습니다

Anthropic 내부 측정에서 Claude는 AI R&D의 **26%에서 lead**, 90%가 넘는 작업에서 collaborator로 참여했습니다.

Coding assistant를 넘어 다음 세대 model을 만드는 연구 과정 자체에 AI가 들어오고 있다는 신호입니다.

## Frontier model 평가도 외부 검사에서 embedded evaluation으로 갑니다

Anthropic과 Accenture는 향후 5년 동안 **각각 최소 10억 달러**를 투입해 embedded evaluation 역량을 구축하기로 했습니다.

Evaluator가 Anthropic 내부에서 model evaluation, red-teaming, alignment assessment, safeguard testing을 수행합니다.

강한 model을 만든 뒤 밖에서 시험하는 것보다, **개발 중간부터 평가를 붙이는 구조**로 옮겨가는 변화입니다.

## Physical AI는 edge compute와 real-world data를 같이 밀고 있습니다

NVIDIA Jetson Orin Nano 2는 **78 TOPS, 8GB memory**와 이전 세대 대비 2배 inference performance를 제시했습니다.

Spirit AI는 약 1,000명의 contractor가 수집하는 real-world robot data를 중심으로 humanoid를 학습하고 있다고 밝혔습니다.

Robot Learning에서는 결국 model 크기만큼 **어디서 inference하고 어떤 data로 반복 학습하는지**가 중요해지고 있습니다.

## Sources
- [Anthropic — Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development)
- [Anthropic — Partnering with Accenture on embedded evaluation](https://www.anthropic.com/news/accenture-embedded-evaluation)
- [NVIDIA Jetson Orin Nano 2 — product details reported September 18](https://roboticsandautomationnews.com/2026/09/18/nvidia-unveils-jetson-orin-nano-2-for-robotics-and-edge-ai/104918/)
- [Reuters — Spirit AI sees robot-brain breakthrough as soon as 2027](https://www.reuters.com/world/asia-pacific/founder-chinese-startup-spirit-ai-says-robot-brains-set-2027-breakthrough-2026-09-18/)
