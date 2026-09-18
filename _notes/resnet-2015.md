---
layout: note
title: "ResNet (2015) 논문 정리"
title_ko: "ResNet (2015) 논문 정리"
title_en: "ResNet (2015) Paper Notes"
date: 2026-09-17
category: Papers
category_ko: 논문
category_en: Papers
summary: "Degradation problem, residual learning, identity shortcut을 중심으로 ResNet의 핵심 아이디어를 정리한 노트."
summary_ko: "Degradation problem, residual learning, identity shortcut을 중심으로 ResNet의 핵심 아이디어를 정리한 노트."
summary_en: "Notes on the degradation problem, residual learning, and identity shortcuts in ResNet."
source: Notion
source_language: ko
---

## 1. Abstract
1. Problem
  네트웤를 더 깊게 만들고 싶지만, 깊어질수록 학습하기 어려워진다. <br>특히, training error 자체가 안 좋아지더라.
2. Core idea
  기존 mapping을 직접 학습시키지 말고, 입력을 기준으로 residual을 학습하도록 바꾸자.
3. Evidence
  plain network는 depth 증가 시 악화되지만 ResNet은 34, 110, 152층까지 depth 증가가 optimization/accuracy 개선으로 이어짐

## 2. Introduction
1. Problem
  핵심 문제는 단순히 vanishing gradient가 아니다. vanishing/exploding gradient는 initialization과 normalization으로 상당 부분 완화되었는데도, `network를 더 깊게 만들었더니 training error 자체가 더 높아지는 degradation problem`이 발생했다.
  
> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

2. 저자들의 관찰
  더 깊은 network는 적어도 추가된 layer들이 $x→x$$ 만 수행하면 얕은 network와 같은 성능을 낼 수 있어야 한다. 하지만 실제 optimizer가 잘 해결하지 못한다. 따라서 저자들은 이것을 optimization problem으로 본다.
3. Core idea
  그래서 $H(x)$$를 직접 학습하는 대신, $F(x) = H(x) - x$$ 를 학습하게 만들고, $H(x) = F(x) + x$$로 복원한다. 즉 identity를 기준점으로 두고, 그 기준에서 필요한 변화만 학습하자는 발상이다.
  
> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

## 3.1 Residual Learning
여러 nonlinear layer를 거친 함수  $H(x)=L_n(\cdots L_2(L_1(x)))$$ 는 매우 복잡한 함수들을 표현할 수 있다. 그런데 그 복잡한 parameterization 안에서 의외로 아주 단순한 $H(x) = x$$ 라는 identity mapping을 optimizer가 실제 학습을 통해 찾아가는 것이 쉽지 않을 수 있다.
그래서 ResNet은 문제를 바꿔버린다. Plain의 경우 $H(x)≈x$$ 를 여러 layer가 직접 만들어야 하지만, 
Residual 아이디어는 $H(x)=F(x)+x$$ 이므로 identity가 필요하다면 $F(x)+x=x$$
즉, $F(x)=0$$ 이면 된다. 
따라서, `optimizer가 해야 할 일`을 여러 nonlinear layer로 x를 다시 만들어라에서 `추가적인 변화가 필요 없으면 residual을 0으로 만들어라`로 바꾼 것이다.
> identity $H(x)=x$$ 를 직접 찾아가기 어렵다면, 아예 $x$$는 shortcut으로 주고 network는 $F(x)=0$$ 찾게 만들자는 것.

## 3.2 Identity Mapping by Shortcuts
residual learning을 몇 개의 stacked layer마다 하나의 building block으로 적용한다.
**element-wise adding**
$y=F(x,\{W_i\})+x$$ → `두 tensor의 shape가 동일한 경우`
$y=F(x,\{W_i\})+W_sx$$ → `두 tensor의 shape가 동일하지 않은 경우`
-  $F(x,\{W_i\})$$ : 블록 안의 여러 layer가 학습해야 하는 residual mapping이다.
- 단, 더하는 두 tensor를 element-wise add하기 위해선 shape가 동일해야 한다.
- dimension이 다르다면 shortcut 쪽에도 변환을 하나 넣는다.
  여기서 $W_s$$는 dimension을 맞춰주는 linear projection이다. 
  → 1x1 convolution으로 구현

## 3.3 Network Architectures
<details>
<summary>Figure 3. Example network architectures for ImageNet</summary>
  
> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

</details>
여러 종류의 plain network와 residual network를 실험했고, 일관된 현상을 관찰했다.
plain baseline 설계 규칙
- convolution layer는 대부분 3x3 filter를 사용한다.
- feature map의 spatial size가 같다면 filter 수(channel 수)도 같게 유지한다.
- feature map의 가로 및 세로 크기를 절반으로 줄일 때는 filter 수를 두 배로 늘린다.
- feature map의 크기를 줄일 때 pooling만 사용하지 않고, stride 2 convolution으로 직접 downsampling한다.
Residual Network
- 34-layer plain network를 기반으로, shortcut connection만 삽입해서 residual version으로 바꾼다.
- 이로써 아예 아키텍쳐를 전부 새로 설계해서 좋아진 것이 아닌가라는 질문을 하기 어렵게 만든다.
- 기본 depth, width, 계산량을 거의 유지한 상태에서 shortcut connection의 효과를 비교하려는 실험 설계이다.
  1. Solid shortcut : dimension이 같은 때
    입력과 출력의 dimention이 같다면 그냥 identity shortcut을 쓴다.
  2. Dotted shortcut : dimension이 바뀔 때
    Option A : shortcut을 여전히 identity로 유지하고, channel이 부족한 부분을 zero-padding으로 채운다. → 추가 가중치가 없다.
    Option B : shortcut에 1x1 Convolution을 넣어 projection을 수행하는 방식이다.

## 3.4 Implementation
ImageNet에서 random scale/crop/flip 등의 data augmentation을 사용하고, 각 convolution 뒤와 activation 전에 BN을 적용했다. Plain/ResNet 모두 동일한 initialization과 SGD 조건으로 처음부터 학습했다. SGD batch size 256, initial LR 0.1, momentum 0.9, weight decay $10^{-4}$$를 사용했으며 dropout은 사용하지 않았다.

## 노트
---
- `mapping` 
  - 그냥 함수라고 생각하면 된다.
  - $x→H(x)$$
    - 이때 $H$$가 mapping이다.
  - 신경망의 어떤 블록이 입력 feature $x$$를 받아서 다음 feature $H(x)$$를 만든다면, 그 블록은 결국 어떤 함수 $H$$를 학습하고 있는 것이다.
- `identity mapping`
  - 입력을 그대로 출력하는 함수 → 아무것도 바꾸지 않는 mapping
    - $H(x)=x$$
  - ResNet에서 shortcut이 입력 $x$$를 그대로 넘기는 경우를 identity shortcut / identity mapping이라고 부른다.
- `optimization`
  - loss가 작은 parameter를 찾아가는 학습 과정
- `shortcut`
  - 중간 layer들을 건너뛰는 경로
- `plain network`
  - shortcut connection이 없는 일반적인 Deep CNN
- 논문에서의 $H(x)$$
  - 여러 layer가 전체적으로 구현하는 mapping
- `저자의 관찰`
  잘 학습된 3-layer network가 있다고 하자. (training error = 5%)<br> $x→L1→L2→L3→y$$ (shallow network라고 칭하자.)<br>이제 우리가 다음과 같이 더 깊게 만들었다고 하자. 
  $x→L1→L2→L3→L4→L5→y$$
  Q. 이전에는 깊은 layer network가 성능이 더 안 나온다고 했는데, 더 깊어진 5-layer network가 최소한 기존 3-layer network만큼은 잘할 수 있지 않을까?
  A. 그렇다. 기존 $L1,L2,L3$$ 의 weight를 그대로 복사하고, 새로 추가된 $L4,L5$$ 가 아무것도 하지 않게 만들면 되기 때문이다.
  $L4,L5:x→x$$ 
  identity mapping을 하도록 만들면 된다.
- BN (Batch Normalization)
