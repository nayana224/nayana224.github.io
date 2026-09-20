---
layout: note
title: "Scaled Dot-Product Attention과 Multi-Head Attention은 무엇이 다른가"
date: 2026-09-21
library_type: concept
category: Concepts & Theory
category_ko: 개념 & 이론
category_en: Concepts & Theory
topic: Transformer
topic_ko: Transformer
topic_en: Transformer
summary: "Attention head 하나의 내부 계산과 Multi-Head Attention의 projection·병렬 처리 구조를 Q/K/V 관점에서 구분합니다."
source_language: ko
---

<div class="note-callout note-callout-primary">
  <strong>핵심 요약</strong>
  <p><b>Scaled Dot-Product Attention</b>은 하나의 Q, K, V로 attention을 계산하는 핵심 연산이고, <b>Multi-Head Attention</b>은 Q, K, V를 여러 projection 공간으로 나눈 뒤 이 연산을 여러 head에서 병렬로 수행하고 다시 합치는 구조다.</p>
</div>

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">CORE OPERATION</span>
    <h3>Scaled Dot-Product Attention</h3>
    <p>하나의 Q, K, V 집합을 받아 attention weight와 weighted sum을 계산한다.</p>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">ARCHITECTURE</span>
    <h3>Multi-Head Attention</h3>
    <p>여러 projection된 Q/K/V에 Scaled Dot-Product Attention을 각각 적용하고 결과를 합친다.</p>
  </div>
</div>

둘은 같은 개념이 아니다.

보통 Transformer 그림에서 하나의 <b>head</b> 안에는 Scaled Dot-Product Attention 연산이 들어가고, Multi-Head Attention은 그런 head 여러 개를 병렬로 사용하는 더 큰 구조다.

---

## 1. 먼저 Q, K, V를 구분하자

<div class="concept-grid">
  <div class="concept-card">
    <span class="concept-kicker">QUERY</span>
    <h3>Q</h3>
    <p>현재 위치가 <b>무엇을 찾고 싶은가</b>를 표현한다.</p>
  </div>
  <div class="concept-card">
    <span class="concept-kicker">KEY</span>
    <h3>K</h3>
    <p>각 위치가 <b>어떤 정보를 가지고 있는가</b>를 비교하기 위한 표현이다.</p>
  </div>
  <div class="concept-card">
    <span class="concept-kicker">VALUE</span>
    <h3>V</h3>
    <p>attention weight가 정해진 뒤 실제로 <b>가져올 정보</b>를 담는다.</p>
  </div>
  <div class="concept-card">
    <span class="concept-kicker">ATTENTION</span>
    <h3>Q ↔ K → V</h3>
    <p>Q와 K로 중요도를 구하고, 그 중요도로 V를 가중합한다.</p>
  </div>
</div>

---

## 2. Scaled Dot-Product Attention

핵심 식은 다음과 같다.

\\[
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
\\]

이 식은 네 단계로 볼 수 있다.

<div class="hierarchy-block">
  <div class="hierarchy-level">
    <span class="hierarchy-label">STEP 1</span>
    <strong>Q와 K의 dot product</strong>
    <p>각 query가 각 key와 얼마나 관련 있는지 score를 계산한다.</p>
  </div>
  <div class="hierarchy-level">
    <span class="hierarchy-label">STEP 2</span>
    <strong>\\(\sqrt{d_k}\\)로 scaling</strong>
    <p>차원이 커질수록 dot product가 지나치게 커지는 것을 완화한다.</p>
  </div>
  <div class="hierarchy-level">
    <span class="hierarchy-label">STEP 3</span>
    <strong>Softmax</strong>
    <p>score를 attention weight로 바꾼다.</p>
  </div>
  <div class="hierarchy-level">
    <span class="hierarchy-label">STEP 4</span>
    <strong>V의 weighted sum</strong>
    <p>중요도가 높은 value 정보를 더 많이 가져온다.</p>
  </div>
</div>

<div class="pipeline-row">
  <div class="pipeline-node">QKᵀ</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Scale by √dₖ</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Softmax</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">× V</div>
</div>

즉 Scaled Dot-Product Attention은 **attention 한 번의 계산 방법**이다.

---

## 3. 그렇다면 Head는 무엇인가

하나의 head는 단순히 원본 embedding 전체를 그대로 Scaled Dot-Product Attention에 넣는 것이 아니다.

먼저 입력 representation을 서로 다른 learned projection으로 바꾼다.

\\[
Q_i = QW_i^Q
\\]

\\[
K_i = KW_i^K
\\]

\\[
V_i = VW_i^V
\\]

그리고 projection된 \\(Q_i, K_i, V_i\\)로 Scaled Dot-Product Attention을 수행한다.

\\[
\operatorname{head}_i
=
\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V)
\\]

<div class="flow-diagram">
  <div class="flow-step">Input Representation</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Linear Projection<small>WᵢQ · WᵢK · WᵢV</small></div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Projected Qᵢ / Kᵢ / Vᵢ</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Scaled Dot-Product Attention</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Head i Output</div>
</div>

따라서 다음처럼 생각하면 된다.

<div class="note-callout">
  <strong>Head 하나 = Projection + Scaled Dot-Product Attention</strong>
  <p>Scaled Dot-Product Attention 자체와 head는 완전히 같은 말이 아니다. Head에는 그 attention을 수행하기 전에 각자의 Q/K/V projection이 포함된다.</p>
</div>

---

## 4. Multi-Head Attention

Multi-Head Attention은 이런 head를 여러 개 병렬로 만든다.

\\[
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}
(
\operatorname{head}_1,
\ldots,
\operatorname{head}_h
)W^O
\\]

<div class="flow-diagram">
  <div class="flow-step">Input Q / K / V</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">여러 개의 Q/K/V Linear Projection</div>
  <div class="flow-arrow">↓</div>
  <div class="concept-grid">
    <div class="concept-card"><h3>Head 1</h3><p>Scaled Dot-Product Attention</p></div>
    <div class="concept-card"><h3>Head 2</h3><p>Scaled Dot-Product Attention</p></div>
    <div class="concept-card"><h3>Head 3 ... h</h3><p>각기 다른 projection 공간</p></div>
    <div class="concept-card"><h3>Parallel</h3><p>각 head는 동시에 계산 가능</p></div>
  </div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Concat</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-step">Output Linear Projection Wᴼ</div>
</div>

각 head는 서로 다른 projection matrix를 학습한다.

따라서 같은 token sequence를 보더라도 각 head가 **서로 다른 representation subspace에서 관계를 볼 수 있다.**

---

## 5. Projection은 무엇을 의미하는가

여기서 projection은 물리적인 투영이 아니라, learned linear transformation으로 representation을 다른 좌표 공간으로 바꾸는 것을 의미한다.

\\[
X' = XW
\\]

예를 들어 원래 embedding이 \\(d_{model}=512\\) 차원이고 head가 8개라면, 원 논문에서는 각 head의 차원을 보통 다음처럼 둔다.

\\[
d_k=d_v=\frac{d_{model}}{h}
=
\frac{512}{8}
=
64
\\]

<div class="compare-grid">
  <div class="compare-card">
    <span class="concept-kicker">BEFORE</span>
    <h3>512-d representation</h3>
    <p>원래 Transformer hidden representation</p>
  </div>
  <div class="compare-card">
    <span class="concept-kicker">EACH HEAD</span>
    <h3>64-d subspace</h3>
    <p>각 head가 자기 projection matrix로 만든 별도의 표현 공간</p>
  </div>
</div>

Projection이 있기 때문에 모든 head가 완전히 같은 Q/K/V를 보는 것이 아니다.

---

## 6. Head가 많아지면 parameter도 늘어나는가

각 head에는 \\(W_i^Q\\), \\(W_i^K\\), \\(W_i^V\\) 같은 learned weight가 존재한다.

따라서 projection layer 자체에는 학습 parameter가 있다.

하지만 head를 8개 쓴다고 단순히 계산량이 8배가 되는 것은 아니다.

원 논문의 일반적인 설정에서는 각 head의 차원을 \\(d_{model}/h\\)로 줄여 전체 attention 계산량이 full-dimensional single-head attention과 비슷한 수준이 되도록 구성한다.

<div class="note-callout">
  <strong>중요한 직관</strong>
  <p>Head 수를 늘리는 목적은 같은 계산을 8번 복제하는 것이 아니라, <b>전체 representation을 여러 subspace로 나눠 서로 다른 관계를 병렬로 학습</b>하는 데 있다.</p>
</div>

---

## 7. 왜 Multi-Head가 필요한가

Single attention은 하나의 attention distribution으로 정보를 모은다.

Multi-Head Attention은 여러 representation subspace에서 동시에 관계를 볼 수 있다.

예를 들어 문장 안에서 각 head가 반드시 이렇게 역할 분담한다고 보장할 수는 없지만, 직관적으로는 다음과 같은 서로 다른 관계를 학습할 수 있다.

<div class="concept-grid">
  <div class="concept-card"><h3>Local Relation</h3><p>가까운 token 사이의 관계</p></div>
  <div class="concept-card"><h3>Long-range Relation</h3><p>멀리 떨어진 token 사이 dependency</p></div>
  <div class="concept-card"><h3>Syntactic Pattern</h3><p>문법적 연결이나 구조</p></div>
  <div class="concept-card"><h3>Semantic Relation</h3><p>의미적으로 관련 있는 token 연결</p></div>
</div>

핵심은 **하나의 attention map에 모든 관계를 압축하지 않는 것**이다.

---

## 8. 전체 구조를 한 번에 보면

<div class="pipeline-row">
  <div class="pipeline-node">Input</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Q/K/V Projection</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Multiple Heads</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Concat</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Wᴼ</div>
</div>

각 head 내부는 다시 다음과 같다.

<div class="pipeline-row">
  <div class="pipeline-node">Projected Q/K/V</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">QKᵀ</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Scale</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Softmax</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Weighted V</div>
</div>

---

## 정리

| 개념 | 역할 |
| --- | --- |
| **Scaled Dot-Product Attention** | Q/K similarity를 계산하고 V를 weighted sum하는 핵심 연산 |
| **Projection** | learned linear transformation으로 Q/K/V 표현 공간을 바꿈 |
| **Head** | 자기 projection된 Q/K/V에 Scaled Dot-Product Attention을 수행하는 단위 |
| **Multi-Head Attention** | 여러 head를 병렬로 계산하고 concat한 뒤 다시 projection |
| **\\(W^O\\)** | 여러 head 결과를 다시 하나의 output representation으로 변환 |

<div class="note-callout note-callout-primary">
  <strong>한 문장으로</strong>
  <p><b>Scaled Dot-Product Attention은 head 내부의 핵심 연산이고, Multi-Head Attention은 서로 다른 projection을 가진 여러 head를 병렬로 묶은 구조다.</b></p>
</div>

## References

- [Vaswani et al. — Attention Is All You Need](https://arxiv.org/abs/1706.03762)
