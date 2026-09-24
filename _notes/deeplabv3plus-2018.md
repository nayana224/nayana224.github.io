---
layout: note
title: "DeepLabV3+ (2018) 논문 정리"
title_ko: "DeepLabV3+ (2018) 논문 정리"
title_en: "DeepLabV3+ (2018) Paper Notes"
date: 2026-09-18
category: Papers
category_ko: 논문
category_en: Papers
topic: "Computer Vision"
topic_ko: "컴퓨터 비전"
topic_en: "Computer Vision"
library_type: papers
blog_category: "Paper Study"
summary: "Atrous convolution, ASPP, encoder-decoder, depthwise separable convolution을 중심으로 DeepLabV3+를 정리한 노트."
summary_ko: "Atrous convolution, ASPP, encoder-decoder, depthwise separable convolution을 중심으로 DeepLabV3+를 정리한 노트."
summary_en: "Notes on atrous convolution, ASPP, encoder-decoder design, and depthwise separable convolution in DeepLabV3+."
source: Notion
source_language: ko
---

<p class="figure-note"><strong>Original paper:</strong> <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">Chen et al., Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation (ECCV 2018)</a></p>

<!-- visual-summary:v1 -->
<div class="note-callout note-callout-primary">
  <strong>핵심 아이디어</strong>
  <p><b>ASPP의 multi-scale context</b>와 <b>encoder-decoder의 boundary recovery</b>를 결합해 semantic segmentation의 두 요구를 동시에 잡는다.</p>
</div>

<div class="compare-grid">
  <div class="compare-card"><span class="concept-kicker">CONTEXT</span><h3>ASPP</h3><p>여러 atrous rate로 같은 feature를 서로 다른 receptive field에서 본다.</p></div>
  <div class="compare-card"><span class="concept-kicker">DETAIL</span><h3>Decoder</h3><p>low-level spatial feature와 high-level semantic feature를 합쳐 boundary를 정교화한다.</p></div>
</div>

<div class="pipeline-row">
  <div class="pipeline-node">Backbone</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Atrous Conv</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">ASPP</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Decoder + Low-level Feature</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-node">Segmentation</div>
</div>



<!-- paper-figure:deeplab-overview -->
<figure class="paper-figure">
 <div class="paper-figure-frame"><div class="paper-figure-canvas">
 <svg viewBox="0 0 760 300" role="img" aria-label="DeepLabV3 Plus overview">
  <defs><marker id="dlA" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#7d858c"/></marker></defs>
  <text x="24" y="28" class="fig-kicker">DEEPLABV3+ OVERVIEW</text>
  <rect x="30" y="105" width="120" height="60" rx="3" class="fig-box"/><text x="90" y="135" class="fig-label">Input</text>
  <path d="M150 135 L210 135" class="fig-arrow" marker-end="url(#dlA)"/>
  <rect x="222" y="92" width="140" height="86" rx="3" class="fig-box-accent"/><text x="292" y="121" class="fig-label">Backbone</text><text x="292" y="146" class="fig-small">atrous feature extraction</text>
  <path d="M362 120 L425 82" class="fig-arrow" marker-end="url(#dlA)"/>
  <rect x="438" y="48" width="130" height="68" rx="3" class="fig-box-accent"/><text x="503" y="72" class="fig-label">ASPP</text><text x="503" y="94" class="fig-small">multi-scale context</text>
  <path d="M568 82 L626 112" class="fig-arrow" marker-end="url(#dlA)"/>
  <rect x="618" y="120" width="112" height="62" rx="3" class="fig-box"/><text x="674" y="151" class="fig-label">Decoder</text>
  <path d="M292 178 C292 240, 600 240, 645 182" class="fig-arrow-accent" marker-end="url(#dlA)"/>
  <text x="456" y="257" class="fig-small">low-level spatial feature → boundary refinement</text>
  <text x="504" y="207" class="fig-small">semantic context + spatial detail</text>
 </svg></div></div>
 <figcaption><strong>Figure 1.</strong> DeepLabV3+는 ASPP의 multi-scale context와 decoder의 boundary refinement를 결합한다. Adapted from Chen et al. (2018).</figcaption>
</figure>

## Summary
  ---
  1. **Problem**<br>semantic segmentation에서 강한 semantic context와 정확한 boundary를 동시에 얻기 어렵다.
  2. **Core idea**<br>DeepLabV3의 multi-scale context 능력과 encoder-decoder의 spatial detail 복원 능력을 합친다.
  3. **Atrous Conv**<br>downsampling을 덜 하면서도 dilation으로 넓은 receptive field를 확보한다.
  4. **ASPP**<br>여러 atrous rate로 같은 feature를 서로 다른 receptive field에서 보고 multi-scale context를 얻는다.
  5. **Decoder**<br>high-level semantic feature를 upsample하고 backbone의 low-level feature와 concat해서 boundary를 refinement한다.
  6. **Evidence**<br>decoder ablation과 boundary 실험에서 제안 구조가 실제로 개선을 만들었고, VOC/Cityscapes에서도 강한 최종 성능을 보였다.

## Abstract
Semantic segmentation을 위한 DNN은 크게 (1) spatial pyramid pooling module, (2) encoder-decoder 구조가 사용된다.
1. **Spatial pyramid pooling module**
  여러 비율(rate)과 여러 크기의 effective field-of-view를 가지는 filter 또는 pooling 연산을 통해 입력 feature를 탐색함으로써, `multi-scale contextual information을 인코딩`한다.
  Ex) 어떤 물체가 작은 물체인지, 큰 물체인지 모르기 때문에 하나의 receptive field만 보는 것보다 여러 크기로 보는 것이 유리하다.
2. **Encoder-decoder **
  Spatial information을 점진적으로 복원함으로써 `더 선명한 object boundary를 얻을 수 있다.`
  Ex) 고양이 영역이라고 맞추는 것뿐 아니라, 고양이가 정확히 어디서 시작하고 어디서 끝나는지를 더 정확하게 복원한다.
DeepLabv3+는 `위 두 방법의 장점을 결합`하는 것을 제안한다. 간단하지만 효과적인 decoder module을 추가함으로써, 특히 object boundary 주변의 segmentation 결과를 더 정교하게 개선한다.
```python
        DeepLabV3
   multi-scale context
          ↓
       Encoder
          ↓
   semantic feature
          ↓
       Decoder
          ↓
 boundary refinement
          ↓
 segmentation
```

## 1. Introduction
- Semantic segmentation의 목표
  ```python
넓은 context 이해
+
정확한 object boundary
  ```
- 기존의 문제점 `trade-off` → 전부 고해상도로 처리하면 너무 비싸다.
  ```python
Feature resolution을 낮추면
→ 계산량 ↓
→ semantic abstraction ↑
→ spatial detail ↓

Feature resolution을 높게 유지하면
→ spatial detail ↑
→ segmentation boundary ↑
→ 계산량 / memory ↑
  ```

<p class="figure-note"><strong>Original Figure 1:</strong> Spatial Pyramid Pooling, Encoder-Decoder, 그리고 제안 구조의 차이는 <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">원 논문 Figure 1</a>을 함께 보면 가장 명확하다. 위의 DeepLabV3+ overview는 그 핵심만 redraw한 것이다.</p>

1. (a) Spatial Pyramid Pooling
  장점: multi-scale context 높임
  단점: 마지막에 크게 upsample → 세밀한 boundary 복원 어려움
2. (b) Encoder-Decoder
  장점: spatial resolution을 점진적으로 복원 → boundary에 유리
3. (c) Encoder-Decoder with Atrous Conv (저자 방법)
  DeepLab의 강한 sementic encoder + encoder-decoder의 boundary recovery
⇒ DeepLabV3+가 `encoder에서 rich semantic information을 얻고, decoder에서 detailed object boundary를 복원`한다.
```python
Encoder:
적당히 낮은 resolution에서
semantic feature를 효율적으로 추출

Decoder:
필요한 spatial information을 다시 가져와
boundary를 복구
```

- Contribution
  - DeepLabV3 + decoder
  - Atrous convolution으로 encoder resolution 제어
  - Xception 수정 + depthwise separable convolution
  - 실험적인 성능 좋게 나옴
  - 구현 공개함

## 3. Method
## 3.1 Encoder-Decoder with Atrous Convolution

<p class="figure-note"><strong>Visual reference:</strong> encoder → ASPP → decoder와 low-level feature 경로는 위 <b>Figure 1</b>에 redraw했다. 세부 tensor flow는 <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">원 논문 Method section</a>을 참고한다.</p>

### Atrous convolution
일반 convolution과 같은 방식으로 feature를 계산하지만, `kernel 내부 sampling 간격을 벌려서 더 넓은 receptive field를 확보`한다.
- 특징
  - 같은 깊이인데, 더 넓게 볼 수 있다.
  - downsampling으로 spatial size를 너무 줄이면 존재 여부와 같은 semantic 정보는 잘 잡을 수 있지만, 물체의 경계가 몇 픽셀 위치이고 어디까지인지와 같은 세밀한 spatial 정보는 손실되기 쉽다. 

<figure class="paper-figure">
  <div class="paper-figure-frame"><div class="paper-figure-canvas">
  <svg viewBox="0 0 760 245" role="img" aria-label="Atrous convolution sampling pattern">
    <text x="24" y="28" class="fig-kicker">ATROUS CONVOLUTION</text>
    <rect x="46" y="68" width="250" height="128" rx="3" class="fig-box"/>
    <text x="171" y="89" class="fig-label">Standard 3×3</text>
    <circle cx="111" cy="126" r="6" fill="#668ca7"/><circle cx="171" cy="126" r="6" fill="#668ca7"/><circle cx="231" cy="126" r="6" fill="#668ca7"/>
    <circle cx="111" cy="156" r="6" fill="#668ca7"/><circle cx="171" cy="156" r="6" fill="#668ca7"/><circle cx="231" cy="156" r="6" fill="#668ca7"/>
    <circle cx="111" cy="186" r="6" fill="#668ca7"/><circle cx="171" cy="186" r="6" fill="#668ca7"/><circle cx="231" cy="186" r="6" fill="#668ca7"/>
    <rect x="464" y="68" width="250" height="128" rx="3" class="fig-box-accent"/>
    <text x="589" y="89" class="fig-label">Atrous 3×3</text>
    <circle cx="499" cy="116" r="6" fill="#668ca7"/><circle cx="589" cy="116" r="6" fill="#668ca7"/><circle cx="679" cy="116" r="6" fill="#668ca7"/>
    <circle cx="499" cy="151" r="6" fill="#668ca7"/><circle cx="589" cy="151" r="6" fill="#668ca7"/><circle cx="679" cy="151" r="6" fill="#668ca7"/>
    <circle cx="499" cy="186" r="6" fill="#668ca7"/><circle cx="589" cy="186" r="6" fill="#668ca7"/><circle cx="679" cy="186" r="6" fill="#668ca7"/>
    <text x="380" y="144" class="fig-label">→</text>
  </svg></div></div>
  <figcaption><strong>Figure 2.</strong> Atrous convolution은 kernel parameter 수를 늘리지 않고 sampling 간격을 벌려 더 넓은 receptive field를 확보한다. Conceptually adapted from Chen et al. (2018).</figcaption>
</figure>

### Depthwise separable convolution
- Depthwise conv: 각 channel 별로 spatial convolution
- Pointwise conv: 1x1 convolution으로 channel들을 섞음
- `Depthwise separable convolution`: 둘을 불리해서 일반 convolution보다 계산량을 줄임
```python
각 input channel
      ↓
각자 3×3 conv
      ↓
1×1 conv
      ↓
channel mixing
```

<figure class="paper-figure">
  <div class="paper-figure-frame"><div class="paper-figure-canvas">
  <svg viewBox="0 0 760 250" role="img" aria-label="Depthwise separable convolution">
    <defs><marker id="dscA" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#7d858c"/></marker></defs>
    <text x="24" y="28" class="fig-kicker">DEPTHWISE SEPARABLE CONVOLUTION</text>
    <rect x="48" y="88" width="150" height="70" rx="3" class="fig-box"/><text x="123" y="114" class="fig-label">Input channels</text><text x="123" y="139" class="fig-small">C feature maps</text>
    <path d="M198 123 L278 123" class="fig-arrow" marker-end="url(#dscA)"/>
    <rect x="290" y="76" width="170" height="94" rx="3" class="fig-box-accent"/><text x="375" y="105" class="fig-label">Depthwise 3×3</text><text x="375" y="132" class="fig-small">spatial filtering</text><text x="375" y="151" class="fig-small">per channel</text>
    <path d="M460 123 L536 123" class="fig-arrow" marker-end="url(#dscA)"/>
    <rect x="548" y="76" width="164" height="94" rx="3" class="fig-box"/><text x="630" y="105" class="fig-label">Pointwise 1×1</text><text x="630" y="132" class="fig-small">channel mixing</text>
  </svg></div></div>
  <figcaption><strong>Figure 3.</strong> Depthwise separable convolution은 spatial filtering과 channel mixing을 분리한다.</figcaption>
</figure>

### DeepLabv3 as encoder
- `output stride` 정의
  - input image의 spatial resolution과 최종 feature resolution의 비율
  - `encoder가 spatial information을 얼마나 버렸는지, 그리고 계산량이 얼마나 큰지를 동시에 나타내는 지표`이다.
    Ex) 입력이 512x512이고, OS=32라면 원본 이미지의 대략 32x32 영역이 encoder output의 한 spatial location으로 압축되는 셈이다.
    ```python
Input: 512 × 512
Feature: 16 × 16

512 / 16 = 32
→ output stride = 32

"encoder가 입력의 가로/세로를 16배 줄인 feature를 출력한다."
    ```

<p class="figure-note"><strong>Output stride reference:</strong> OS와 atrous rate의 관계는 <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">원 논문 encoder-decoder 설명</a>을 참고한다. 본문 예시처럼 OS가 작을수록 feature resolution은 높고 계산량은 커진다.</p>

- **DCNN/backbone** → feature 추출
- **Atrous Conv** → downsampling을 덜 하면서 receptive field 확보
- **ASPP** → 여러 scale의 context 수집
- **ASPP 뒤 1×1 Conv** → multi-scale feature fusion
- **Low-level feature** → boundary/spatial detail 제공
- **Low-level 쪽 1×1 Conv** → channel을 48로 축소
- **×4 upsample** → low-level feature와 spatial size 맞춤
- **Concat** → semantic + spatial feature 결합
- **3×3 Conv ×2** → 실제 decoder refinement
- **마지막 ×4** → 원본 resolution으로 복원

## 3.2 Modified Aligned Xception
Xception이 ImageNet classification에서 좋은 성능과 빠른 계산을 보엿다. MSRA 팀이 `Xception을` object detection용으로 수정한 Aligned Xception을 만들었고, DeepLabV3+ 저자들은 그 흐름을 이어서 `semantic segmentation에 맞게 수정`한다.
- **Xception을 더 깊게 만든다**
  segmentation backbone으로 더 강한 featrue extractor를 쓰기 위해 더 깊게 확장한다.
- **모든 max pooling을 stride가 있는 depthwise separable convolution으로 바꾼다**
  backbone 전체를 convolution 기반으로 만들어서 output stride와 atrous rate를 더 자유롭게 제어하기 위함이다.
- **각 3×3 depthwise convolution 뒤에 BatchNorm과 ReLU를 추가한다**
  학습 안정성과 표현력을 높이기 위한 일반적인 설계이다. (MobileNet 설계와 비슷하다.)

<p class="figure-note"><strong>Xception reference:</strong> Modified Aligned Xception의 상세 entry/middle/exit flow는 <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">원 논문 architecture figure</a>에서 확인한다. 이 노트에서는 segmentation 관점에서 필요한 변경점만 유지한다.</p>

```python
Entry flow
→ 초반 feature extraction + downsampling

Middle flow
→ 같은 resolution에서 feature를 깊게 처리
→ 16번 반복

Exit flow
→ 마지막 high-level semantic feature 추출
```
Xception backbone도 일반 CNN처럼 초반에는 spatial size를 줄이고 channel을 늘리면서, 후반으로 갈수록 더 semantic한 feature를 만든다.
참고) `+` 기호는 ResNet 때 본 것과 같이 shortcut connection이다. 

## 4.1 Decoder Design Choices
1. low-level feature의 channel을 얼마나 줄일까?
  low-level feature를 1x1 conv로 줄이는데, 8/16/32/48/64 channel을 비교한다. 결과는 48 channels가 78.21% mIoU로 가장 좋았고, 32도 비슷하게 좋았다. 
  따라서 최종적으로 \\[1x1, 48\\]을 쓴다.
2. decoder에 3x3 conv를 몇 개, 몇 channel로 둘까?
  concat 이후의 decoder convolution을 비교한다. 결과는 256개 필터를 2번 한 것이 최적이었다. 
3. backbone의 어느 low-level feature를 가져올까?
  DeepLabV3 encoder 자체가 이미 강한 semantic feature를 만들기 때문에, decoder를 U-Net처럼 복잡하게 만들 필요가 없었다.
- baseline
  DeepLabV3는 OS=16일 때 prediction logits을 그냥 16배 bilnear upsampling해서 원본 크기로 만든다. 저자들은 이것을 naive decoder라고 부르고, PASCAL VOC val에서 77.21% mIoU를 얻는다.
  DeepLabV3+는 여기에 학습 가능한 decoder를 추가하여 더 개선하려는 것이다.

## 4.2 ResNet-101 as Network Backbone
output stride decoder, multi-scale evaluation이 실제 성능과 계산량에 어떤 영향을 주는가를 확인한다.
1. OS를 16에서 8로 줄이면 feature가 더 dense해져 성능은 올라가지만 계산량이 크게 증가한다.
  <table>
  
<tr>
<td>설정</td>
<td>mIoU</td>
<td>계산량</td>
</tr>
<tr>
<td>train OS=16, eval OS=16</td>
<td>77.21%</td>
<td>81.02B</td>
</tr>
<tr>
<td>train OS=16, eval OS=8</td>
<td>78.51%</td>
<td>276.18B</td>
</tr>
<tr>
<td>train OS=16, eval OS=16 + Decoder</td>
<td>78.85%</td>
<td>101.28B</td>
</tr>
<tr>
<td>train OS=16, eval OS=8 + Decoder</td>
<td>79.35%</td>
<td>297.92B</td>
</tr>
  </table>
2. decoder가 효율적이다.
  OS=16 상태에서 단순 bilinear upsampling만 하면 77.21%인데, proposed decoder를 추가하면 78.85%까지 올라간다.
  계산량은 81.02B → 101.28B 정도로 증가한다.
> OS를 줄이면 더 dense한 feature를 얻어서 성능은 올라가지만 계산비용이 크게 증가한다. 반면 OS=16을 유지한 채 decoder를 추가하면 비교적 적은 계산량 증가로 segmentation 성능을 개선할 수 있다. 그래서 DeepLabV3+는 OS=16 encoder + decoder 구성을 효율적인 선택으로 본다.

## 4.3 Xception as Network Backbone
1. Xception + DeepLabv3 encoder 자체가 강하다. Cityscapes val에서 X-65 backbone에 ASPP와 image-feature를 사용한 DeepLabv3 설정이 77.33 mIoU를 낸다.
2. decoder를 붙이면 성능이 명확히 오른다. DeepLabV3+의 핵심 주장인 “decoder가 segmentation detail을 복원한다”는 것과 연결된다.
3. backbone을 더 깊게 하면 추가 이득이 있다.  

## 4.4 Improvement along Object Boundaries
```python
주장:
decoder가 boundary를 개선한다.

Evidence:
boundary 근처를 따로 평가해도
decoder 사용 모델이 더 좋았다.
```

<p class="figure-note"><strong>Boundary experiment:</strong> decoder가 object boundary를 실제로 개선하는 qualitative/trimap 결과는 <a href="https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html">원 논문 boundary analysis</a>에서 확인할 수 있다. 여기서는 ablation 결과와 해석을 중심으로 남겼다.</p>

## Summary
1. **Problem**<br>semantic segmentation에서 강한 semantic context와 정확한 boundary를 동시에 얻기 어렵다.
2. **Core idea**<br>DeepLabV3의 multi-scale context 능력과 encoder-decoder의 spatial detail 복원 능력을 합친다.
3. **Atrous Conv**<br>downsampling을 덜 하면서도 dilation으로 넓은 receptive field를 확보한다.
4. **ASPP**<br>여러 atrous rate로 같은 feature를 서로 다른 receptive field에서 보고 multi-scale context를 얻는다.
5. **Decoder**<br>high-level semantic feature를 upsample하고 backbone의 low-level feature와 concat해서 boundary를 refinement한다.
6. **Evidence**<br>decoder ablation과 boundary 실험에서 제안 구조가 실제로 개선을 만들었고, VOC/Cityscapes에서도 강한 최종 성능을 보였다.

---
## 참고사항
### Spatial pyramid pooling module
segmentation에서 물체 크기가 제각각이다.
Ex) 한 이미지 안에 아주 작은 사람, 큰 자동차, 넓은 도로가 있을 수 있다. 
하나의 고정된 receptive field만 보면 어떤 물체에는 너무 좁고, 어떤 물체에는 너무 넓을 수 있다. 그래서 `여러 크기의 문맥을 동시에 보고 합치자`는 아이디어가 나온다.
```python
feature map
   ├─ 작은 범위로 보기
   ├─ 중간 범위로 보기
   ├─ 큰 범위로 보기
   └─ 전체 이미지 수준으로 보기
          ↓
       concatenate
          ↓
   multi-scale feature
```
- Pyramid : 서로 다른 spatial scale을 여러 단계로 본다.
DeepLab에서는 전통적인 pooling pyramid를 그대로 쓰기보다, ASPP (Atrous Spatial Pyramid Pooling)을 쓴다.
Ex) 각 branch가 보는 범위가 다르다.
```python
같은 feature map
   ├─ 1×1 conv
   ├─ 3×3 atrous conv, rate=6
   ├─ 3×3 atrous conv, rate=12
   ├─ 3×3 atrous conv, rate=18
   └─ image-level feature
          ↓
       concatenate
```

### Backbone
`특징 추출을 담당하는 기본 네트워크`
```python
Input image
   ↓
Backbone
   ↓
Feature map
   ↓
Task-specific module
   ↓
Prediction
```
Ex) Image classification → ResNet이 backbone이다.
```python
Image
  ↓
ResNet
  ↓
Feature
  ↓
FC layer
  ↓
Class
```

Ex) Semantic segmentation → ResNet이나 Xception이 backbone이다.
```python
Image
  ↓
Backbone
  ↓
Feature map
  ↓
ASPP / Decoder
  ↓
Segmentation mask
```

<section class="related-notes" aria-labelledby="related-notes-title">
  <h2 id="related-notes-title">Related Notes</h2>
  <div class="related-notes-list">
    <a class="related-note-link" href="/notes/unet-2015/"><strong>U-Net (2015)</strong><span>Encoder-decoder와 skip connection을 중심으로 한 segmentation 구조 비교.</span></a>
    <a class="related-note-link" href="/notes/resnet-2015/"><strong>ResNet (2015)</strong><span>DeepLab backbone에서도 자주 쓰이는 residual learning의 기본 메커니즘.</span></a>
  </div>
</section>

