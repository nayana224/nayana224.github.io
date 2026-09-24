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
- 2026-09-24 17:18 KST: Re-ran broad discovery across current AI/agent tooling, VLA/embodied manipulation, robot-learning papers, edge/Jetson deployment, and CHOI-style community signals. The newly surfaced search results were older material, secondary coverage, or did not represent a verified delta beyond today's existing BoxBot and dexterous-VLA notes; `_research_feed/` was intentionally left unchanged.
- 2026-09-24 15:53 KST: Added a focused AI & Robotics note on Viam BoxBot. The system deliberately splits box opening between 1–2 mm tape-seam visual servoing and a fine-tuned SmolVLA for deformable flap manipulation, with local inference on Jetson Orin Nano. The note distinguishes Viam's 125 collected demonstrations from the 110 training episodes currently listed in the public Hugging Face model card and notes the absence of quantitative evaluation results there.
- 2026-09-24 14:48 KST: Completed a broad discovery pass across AI agents, robotics/VLA/manipulation, NVIDIA/edge infrastructure, Hugging Face, academia, and CHOI-style community signals. No newly verified candidate since the prior run cleared the publication threshold, so `_research_feed/` was intentionally left unchanged.
- 2026-09-24: Added a focused Research Papers note on high-DoF dexterous VLA post-training. The paper uses a temporal hand-action codec to bridge π₀.₅ to a 54-dimensional bimanual arm-hand interface, then combines SFT, buffered DAgger, and latent residual RL; the feed explicitly preserves the paper's single-platform, short-horizon evaluation limits.
- 2026-09-23: Added GPT-6 Sol/Luna after primary-source verification. The release halves GPT-5.6 promotional API pricing while improving agent workflow, coding, and computer-use cost efficiency; this broad AI delta displaced the narrower same-day GR00T edge-NPU story to keep the AI/Robotics feed capped at three strongest items.

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
