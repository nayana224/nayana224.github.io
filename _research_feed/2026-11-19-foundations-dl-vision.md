---
layout: feed_note
title: "[필수 기초 로드맵 ④] 딥러닝 & 3D 로봇 비전: ResNet·Transformer부터 ViT·CLIP·PointNet++까지 필수 논문 5선"
date: 2026-11-19 08:00:00 +0900
channel: foundations
channel_label: "Foundations · 필수 기초"
tags: ["3D Vision", "VLA / VLM"]
source_url: "https://arxiv.org/abs/1706.03762"
summary: "현대 로보틱스와 VLA의 눈과 두뇌를 이루는 딥러닝·비전 필수 기초 논문 5편(ResNet, Transformer, ViT, CLIP, PointNet++)이 각각 어떤 병목을 어떻게 뚫었는지 직관적으로 정리합니다."
---

최신 로봇 논문(VLA, 3D Manipulation, World Model)을 열어보면 항상 등장하는 블록들이 있습니다: *"시각 인코더로 ViT와 CLIP/SigLIP을 쓰고, 3D 점군(Point Cloud)은 PointNet++로 읽은 뒤, Transformer 백본에 넣는다."*

이 블록들이 왜 탄생했는지 **핵심 아이디어 한 줄씩**만 정확히 꿰고 있으면 어떤 최신 논문 아키텍처 그림을 봐도 부품 조립도처럼 한눈에 읽힙니다.

---

## 한눈에 보는 진화 계보

`① ResNet (깊은 신경망의 지름길 연결) → ② Transformer (모든 단어·부품이 서로를 직접 참조하는 Attention) → ③ ViT (사진도 바둑판 조각으로 잘라 단어처럼 처리) → ④ CLIP (사진과 자연어를 같은 의미 공간에 정렬) → ⑤ PointNet++ (3D RGB-D 점군에서 물체 형상 읽기)`

---

## 1. ResNet (Deep Residual Learning, 2015)
- **원문:** [*Deep Residual Learning for Image Recognition* (`arXiv:1512.03385`)](https://arxiv.org/abs/1512.03385)
- **해결한 문제:** 신경망 층(Layer)을 깊게 쌓으면 더 똑똑해져야 하는데, 20층만 넘어가도 신호가 사라져 오히려 얕은 신경망보다 성적이 나빠졌습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 원래 값 $x$를 다음 층으로 그대로 넘겨주는 **지름길 통로(Skip Connection, $y = F(x) + x$)**를 뚫어주었습니다.
  - 신경망이 처음부터 전체 답을 새로 배우는 대신 **'원래 입력에서 고쳐야 할 차이(나머지, Residual)만 배우게'** 만들어, 수백 층짜리 딥러닝과 모든 현대 신경망 블록의 기본 뼈대가 되었습니다.

---

## 2. Transformer (*Attention Is All You Need*, 2017)
- **원문:** [*Attention Is All You Need* (`arXiv:1706.03762`)](https://arxiv.org/abs/1706.03762)
- **해결한 문제:** 기존 RNN은 문장을 첫 단어부터 순서대로 한 글자씩 읽어야 해서, 문장이 길어지면 앞부분을 까먹고 GPU 병렬 계산도 불가능했습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 순차 읽기를 버리고, **모든 단어가 다른 모든 단어와 한꺼번에 직통 전화를 걸어 "내가 지금 누구에게 집중(Attention)해야 하는지" 가중치를 계산**합니다(**Self-Attention**).
  - 로보틱스에서는 `[카메라 토큰 + 언어 명령 토큰 + 현재 로봇 관절 토큰 + 미래 행동 토큰]`을 한 방에 넣어 서로 관계를 계산하는 만능 결합기로 쓰입니다.

---

## 3. ViT (Vision Transformer, 2020)
- **원문:** [*An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (`arXiv:2010.11929`)](https://arxiv.org/abs/2010.11929)
- **해결한 문제:** 텍스트는 Transformer를 쓰고 이미지는 CNN을 쓰다 보니, 시각과 언어를 하나의 모델에서 자연스럽게 합치기 번거로웠습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - **"사진 한 장을 $16 \times 16$ 픽셀 크기의 작은 타일(Patch)들로 잘라서, 각 타일을 문장의 '단어 하나'처럼 Transformer에 그대로 넣자!"**
  - 이 단순한 발상 덕분에 이미지와 텍스트가 완전히 똑같은 형태의 '토큰(Token)'이 되었고, 오늘날 모든 VLM과 VLA의 기본 눈(Vision Encoder)이 되었습니다.

---

## 4. CLIP (OpenAI, 2021)
- **원문:** [*Learning Transferable Visual Models From Natural Language Supervision* (`arXiv:2103.00020`)](https://arxiv.org/abs/2103.00020)
- **해결한 문제:** 기존 이미지 분류기는 사람이 미리 정해둔 1,000개 이름표(개, 고양이, 자동차...)만 맞힐 수 있어서, 로봇에게 *"파란색 손잡이가 달린 드라이버 집어줘"*처럼 새로운 물체를 말로 지시할 수 없었습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 인터넷에서 수집한 4억 쌍의 **(사진, 사진 설명 텍스트)**를 이용해, **같은 뜻의 사진 벡터와 문장 벡터는 가까워지고 다른 쌍은 멀어지도록(Contrastive Learning)** 학습시켰습니다.
  - 덕분에 한 번도 학습해 본 적 없는 물체라도 자연어 설명만 주면 화면에서 바로 찾아내는 **Zero-shot 시각-언어 정렬**이 가능해졌습니다.

---

## 5. PointNet / PointNet++ (Stanford, 2017)
- **원문:** [*PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space* (`arXiv:1706.02413`)](https://arxiv.org/abs/1706.02413)
- **해결한 문제:** 2D 사진만으로는 물체까지의 정확한 거리(Depth)나 컵 뒷면의 3차원 파지 자세(6-DoF Grasp Pose)를 알기 어렵습니다. 하지만 RGB-D 카메라나 LiDAR에서 나오는 **3D 점군(Point Cloud)**은 점들의 순서가 뒤죽박죽이라 일반 CNN에 넣을 수 없습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 점들의 순서를 어떻게 섞어도 결과가 바뀌지 않는 대칭 함수(Max Pooling)를 쓰고, 가까운 주변 점들끼리 단계적으로 묶어(Hierarchical Grouping) **3차원 공간의 국소 곡면과 전체 물체 형상을 동시에 읽어내는 3D 로보틱스의 필수 백본**입니다.
