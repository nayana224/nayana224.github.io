---
layout: feed_note
title: "15,465개 MCP server를 조사했더니 agent의 trust boundary가 protocol 밖에 있었다"
date: 2026-09-24 23:17:23 +0900
channel: ai-robotics
channel_label: AI & Robotics
summary: "OX Security가 공개 MCP server 15,465개와 5,095개 hostname을 조사해 data residency, abandoned domain, consumer-network exposure를 확인했다. Claude Code 실험에서는 일부 구형 모델 구성에서 한 번의 Always-Allow가 이후 prompt injection의 privileged file access로 이어질 수 있었다. Anthropic의 parallel-agent science workflow와 ROS 2 GPU-resident transport까지 함께 보면 agent/robotics system은 모델 성능뿐 아니라 trust boundary와 data path를 함께 설계해야 한다."
---

**OX Security가 공개 MCP server 15,465개를 분석했더니, agent가 연결하는 tool infrastructure 자체가 새로운 trust boundary로 떠올랐다.** 조사 대상 5,095개 unique hostname 중 **15.6%는 미국 밖의 infrastructure로 resolve**됐고, **2.3%는 resolve되지 않았으며 그중 6개 domain은 다시 등록 가능한 상태**였다. 또 0.45%는 home network나 consumer tunneling tool과 연관돼 있었다.

핵심은 MCP protocol 자체의 결함 하나라기보다 **agent에게 tool permission을 주는 순간 그 뒤의 server·domain·hosting lifecycle까지 신뢰하게 된다는 점**이다. OX의 Claude Code 실험에서는 Haiku 3.5를 사용했을 때 한 번 `Always-Allow`를 허용한 뒤 malicious MCP server의 prompt injection이 추가 확인 없이 privileged file access로 이어졌다. 같은 공격은 OX가 시험한 Opus 4.6·4.7에서는 성공하지 않았으므로, 이를 모든 Claude/MCP client에 일반화해서는 안 된다.

MCP를 실제 agent architecture에 넣을 때는 `tool schema가 안전한가`만 보는 것으로 부족하다. **server identity, domain ownership, network/data residency, permission persistence, model/client별 prompt-injection resistance**까지 함께 관리해야 한다. MCP가 plugin layer처럼 넓어질수록 tool registry와 permission policy도 dependency governance에 가까운 system component가 된다.

---

**약 950개의 Claude agent가 21시간 동안 2억1천만 token을 사용해 DNA sequence를 탐색하고, 기존에 정의되지 않았던 enzyme system 후보를 찾아냈다.** Anthropic의 새 life sciences 연구팀은 이 과정에서 Claude가 20만 개가 넘는 reverse transcriptase(RT)를 모으고, 3,500개 candidate system을 추린 뒤 20개까지 좁혔다고 공개했다.

그중 한 agent가 jumbo phage의 RT 주변에서 반복되는 non-coding DNA array를 발견했고, 추가 분석과 인간 연구자의 wet-lab 검증을 거쳐 이를 **array-associated reverse transcriptase(ART)**라고 명명했다. ART는 RT, 인접 partner gene, 일정 간격의 DNA repeat array로 구성되며, 초기 실험에서는 이 array가 여러 short RNA로 발현되는 것도 확인됐다. 다만 **ART의 실제 biological function은 아직 밝혀지지 않았다.** 따라서 이를 곧바로 새로운 CRISPR나 gene-editing tool로 해석하는 것은 이르다.

흥미로운 부분은 특정 biology model 하나보다 **parallel agent orchestration 자체가 discovery instrument로 사용됐다는 점**이다. 초기 prompt와 wet-lab work를 제외하면 agent들이 literature와 sequence database를 탐색하고, candidate를 비교·비판하고, human-readable report까지 생성했다. `여러 agent가 넓게 탐색 → 후보를 좁힘 → 사람이 physical experiment로 검증`하는 구조는 software agent를 넘어 실제 science workflow에서도 high-level agent와 deterministic/physical verification layer를 어떻게 분리할지 보여주는 사례다.

---

**같은 날 robotics stack 쪽에서는 ROS 2 Lyrical의 `rosidl::Buffer`와 NVIDIA CUDA buffer backend가 GPU-resident data를 표준 ROS message 안에서 직접 전달하는 경로를 열었다.** 같은 host·CUDA device·Linux user와 지원 RMW 조건을 만족하면 co-located node 사이 payload를 host copy·serialization 없이 넘기고, 조건이 맞지 않으면 기존 CPU path로 fallback한다.

Isaac ROS 5.0도 이 upstream mechanism으로 이동하면서 기존 NITROS transport API를 deprecated하고 있다. perception-to-action pipeline에서는 model inference 시간뿐 아니라 **sensor → preprocessing → model → control 사이에서 data가 어떤 memory path로 이동하는지**까지 end-to-end latency에 포함해 봐야 한다는 변화다.

## Sources
- [OX Security Research — 15,465 MCP Servers. 0 Governance.](https://www.ox.security/ebooks/15465-mcp-servers-0-governance/)
- [Anthropic — Claude discovers a novel enzyme system with CRISPR-like repeats](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)
- [NVIDIA Technical Blog — Accelerating a ROS 2 Node with an AI Agent and NVIDIA Isaac ROS](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros)
- [Isaac ROS — rosidl::Buffer and Buffer Backends](https://nvidia-isaac-ros.github.io/concepts/rosidl_buffer/index.html)
- [Isaac ROS 5.0 — From NITROS to rosidl::Buffer](https://nvidia-isaac-ros.github.io/v/release-5.0/concepts/rosidl_buffer/nitros_migration.html)
