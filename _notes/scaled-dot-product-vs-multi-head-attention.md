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

<!-- paper-figure:attention-overview -->
<figure class="paper-figure">
  <div class="paper-figure-frame">
    <div class="paper-figure-canvas">
      <svg viewBox="0 0 760 240" role="img" aria-label="Scaled Dot-Product Attention과 Multi-Head Attention의 관계">
        <defs>
          <marker id="pa1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <path d="M0,0 L8,4 L0,8 z" fill="#7d858c"></path>
          </marker>
        </defs>
        <text x="24" y="28" class="fig-kicker">CORE RELATION</text>

        <rect x="42" y="72" width="160" height="68" rx="3" class="fig-box"></rect>
        <text x="122" y="98" class="fig-label">Q / K / V</text>
        <text x="122" y="120" class="fig-small">projected inputs</text>

        <path d="M202 106 L278 106" class="fig-arrow" marker-end="url(#pa1)"></path>

        <rect x="290" y="58" width="210" height="96" rx="3" class="fig-box-accent"></rect>
        <text x="395" y="92" class="fig-label">Scaled Dot-Product</text>
        <text x="395" y="115" class="fig-label">Attention</text>
        <text x="395" y="137" class="fig-small">core operation inside one head</text>

        <path d="M500 106 L576 106" class="fig-arrow" marker-end="url(#pa1)"></path>

        <rect x="588" y="72" width="130" height="68" rx="3" class="fig-box"></rect>
        <text x="653" y="98" class="fig-label">Head i</text>
        <text x="653" y="120" class="fig-small">one head output</text>

        <line x1="48" y1="178" x2="712" y2="178" class="fig-divider"></line>
        <text x="380" y="205" class="fig-small">Multi-Head Attention = multiple projected heads → Concat → output projection</text>
      </svg>
    </div>
  </div>
  <figcaption><strong>Figure 1.</strong> Scaled Dot-Product Attention은 head 내부의 핵심 연산이고, Multi-Head Attention은 여러 projected head를 병렬로 결합하는 구조다. Adapted conceptually from Vaswani et al. (2017).</figcaption>
</figure>

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

<!-- paper-figure:scaled-dot-product -->
<figure class="paper-figure">
  <div class="paper-figure-frame">
    <div class="paper-figure-canvas">
      <svg viewBox="0 0 760 245" role="img" aria-label="Scaled Dot-Product Attention 계산 흐름">
        <defs>
          <marker id="pa2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <path d="M0,0 L8,4 L0,8 z" fill="#7d858c"></path>
          </marker>
        </defs>
        <text x="24" y="28" class="fig-kicker">SCALED DOT-PRODUCT ATTENTION</text>

        <rect x="24" y="86" width="116" height="62" rx="3" class="fig-box"></rect>
        <text x="82" y="108" class="fig-label">QKᵀ</text>
        <text x="82" y="131" class="fig-small">similarity</text>

        <path d="M140 117 L187 117" class="fig-arrow" marker-end="url(#pa2)"></path>

        <rect x="198" y="86" width="116" height="62" rx="3" class="fig-box"></rect>
        <text x="256" y="108" class="fig-label">÷ √dₖ</text>
        <text x="256" y="131" class="fig-small">scale</text>

        <path d="M314 117 L361 117" class="fig-arrow" marker-end="url(#pa2)"></path>

        <rect x="372" y="86" width="116" height="62" rx="3" class="fig-box-accent"></rect>
        <text x="430" y="108" class="fig-label">Softmax</text>
        <text x="430" y="131" class="fig-small">weight</text>

        <path d="M488 117 L535 117" class="fig-arrow" marker-end="url(#pa2)"></path>

        <rect x="546" y="86" width="168" height="62" rx="3" class="fig-box"></rect>
        <text x="630" y="108" class="fig-label">Weight × V</text>
        <text x="630" y="131" class="fig-small">weighted value</text>

        <text x="82" y="188" class="fig-small">where should I look?</text>
        <text x="630" y="188" class="fig-small">what information should I take?</text>
      </svg>
    </div>
  </div>
  <figcaption><strong>Figure 2.</strong> Query-Key similarity를 scaling과 softmax로 attention weight로 바꾸고, 그 weight로 Value를 가중합한다.</figcaption>
</figure>


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

<!-- paper-figure:multi-head -->
<figure class="paper-figure">
  <div class="paper-figure-frame">
    <div class="paper-figure-canvas">
      <svg viewBox="0 0 760 370" role="img" aria-label="Multi-Head Attention 구조">
        <defs>
          <marker id="pa3" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <path d="M0,0 L8,4 L0,8 z" fill="#7d858c"></path>
          </marker>
        </defs>
        <text x="24" y="28" class="fig-kicker">MULTI-HEAD ATTENTION</text>

        <rect x="36" y="145" width="126" height="62" rx="3" class="fig-box"></rect>
        <text x="99" y="168" class="fig-label">Q / K / V</text>
        <text x="99" y="191" class="fig-small">input</text>

        <path d="M162 176 L222 88" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M162 176 L222 153" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M162 176 L222 218" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M162 176 L222 283" class="fig-arrow" marker-end="url(#pa3)"></path>

        <rect x="234" y="58" width="176" height="54" rx="3" class="fig-box-accent"></rect>
        <text x="322" y="79" class="fig-label">Head 1</text>
        <text x="322" y="99" class="fig-small">projection + attention</text>
        <rect x="234" y="123" width="176" height="54" rx="3" class="fig-box-accent"></rect>
        <text x="322" y="144" class="fig-label">Head 2</text>
        <text x="322" y="164" class="fig-small">projection + attention</text>
        <rect x="234" y="188" width="176" height="54" rx="3" class="fig-box-accent"></rect>
        <text x="322" y="209" class="fig-label">Head 3</text>
        <text x="322" y="229" class="fig-small">projection + attention</text>
        <rect x="234" y="253" width="176" height="54" rx="3" class="fig-box-accent"></rect>
        <text x="322" y="274" class="fig-label">Head h</text>
        <text x="322" y="294" class="fig-small">projection + attention</text>

        <path d="M410 85 L486 156" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M410 150 L486 168" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M410 215 L486 180" class="fig-arrow" marker-end="url(#pa3)"></path>
        <path d="M410 280 L486 192" class="fig-arrow" marker-end="url(#pa3)"></path>

        <rect x="498" y="147" width="102" height="58" rx="3" class="fig-box"></rect>
        <text x="549" y="176" class="fig-label">Concat</text>

        <path d="M600 176 L635 176" class="fig-arrow" marker-end="url(#pa3)"></path>

        <rect x="646" y="147" width="78" height="58" rx="3" class="fig-box-soft"></rect>
        <text x="685" y="168" class="fig-label">Wᴼ</text>
        <text x="685" y="190" class="fig-small">Linear</text>

        <text x="380" y="340" class="fig-small">Different heads learn different representation subspaces.</text>
      </svg>
    </div>
  </div>
  <figcaption><strong>Figure 3.</strong> 각 head는 서로 다른 Q/K/V projection을 학습하고, 결과를 concatenate한 뒤 output projection으로 결합한다.</figcaption>
</figure>


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

<section class="related-notes" aria-labelledby="related-notes-title">
  <h2 id="related-notes-title">Related Notes</h2>
  <div class="related-notes-list">
    <a class="related-note-link" href="/notes/attention-is-all-you-need-2017/"><strong>Attention Is All You Need (2017)</strong><span>Transformer 전체 encoder-decoder 구조와 attention 적용 위치를 함께 보기.</span></a>
  </div>
</section>

## References

- [Vaswani et al. — Attention Is All You Need](https://arxiv.org/abs/1706.03762)
