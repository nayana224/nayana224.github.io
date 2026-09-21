---
layout: note
title: "Attention Is All You Need (2017) 논문 정리"
title_ko: "Attention Is All You Need (2017) 논문 정리"
title_en: "Attention Is All You Need (2017) Paper Notes"
date: 2026-09-18
category: Papers
category_ko: 논문
category_en: Papers
topic: "Transformer"
topic_ko: "Transformer"
topic_en: "Transformer"
library_type: papers
summary: "Transformer encoder-decoder, Scaled Dot-Product Attention, Multi-Head Attention과 Q/K/V 구조를 중심으로 정리한 노트."
summary_ko: "Transformer encoder-decoder, Scaled Dot-Product Attention, Multi-Head Attention과 Q/K/V 구조를 중심으로 정리한 노트."
summary_en: "Notes on the Transformer encoder-decoder, scaled dot-product attention, multi-head attention, and Q/K/V."
source: Notion
source_language: ko
---

<p class="figure-note"><strong>Original paper:</strong> <a href="https://arxiv.org/abs/1706.03762">Vaswani et al., Attention Is All You Need (2017)</a></p>

<!-- visual-summary:v1 -->
<div class="note-callout note-callout-primary">
  <strong>핵심 아이디어</strong>
  <p>RNN의 순차 recurrence를 제거하고, <b>self-attention으로 token 사이 dependency를 직접 연결</b>해 sequence modeling을 병렬화한다.</p>
</div>

<div class="pipeline-row">
  <div class="pipeline-node">Tokens</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Embedding + Position</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Multi-Head Attention</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Feed Forward</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Contextual Representation</div>
</div>

<div class="concept-grid">
  <div class="concept-card"><h3>Q</h3><p>현재 token이 무엇을 찾고 싶은지 표현한다.</p></div>
  <div class="concept-card"><h3>K</h3><p>각 token이 어떤 정보를 가지고 있는지 비교 기준을 제공한다.</p></div>
  <div class="concept-card"><h3>V</h3><p>attention weight에 따라 실제로 전달될 정보를 담는다.</p></div>
  <div class="concept-card"><h3>Multi-Head</h3><p>여러 projection 공간에서 서로 다른 관계를 병렬로 본다.</p></div>
</div>


왜 RNN/CNN을 버리고 attention만으로도 sequence modeling이 가능한가?
ViT, SAM, DINOv2, ACT까지 이어지는 기반 논문이다.


<!-- paper-figure:transformer-overview -->
<figure class="paper-figure">
 <div class="paper-figure-frame"><div class="paper-figure-canvas">
 <svg viewBox="0 0 760 355" role="img" aria-label="Transformer encoder decoder overview">
  <defs><marker id="trA" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#7d858c"/></marker></defs>
  <text x="24" y="28" class="fig-kicker">TRANSFORMER OVERVIEW</text>
  <rect x="70" y="260" width="150" height="54" rx="3" class="fig-box"/><text x="145" y="287" class="fig-label">Input tokens</text>
  <rect x="540" y="260" width="150" height="54" rx="3" class="fig-box"/><text x="615" y="287" class="fig-label">Output tokens</text>
  <path d="M145 260 L145 214" class="fig-arrow" marker-end="url(#trA)"/><path d="M615 260 L615 214" class="fig-arrow" marker-end="url(#trA)"/>
  <rect x="65" y="88" width="160" height="112" rx="3" class="fig-box-accent"/><text x="145" y="116" class="fig-label">Encoder × N</text><text x="145" y="145" class="fig-small">Self-Attention</text><text x="145" y="168" class="fig-small">Feed Forward</text>
  <rect x="535" y="70" width="160" height="148" rx="3" class="fig-box-accent"/><text x="615" y="98" class="fig-label">Decoder × N</text><text x="615" y="128" class="fig-small">Masked Self-Attention</text><text x="615" y="151" class="fig-small">Cross-Attention</text><text x="615" y="174" class="fig-small">Feed Forward</text>
  <path d="M225 144 L520 144" class="fig-arrow-accent" marker-end="url(#trA)"/>
  <text x="374" y="130" class="fig-small">encoder representation → K, V</text>
  <text x="372" y="328" class="fig-small">attention replaces recurrence; position information is added explicitly</text>
 </svg></div></div>
 <figcaption><strong>Figure 1.</strong> Transformer는 recurrence 없이 encoder-decoder를 attention 중심으로 구성하며, decoder는 encoder output을 cross-attention으로 참조한다. Adapted from Vaswani et al. (2017).</figcaption>
</figure>

## Abstract
기존의 대표적인 sequence transduction 모델들은 대부분 encoder와 decoder를 포함하는 복잡한 RNN 또는 CNN를 기반으로 한다. 성능이 좋은 모델들은 여기에 더해 attention mechanism을 사용하여 encoder와 decoder를 연결한다.
Transformer는 RNN과 CNN을 제거하고 attention만으로 sequence를 처리함으로써, 더 높은 병렬성과 짧은 학습 시간, 그리고 더 좋은 성능을 달성한 모델이다.

## 1. Introduction
RNN 기반 sequence model은 hidden state를 순차적으로 계산해야 해서 병렬화에 근본적인 제약이 있고, Transformer는 `recurrence를 제거하고 attention만으로 global dependency를 직접 modeling하여 이 병목을 해결`하려 한다.

## 2. Background
기존 CNN 기반 sequence model도 RNN의 순차 계산 문제는 줄였지만, 먼 위치 사이의 정보 전달에는 여러 연산 단계가 필요했다. Transformer는 self-attention을 통해 모든 위치를 직접 연결하여 long-range dependency를 더 짧은 path로 학습한다.
- Path length : 한 token의 정보가 다른 token까지 전달되기 위해 몇 번의 연산 단계를 거쳐야 하는가

## 3. Model Architecture
대부분의 경쟁력 있는 neural sequence transduction 모델은 encoder-decoder 구조를 가진다. 
- encoder 입력 sequence의 symbol 표현
  \\[
(x_1,…,x_n)
\\]
- 입력 sequence를 연속적인 representation sequence로 변환
  \\[
z=(z_1,\ldots,z_n)
\\]
- decoder는 위 \\(z\\) 를 이용하여 출력 sequence를 한 번에 하나의 symbol씩 생성한다.
  \\[
(y_1,\ldots,y_m)
\\]
각 step에서 모델은 autoregressive(자기회귀)하게 동작한다. 즉, 다음 출력을 생성할 때 이전에 생성한 output symbol들을 추가 입력으로 사용한다.

Transformer도 이 encoder-decoder 틀 자체를 유지한다.
차이는 encoder와 decoder 내부를 stacked self-attention + point-wise fully connected layer로 구성한다는 점이다. 이 구조가 Figure 1의 왼쪽 encoder, 오른쪽 decoder에 나와 있다.

## Figure 1 전체 구조

> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

### 1) Encoder 쪽
입력은 다음과 같이 흐른다.
```python
Input tokens 

→ Input Embedding 

→ Positional Encoding 추가 

→ Multi-Head Self-Attention 

→ Add & Norm 

→ Feed Forward 

→ Add & Norm
```
이 block이 N번 반복된다. 논문에서는 \\(N=6\\) 이다. 
즉 encoder는 동일한 형태의 layer를 6개 쌓은 구조다.

### 2) Decoder 쪽
decoder는 encoder보다 sub-layer가 하나 더 있다.
```python
Output tokens shifted right

→ Output Embedding

→ Positional Encoding 

→ Masked Multi-Head Self-Attention 

→ Add & Norm 

→ Multi-head Attention with Encoder Ouput

→ Add & Norm

→ Feed Forward 

→ Add & Norm
```
이것도 \\(N=6\\) 번 반복된다.
마지막에는 \\(Linear → Softmax\\) 를 거쳐 다음 token의 확률을 출력한다. 

### 3) Encoder와 Decoder의 차이
가장 중요한 차이는 decoder에는 attention이 두 종류가 있다는 것이다.
Encoder에서는 Self-Attention, Decoder에서는 Masked Self-Attention 그리고 Encoder-Decoder Attention이 두 개가 있다.
즉 decoder 다음과 같이 이해하면 된다.
1. 지금까지 생성한 output끼리 보고
2. encoder가 만든 input representation도 본다.

### 4) 왜 output이 shifted right인가?
Figure 1 아래쪽 decoder를 보면 Outputs(shifted right)라고 되어 있다.
이유는 autoregressive prediction 때문이다.
예를 들어, 정답이 \\([I, love, you]\\) 라면 decoder 입력은 대략 \\([<start>, I, love]\\) 가 된다.
정답 target은 \\([I, love, you]\\) 가 된다.
즉 `decoder는 항상 다음 token을 예측`한다.
> Transformer는 기존 encoder-decoder seq2seq 틀은 유지하되, encoder와 decoder 내부의 recurrent layer를 self-attention과 feed-forward network로 대체한 구조이다.

> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

→  **LSTM이 시간축을 따라 순차적으로 처리하던 역할을 Transformer의 attention 기반 block이 대신한다**
Ex)
\\(I→LSTM→study→LSTM→math→⋯\\) 구조를
\\(tokens→Self-Attention→FFN\\) 구조로 바꾼 것이다.
Transformer의 self-attention은 `"I", "study", "math", "hard"`를 **한꺼번에 넣고**, 각 token이 다른 모든 token을 바라보게 한다.

## 3.1 Encoder and Decoder Stacks
### 1) Encoder
`입력 문장 내부 관계를 본다.`
동일한 layer \\(N=6\\) 개를 쌓은 구조다.
각 encoder layer는 두 개의 sub-layer를 가진다.
1. Multi-Head Self-Attention
2. Position-wise Feed-Forward Network
그리고 sub-layer 주변에는 residual connection을 사용하고, 그 뒤에 Layer Normalization을 적용한다.
즉, 각 sub-layer의 출력은 다음과 같다.
\\[
\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))
\\]
여기서 `Sublayer(x)` 는 attention 또는 feed-forward 연산을 의미한다.
Residual connection을 적용하려면 입력과 출력 자원이 같아야 하므로, embedding과 모든 sub-layer의 출력 차원은 \\(d_{model} = 512\\) 로 맞춘다.
\\[
x\to\text{Multi-Head Self-Attention}\to\text{Add \& Norm}\to\text{FFN}\to\text{Add \& Norm}
\\]

### 2) Decoder
`자기 자신 쪽 output sequence를 보는 attention(Masked Self-Attention)과 encoder가 만든 입력 정보와 연결하는 attenion(Encoder-Decoder Attention)이 있다.`
동일한 layer \\(N=6\\) 개를 쌓은 구조다.
다만 encoder와 달리 각 decoder layer에는 sub-layer가 하나 더 있어서 총 3개다.
1. Masked Multi-Head Attention
2. Encoder output에 대한 Multi-Head Attention
3. Position-wise Feed-Forward Network
여기에도 각 sub-layer마다 residual connection과 LazyNorm을 적용한다.
그리고 decoder의 self-attention은 미래 위치를 볼 수 없도록 수정한다.
즉 postion \\(i\\) 에서 예측할 때는 \\(1, …, i-1\\) 위치까지만 참고할 수 있고 \\(i+1, …\\) 같은 미래 token은 볼 수 없다. 
이 masking과 ouput embedding을 한 칸 오른쪽으로 shift하는 것을 함께 사용해서, decoder가 auto-regressive하게 다음 token을 예측하도록 만든다.
\\[
y \rightarrow \text{Masked Self-Attention} \rightarrow \text{Add \& Norm} \rightarrow \text{Encoder-Decoder Attention} \rightarrow \text{Add \& Norm} \rightarrow \text{FFN} \rightarrow \text{Add \& Norm}
\\]

> **Encoder = Self-Attention + FFN**
> **Decoder = Masked Self-Attention + Encoder-Decoder Attention + FFN**
⇒ `둘다 Residual + LayerNorm을 붙인다.`

## 3.2 Attention
논문은 attention을 다음과 같이 정의한다.
> Query와 Key-Value 쌍들을 입력으로 받아 하나의 output을 만드는 함수
여기서 Query, Key, Value, Output은 모두 vector이다.
출력은 여러 Value의 weighted sum으로 만들어지고, 각 Value에 얼마의 weight를 줄지는 해당 Query와 Key가 얼마나 잘 맞는지를 보고 결정한다.
- Query : 내가 지금 어떤 정보를 찾고 싶은가?
- Key : 나는 어떤 정보를 가지고 있는가?
- Value : Query와 Key의 유사도를 보고 Value의 정보를 얼마나 가져올지 정한다.
```python
1. Query (질의)      : "로봇 궤적 계획에 대한 책 찾아줘" (질문)
                            │
                            ▼ [내적 비교: Q · K]
2. Key (도서 라벨)   : 서가에 꽂힌 수만 권의 [책 제목/키워드 라벨]과 일치도 비교
                            │
                            ▼ [Softmax: Attention Weight]
                      일치도 확률: 책 A (85%), 책 B (12%), 책 C (3%)
                            │
                            ▼ [가중합: Weight × V]
3. Value (책의 내용) : 책 A의 내용을 85%, 책 B를 12%만큼 뽑아와 요약본 작성
                            │
                            ▼
4. Output (출력)     : 질문(Query)에 딱 맞춤형으로 추출된 새로운 지식 벡터
```

## 3.2.1 Scaled Dot-Product Attention

> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

이 논문이 사용하는 attention은 Scaled Dot-Product Attention이다.
입력은 다음과 같다. 
- Query : \\(Q\\)
- Key : \\(K\\)
- Value: \\(V\\)
Query와 Key의 차원은 \\(d_k\\) 이고, Value의 차원은 \\(d_v\\) 이다.

계산식은 다음과 같다.

\\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\\]

### 1) \\(QK^T\\)
먼저 Query와 모든 Key 사이의 dot product를 계산한다.
\\[
QK^T
\\]
이 값은 `Query와 각 Key가 얼마나 잘 맞는가를 나타내는 score`이다.
예를 들어, `“math”` 라는 token이 다른 token들과 얼마나 관계 있는지를 계산한다고 생각할 수 있다.
\\]
\text{math query} \cdot \text{I key} \\
\text{math query} \cdot \text{study key} \\
\text{math query} \cdot \text{math key} \\
\text{math query} \cdot \text{hard key}
\\[
이런 score들이 한꺼번에 나온다.

### 2) \\(\sqrt{d_k}\\) 로 나눈다.
\\]
\frac{QK^T}{\sqrt{d_k}}
\\[
저자들은 \\(d_k\\) 가 커지면 dot product의 크기도 커질 수 있다고 설명한다.
논문에서는 q와 k의 성분이 평균 0, 분산 1인 독립 확률 변수라고 가정하면,
\\]
q \cdot k = \sum_{i=1}^{d_k} q_i k_i
\\[
의 분산이 \\(d_k\\)가 된다고 설명한다.
즉, 차원이 커질수록 dot product 값이 커질 가능성이 있다.
그러면 softmax에 큰 값들이 들어가면서 출력이 지나치게 한쪽으로 몰리고, gradient가 매우 작아질 수 있다. 그래서  \\(\sqrt{d_k}\\) 로 나눠서 scale을 조절한다.

### 3) Softmax
그 다음 \\(softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)\\) 를 적용한다.
이제 score들이 attention weight가 된다.
예를 들어 임의로 \\[0.1, 0.6, 0.2, 0.1\\]이 나왔다면
`“math”`가
- `"I"` → 10%
- `"study"` → 60%
- `"math"` → 20%
- `"hard"` → 10%
정도의 비중으로 정보를 본다고 이해할 수 있다.
실제 수치는 학습으로 결정된다.

### 4) 마지막으로 \\(V\\)와 곱한다.
\\[
\\operatorname{softmax}(\\cdot)V
\\]
attention weight를 이용해서 `Value들을 weighted sum`한다.
- weighted sum : 각 값의 중요도나 관련성에 따라 가중치(Weight)를 각각 곱한 뒤 모두 더하는 연산
예를 들어 다음과 같은 식이다.
\\[
0.1V_1+0.6V_2+0.2V_3+0.1V_4
\\]
그래서 최종적으로 `“math”`의 새로운 representation에는 다른 token들의 정보가 섞여 들어간다.

### 5) 왜 그냥 dot-product attention이 아니라 “Scaled”인가
논문은 기존에 많이 쓰이던 attention으로 Additive attention, Dot-product attention을 언급한다.
Dot-product attention은 계산 효율이 좋다. 특히 matrix multiplication으로 구현할 수 있어 빠르고 메모리 효율이 좋다.
하지만 \\(d_k\\) 가 커지면 dot product가 커질 수 있어 softmax gradient 문제가 생길 수 있다.
그래서 Transformer에서는 \\(\frac{QK^T}{\sqrt{d_k}}\\) 를 곱한 것이다.
\\]
QK^T \rightarrow Scale \rightarrow Softmax \rightarrow V
\\[
> Query와 Key의 관계를 계산하고 → 값이 너무 커지지 않도록 scale하고 → softmax로 중요도를 만들고 → 그 중요도로 Value들을 합친다.

## 3.2.2 Multi-Head Attention

> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.

논문은 하나의 attention만 쓰는 대신, `Query/Key/Value를 여러 번 서로 다른 선형 변환(Linear Block)으로 투영한 뒤 여러 attention head를 병렬로 계산`하는 것이 더 좋다고 설명한다.
형태는 다음과 같다.
\\]
\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\mathrm{head}_1,\ldots,\mathrm{head}_h)W^O
\\[
각 Head는 다음과 같다.
\\]
\mathrm{head}_i=\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V)
\\[
즉, 다른 입력을 보더라도 각 head는 서로 다른 projection을 거쳐서 서로 다른 관점에서 관계를 본다고 이해하면 된다.

### 1) 왜 여러 head를 쓰는가
single-head attention 하나만 쓰면 여러 관계를 하나의 attention 공간에서 평균적으로 처리하게 된다. 
논문은 `Multi-Head Attention을 쓰면 모델이 서로 다른 위치의 정보와 서로 다른 representation subspace를 동시에 볼 수 있다고 설명`한다.
Ex) 한 문장이 다음과 같이 있다고 하자. 
> `I study math hard`
직관적인 예시로 다음처럼 각 head가 서로 다른 관계를 학습할 수 있다.
- Head 1 →문법적 관계
- Head 2 →멀리 떨어진 단어 관계
- Head 3 → 의미적으로 관련된 단어
- Head 4 → 다른 종류의 패턴

핵심은 같은 `sequence를 서로 다른 representation 공간에서 동시에 본다`는 것이다.

### 2) 차원은 어떻게 되는가
논문에선 \\(h=8\\) 개의 head를 사용한다.
전체 모델 차원은 \\(d_{model}=512\\) 이고 각 head에서는 \\(d_k=d_v=\frac{512}{8}=64\\) 를 사용한다.
즉, \\(512→8×64\\) 로 각 head가 attention을 계산하고, 그 결과를 다시 이어 붙이면 \\(8×64=512\\) 가 된다.
그래서 최종적으로 원래  \\(d_{model}=512\\) 차원으로 돌아온다.

head를 8개 쓴다고 계산량이 무조건 8배가 되는 구조는 아니다. 각 head의 차원을 \\(512→64\\) 로 줄여서 계산하기 때문에, 논문에서는 전체 계산 비용이 full-dimensional single-head attention과 비슷한 수준이라고 설명한다.

## 3.2.3 Application in our Model
### 1) Encoder Self-Attention
Encoder의 self-attention에서는 \\(Q, K, V\\) 가 전부 같은 곳, 즉 이전 encoder layer 출력에서 나온다.
그래서 각 입력 token은 encoder의 다른 모든 input token을 볼 수 있다.
Ex) 입력이 \\([I, study, math, hard]\\) 라면 `"math"` 위치는 `"I"`, `"study"`, `"math"`, `"hard"` 전부를 참고할 수 있다.

\\[
Q=K=V=\text{encoder previous layer output}
\\]

### 2) Decoder Masked Self-Attention
Decoder에서도 `self-attention을 쓰지만, 미래 token을 볼 수 없도록 mask를 건다.` (causal mask)
Ex) 현재 세 번째 token을 예측하는 위치라면, \\(1, 2, 3\\) 위치는 볼 수 있지만 \\(4, 5, …\\) 는 볼 수 없다.
논문에서는 softmax 입력에서 허용되지 않는 연결을 \\(−∞\\) 로 설정하여, softmax 이후 weight가 사실상 0이 되도록 한다.
\\(Q, K, V\\) 는 decoder 내부의 같은 representation에서 나온다.
다만 causal mask가 추가된다는 점이 다르다.
**미래 위치에 해당하는 원소들을 전부 \\( -\\infty \\)로 덮어씌운다.**
\\]
\text{Attention Matrix}=\begin{bmatrix}S_{11}&-\infty&-\infty&-\infty\\S_{21}&S_{22}&-\infty&-\infty\\S_{31}&S_{32}&S_{33}&-\infty\\S_{41}&S_{42}&S_{43}&S_{44}\end{bmatrix}
\\[
### 3) Encoder-Decoder Attention
이게 self-attention과 가장 다른 부분이다.
여기서는 \\(Q\\) 는 decoder쪽에서 오고, \\(K, V\\) 는 encoder의 최종 출력에서 나온다.

\\[
Q=\text{decoder representation}, \quad K,V=\text{encoder output}
\\]

직관적으로 보면 decoder가 “내가 지금 다음 단어를 만들려고 하는데, 입력 문장에서 어떤 부분을 봐야하지?” 라고 묻는 구조다.
<table>

<tr>
<td>Attention 종류</td>
<td>\\(Q\\) 출처</td>
<td>\\(K,V\\) 출처</td>
<td>목적</td>
</tr>
<tr>
<td>Encoder Self-Attention</td>
<td>Encoder</td>
<td>Encoder</td>
<td>입력 token끼리 관계 파악</td>
</tr>
<tr>
<td>Decoder Masked Self-Attention</td>
<td>Decoder</td>
<td>Decoder</td>
<td>지금까지 생성된 출력끼리 관계 파악</td>
</tr>
<tr>
<td>Encoder-Decoder Attention</td>
<td>Decoder</td>
<td>Encoder</td>
<td>출력이 입력의 어떤 부분을 볼지 결정</td>
</tr>
</table>
> Self-attention은 Q/K/V가 같은 sequence에서 오고, cross-attention은 Q와 K/V의 출처가 다르다.

> **Figure placeholder** — Notion의 임시 이미지 URL은 제외했습니다. 필요 시 GitHub asset으로 추가합니다.
