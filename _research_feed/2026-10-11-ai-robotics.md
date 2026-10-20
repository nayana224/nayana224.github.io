---
layout: feed_note
title: "두 로봇이 같은 장면을 봐도, 같은 정보를 가진 것은 아니다"
date: 2026-10-11 19:00:00 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "CoLA는 각 팔의 VLA backbone을 고정하고 작은 통신 채널과 팔별 action head를 학습한다. 가려진 정보가 있는 handover에서 통신의 효과가 컸지만, 공유 카메라에서는 효과가 작았다."
---

두 로봇 팔이 같은 작업을 맡아도 관측이 다르면 각자 고른 행동만으로는 해결되지 않는 경우가 있다. 한 팔만 상자의 색 표지를 볼 수 있다면, 반대편 팔은 어느 tray에 놓아야 할지 모른다. **CoLA**는 이처럼 정보가 분산된 작업에서 VLA 간 명시적 통신이 언제 필요한지 측정한다.

각 agent의 pretrained VLA backbone은 고정하고, 작은 message channel과 팔별 diffusion action head를 학습한다. 실행은 decentralized 방식으로 이뤄진다. 즉 중앙 policy가 두 팔의 모든 행동을 한 번에 생성하기보다, 각 agent가 메시지와 자기 관측을 바탕으로 행동을 정한다.

가려진 tray handover에서 표지가 한 agent에게만 보일 때, CoLA의 성공률은 메시지를 학습 중부터 제거한 설정의 **1.3% 대비 76.0%**였다. 반면 overhead camera가 두 팔 모두에게 같은 정보를 제공하는 handover에서는 메시지를 제거해도 성공률 차이가 작았다(두 팔 과제 90.6% 대 88.3%, 세 팔 63.5% 대 60.0%). wrist-only 관측 조건에서는 메시지를 제거했을 때 두 팔 과제 성공률이 74.8%에서 64.3%로 낮아졌다.

따라서 이 결과는 “다중 로봇이면 항상 통신이 이득”이라는 주장을 지지하지 않는다. **agent들이 공유하지 못한 task-relevant information이 있을 때 통신 가치가 커진다**는 조건부 결과다. 공통 시야가 충분한 장면에서는 통신 비용과 복잡도를 추가해도 성능 이득이 작을 수 있다.

실제 다중 팔 시스템에서는 통신 지연·패킷 손실, agent 간 frame과 object identity 일치, 동시에 내린 command의 충돌을 추가로 다뤄야 한다. 논문은 세 handover 조건에서의 성능과 backbone 일반화를 보고하지만, 산업 셀의 장시간 동작이나 네트워크 장애 아래 안전한 조정까지 입증하지는 않는다.

## Sources
- [CoLA 논문 원문과 실험 결과](https://arxiv.org/abs/2610.15337)
- [CoLA 논문 HTML](https://arxiv.org/html/2610.15337v1)
