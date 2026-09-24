---
layout: feed_note
title: "BoxBot은 VLA를 모든 곳에 쓰지 않았다"
date: 2026-09-24 15:53:46 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "Viam의 BoxBot은 1–2 mm tape seam에는 visual servoing을, deformable flap manipulation에는 fine-tuned SmolVLA를 배치하고 Jetson Orin Nano에서 로컬 추론한다."
---

Viam의 **BoxBot**은 taped cardboard box를 여는 하나의 작업을 `visual servoing + learned VLA`로 분리했다. tape seam처럼 **1–2 mm 수준의 정밀한 경로 추종**은 image-based visual servoing으로 처리하고, 잘 휘고 접촉 상태가 계속 달라지는 네 개의 flap을 여는 구간은 **fine-tuned SmolVLA**가 맡는다.

흥미로운 지점은 VLA를 전체 manipulation stack의 대체재로 쓰지 않았다는 것이다. geometry가 비교적 명확하고 feedback control이 잘 맞는 부분은 classical method에 남겨두고, analytical하게 모델링하기 어려운 contact-rich/deformable interaction만 learned policy에 넘겼다. 두 부분은 같은 application 안에서 동작하며 SmolVLA inference는 **NVIDIA Jetson Orin Nano에서 local**로 실행된다.

Viam은 VR controller로 약 **5시간 동안 125 demonstrations**를 수집했다고 밝혔다. synchronized arm/camera data로 SmolVLA를 LeRobot에서 fine-tuning했고 model과 dataset도 공개했다. 다만 현재 Hugging Face model card에는 실제 training dataset이 **110 episodes / 29,821 frames / 10 FPS**로 기록돼 있어, 발표문의 125 collected demonstrations와 최종 학습에 사용된 episode 수는 구분해서 볼 필요가 있다. 또한 model card에는 아직 별도의 quantitative evaluation result가 제공되지 않았다.

Robot manipulation system을 설계할 때 중요한 질문이 `VLA를 쓸 것인가?`보다 **`어느 subproblem까지 deterministic primitive/control로 남기고, 어디부터 learned policy에 맡길 것인가?`**일 수 있음을 보여주는 concrete implementation이다. 특히 high-level agent + deterministic primitive 구조나 edge robotics를 생각할 때 참고하기 좋은 사례다.

### Sources
- [Viam — Viam Debuts Box-Opening Robot at IROS 2026](https://www.viam.com/press-releases/viam-debuts-box-opening-robot-at-iros-2026)
- [Hugging Face — viamrobotics/smolvla-box-bot](https://huggingface.co/viamrobotics/smolvla-box-bot)
- [Hugging Face LeRobot — SmolVLA documentation](https://huggingface.co/docs/lerobot/v0.4.3/en/smolvla)
