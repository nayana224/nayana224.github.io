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
