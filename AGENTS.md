# AGENTS.md

## Project
Personal GitHub Pages site for Inpyo Lee.

## Branch policy
Apply requested website changes directly to `main` unless the user explicitly requests otherwise.

## Homepage copy direction
- Present the profile as a robotics systems / manipulation background that is expanding toward robot learning and multimodal robotics.
- Lead with demonstrated experience before aspirational research interests.
- Keep the core progression: Mechatronics → ROS 2 Robotics → System Integration & Manipulation → Learning for Robotics.
- Group research interests into Robotic Manipulation, Robot Learning, and Multimodal Learning for Robotics instead of listing overlapping VLM/VLA/Embodied AI labels separately.
- Preserve the sparse academic layout and compact information hierarchy.

## Research Feed automation contract
- Research Feed is the Jekyll `research_feed` collection; automated posts live under `_research_feed/`.
- Required front matter: `layout: feed_note`, hook-style title, timezone-aware date (+0900), channel, channel_label, summary. Channels are `ai-robotics` and `research-papers`.
- Treat public @choi.openai Threads as an always-on discovery/editorial benchmark, not merely fallback. Continuously broaden the observed corpus and learn topic/source patterns, while never copying distinctive wording, titles, metaphors, sentence order, or rhythm.
- Discovery spans official AI labs/products, robotics/Physical AI organizations, academia/arXiv/OpenReview/project pages, GitHub builder ecosystem, community demos/experiments, and deployment/inference/edge infrastructure. Social posts are discovery signals only; factual claims require primary-source verification whenever possible.
- Maintain a high-priority radar for Robot Learning, Embodied AI/agents, VLA/VLM robotics, manipulation/grasping/dexterity/bimanual systems, closed-loop feedback/recovery/residual control, imitation learning/ACT/Diffusion Policy, grounding/affordance/task planning, robot foundation models, real-world deployment/lab automation, Isaac/GR00T/sim-to-real/synthetic data, perception-to-action sensing, robotics-relevant vision/Transformers, agent architecture/context/memory/tool orchestration, edge VLM/quantization/Jetson, robotics benchmarks/data/teleoperation, and food/deformable/entangled-object manipulation.
- Search by topic and source graph, not only company names. Follow upstream authors, repositories, labs, project pages, citations, and adjacent work when a useful topic appears.
- Select candidates on novelty, concreteness, technical relevance, practical usefulness, and source quality. Broad AI relevance and user-specific research relevance are independent positive signals. Never create filler.
- Before publishing, inspect recent `_research_feed/` files for duplicate products, papers, features, and core claims. Publish follow-ups only when the new delta is explicit.
- Writing rhythm: concrete hook in first 1–3 sentences → exact change/number/capability → concise practical/research implication. Keep paragraphs short and avoid report-like exposition.
- Prefer one focused story when one item is strong; use `1/`, `2/`, `3/` only for genuinely related items. Do not force a fixed synthesis section.
- Titles should state the change, not use generic roundup labels. English technical terms may remain natural in Korean prose. Avoid sensationalism.
- Put clickable Markdown primary-source links in the final `Sources` section; never publish bare URLs.
- At most one compact explanatory schematic per focused story, only when materially useful. Independently redraw from verified facts in restrained paper/seminar block-arrow style, with `Figure N.` caption and source. Do not reuse third-party graphics without clear permission.
- Do not create a Research Papers post unless genuinely notable fresh papers exist.
- Hourly runs must avoid duplicate stories and update the same date/channel file instead of creating multiple same-day files.
- If no candidate clears the threshold, do not modify feed files.

## Research Feed run log
- 2026-09-21: Discovery contract updated to always-on CHOI benchmarking plus dedicated Robotics/Physical AI/VLA/manipulation radar and source-graph exploration.
- 2026-09-22: Re-ran broad AI/Robotics discovery; retained primary-source-first verification and selected a deployment/inference infrastructure delta only after checking same-day feed state.
- 2026-09-22: Scanned the fresh robotics paper stream and added STRIDER as a notable Robot Learning/loco-manipulation item after checking that no same-day Research Papers file existed.
- 2026-09-22: Added Google Home MCP as a concrete expansion of agent tooling into physical-device context/control; retained the existing TensorRT multi-device inference item and same-day file policy.
- 2026-09-22: Re-scanned fresh official AI, agent, robotics, VLA/manipulation, and infrastructure sources after the prior run; no newly verified item cleared the publication threshold, so the Research Feed was left unchanged.
- 2026-09-22: Re-scanned the post-run window across AI agents, VLA/manipulation, embodied AI, and deployment sources. Fresh search results did not yield a sufficiently new primary-source-verified story beyond the same-day MCP/TensorRT items, so no feed post was changed.
- 2026-09-22: Added JetBrains Air's expansion from a standalone agentic workspace toward an open multi-agent development system after cross-checking current JetBrains product/docs sources; same-day AI & Robotics feed remains capped at three items.
- 2026-09-23: Added NVIDIA Isaac ROS 5.0 as a high-priority Robotics/Physical AI update: agent-ready setup/manipulation skills, ROS Lyrical GPU data-path work, accelerated FoundationPose, and RealSense/Jetson integration connect agentic development directly to the ROS perception-to-manipulation stack.
- 2026-09-23: Added RoboHarm after tracing the CHOI discovery graph back to Robocurve's primary benchmark and reproducible repository. The key editorial signal is physical-AI safety evaluation that separates explicit refusal from capability failure rather than treating task failure as safety.
- 2026-09-23: Added Claude Opus 5.5 after primary-source verification. The editorial delta is agentic-workload efficiency rather than benchmark rank alone: Anthropic reports 40% lower typical workload cost than Opus 5, >30% faster output, lower cache pricing, and an execution-safety stack aimed at long-running autonomous coding agents.
- 2026-09-23: Added VT-Bridge to the Research Papers channel after primary-source verification. Its notable pattern is lightweight closed-loop tactile residual adaptation: a 0.98M-parameter adapter refines pretrained VLA actions at robot execution frequency, using up to 50 vision-tactile demonstrations per task and improving average completion from 11.7% to 62.9% across the authors' tested backbones/tasks.
- 2026-09-23: Added Opt2VLA after primary-source verification. It complements VT-Bridge from a different contact-rich manipulation design axis: the multi-task VLA explicitly predicts both geometric motion goals and continuous contact-force references, with RL whole-body controllers tracking them; closed-loop evaluation includes language-conditioned force modulation in simulation and on humanoid hardware.
- 2026-09-23: Re-scanned the latest post-Opt2VLA window across CHOI-style AI discovery, agent/MCP workflows, VLA/contact-rich manipulation, embodied AI, and deployment. Newly surfaced items were older research, secondary-only reports, or already-covered topics; no candidate cleared the publication threshold, so `_research_feed/` was left unchanged.
- 2026-09-23: Newly verified Nota AI's primary-source edge-VLA implementation and promoted it into the day's top-three AI/Robotics feed in place of the broader Claude item. GR00T N1.7 ran on a Qualcomm Dragonwing IQ-9075 NPU at about 230 ms versus a 1.6 s baseline; the implementation also exposed camera-thread/control-loop bottlenecks beyond model inference, making it directly relevant to practical on-device robotics.
- 2026-09-23: Added Paper2Agent after verifying the Nature version of record and upstream GitHub repository. The notable agent-architecture pattern is paper + code + data + workflow → tested MCP tools/resources/prompts, turning scientific methods into executable, provenance-bearing interfaces rather than retrieval-only context.
- 2026-09-23: Newly confirmed rMuscle from the fresh VLA inference stream and promoted it into the day's Research Papers top-three. Its system-level contribution is cross-execution reuse: visual-token outputs and action-stage activation patterns are cached across repetitive robot runs, yielding a reported 1.29–1.42× speedup on RTX 4090 and Jetson Thor while preserving success rates in the authors' evaluated tasks. Paper2Agent was removed from the same-day top-three to keep the feed focused on the strongest robotics-relevant items.
- 2026-09-23: Re-scanned the latest discovery window across CHOI-style AI/agent topics, fresh VLA/manipulation and embodied-AI work, and edge/Jetson deployment. The apparent Jetson Orin Nano 2 news was a resurfacing of NVIDIA's August 25 announcement rather than a new release; no newly verified candidate exceeded the existing same-day top-three, so `_research_feed/` was left unchanged.
- 2026-09-23: Re-scanned the post-run window across broad AI/product/agent signals and the Robotics/VLA radar. Fresh search was dominated by already-covered Claude Opus 5.5 and RoboHarm, older Gemini Robotics material, or secondary-only items without a sufficiently strong new primary-source delta. No candidate displaced the current same-day top-three, so `_research_feed/` remained unchanged.
- 2026-09-23: Re-scanned broad AI/agent/product sources plus fresh robotics/VLA papers. ActiveArena and topology-informed VLA prompting were technically relevant but did not clearly exceed the current same-day VT-Bridge / Opt2VLA / rMuscle top-three on combined novelty, concreteness, and immediate research usefulness; current-day feed files were left unchanged.
- 2026-09-23: Added FLUX 3 Action after its public 7B open-weight World Action Model release. The primary BFL product page confirms the open-weight 7B model; release reporting adds the supplied RoboLab-120 result and 32-action/future-frame closed-loop interface. Because external reproduction is still limited, benchmark claims are explicitly framed as vendor-supplied. FLUX 3 Action displaced RoboHarm in the same-day AI/Robotics top-three due to stronger freshness and direct robot-foundation-model relevance.
- 2026-09-23: Re-scanned the newest post-FLUX window across CHOI-style broad AI/agent discovery and fresh Robotics/VLA research. A real-time VLA RL paper surfaced around stale-observation/latency-aware policy optimization, but available discovery evidence was not yet strong enough to displace the already-curated same-day top-three without fuller primary-source verification. No Research Feed file was changed.
- 2026-09-23: Added VisForce after verifying the fresh arXiv primary source. It grounds current and desired contact forces directly at fingertip locations in wrist/goal imagery and evaluates real dexterous manipulation including egg, toothpaste-tube, bread-transfer, pouring, and peg-in-hole tasks. Its visual-grounding formulation and direct relevance to force-sensitive/deformable-object manipulation displaced Opt2VLA in the same-day Research Papers top-three.
- 2026-09-23: Re-scanned the latest broad AI/agent and Robotics/VLA window. OpenAI's new model-misalignment reporting framework is broadly notable, while Realset's embodied-agent data funding/benchmark announcement is relevant to the data-collection radar, but neither supplied a stronger immediate technical delta than the current same-day curated top-three; no `_research_feed/` file was changed.
- 2026-09-23: Re-scanned CHOI-style broad AI/product/agent discovery plus fresh VLA/manipulation, embodied-AI, NVIDIA robotics, and inference/deployment sources. Newly surfaced search results were older, secondary-only, or did not provide a stronger verified technical delta than the current same-day top-three; no `_research_feed/` file was changed.

## Public notes / privacy policy
- Public Notes may contain general concepts, theory, paper study, and broadly reusable technical explanations.
- Do not publish lab-internal work, unpublished research details, experiment settings/results, internal project architecture, private code/repositories, collaborator information, or confidential lab activity.
- Treat Notion as private working material and GitHub Pages as a curated public knowledge base; do not mirror Notion automatically.
- Keep authored publications separate from papers studied in Notes.
- Prefer semantic, lightweight, responsive HTML/CSS diagrams or independently redrawn paper-like schematics; never expose private lab/project details through visuals.

## Notes authoring / Notion import rules
- Treat Notion as source material, not publish-ready Markdown.
- Public Notes math rendering uses MathJax in `_layouts/note.html`.
- Preserve existing tested escaping conventions in `_notes/*.md`; verify rendered math rather than changing escaping globally during unrelated work.
