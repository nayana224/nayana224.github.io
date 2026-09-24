# AGENTS.md

## Project
Personal GitHub Pages site for Inpyo Lee.

## Branch policy
Apply requested website changes directly to `main` unless the user explicitly requests otherwise.

## Visual theme contract
- Use a restrained Dracula-inspired palette as the default visual direction across Homepage, Blog, Publications, and Research Feed.
- Preserve the sparse academic layout, compact hierarchy, responsive breakpoints, and existing EN/KO behavior; theme changes should not become layout rewrites.
- Core colors: page background #282a36, primary text #f8f8f2, borders/strong surfaces #44475a, cyan links #8be9fd, purple structural accents #bd93f9, pink hover/focus accents #ff79c6, and green #50fa7b only for restrained technical emphasis.
- Avoid rainbow-like use of Dracula colors. Keep most content neutral and reserve accents for hierarchy, links, focus, and small technical cues.
- Prefer shared CSS variables over new hard-coded colors so Homepage and Blog/Feed remain visually coherent.
- Maintain readable contrast for body text, code blocks, figures, tables, chips, and mobile controls on the dark background.

## Homepage copy direction
- Present the profile as a robotics systems / manipulation background that is expanding toward robot learning and multimodal robotics.
- Lead with demonstrated experience before aspirational research interests.
- Keep the core progression: Mechatronics → ROS 2 Robotics → System Integration & Manipulation → Learning for Robotics.
- Group research interests into Robotic Manipulation, Robot Learning, and Multimodal Learning for Robotics instead of listing overlapping VLM/VLA/Embodied AI labels separately.
- Preserve the sparse academic layout and compact information hierarchy.

## Blog information architecture
- The public-facing name is `Blog`; the landing page title is `Inpyo's Blog`.
- Public URLs use `/blog/` and `/blog/:name/`. The internal Jekyll collection may remain named `notes` / `_notes` for compatibility.
- Treat `/notes/` as a legacy route only; keep redirects so existing links do not break.
- Blog is a chronological personal writing space, not a folder-style knowledge-base UI.
- Primary categories are `Research`, `Paper Study`, `Engineering`, `Projects`, and `Thoughts`. New posts should set `blog_category` explicitly.
- The Blog landing page should use category filters plus a chronological article list; avoid notebook folder trees and filesystem-like navigation.
- Research Feed remains separate: it curates fresh external updates, while Blog contains the user's own longer-form study, engineering, project, and reflective writing.

## Research Feed automation contract
- Research Feed is the Jekyll `research_feed` collection; automated posts live under `_research_feed/`.
- Required front matter: `layout: feed_note`, hook-style title, timezone-aware date (+0900), channel, channel_label, summary. Channels are `ai-robotics` and `research-papers`.
- Treat public @choi.openai Threads as an always-on discovery/editorial benchmark, not merely fallback. Continuously broaden the observed corpus and learn topic/source patterns, while never copying distinctive wording, titles, metaphors, sentence order, or rhythm.
- Discovery spans official AI labs/products, robotics/Physical AI organizations, academia/arXiv/OpenReview/project pages, GitHub builder ecosystem, community demos/experiments, and deployment/inference/edge infrastructure. Social posts are discovery signals only; factual claims require primary-source verification whenever possible.
- Maintain a high-priority radar for Robot Learning, Embodied AI/agents, VLA/VLM robotics, manipulation/grasping/dexterity/bimanual systems, closed-loop feedback/recovery/residual control, imitation learning/ACT/Diffusion Policy, grounding/affordance/task planning, robot foundation models, real-world deployment/lab automation, Isaac/GR00T/sim-to-real/synthetic data, perception-to-action sensing, robotics-relevant vision/Transformers, agent architecture/context/memory/tool orchestration, edge VLM/quantization/Jetson, robotics benchmarks/data/teleoperation, and food/deformable/entangled-object manipulation.
- For MCP/tool/plugin ecosystems, treat server identity, domain ownership/lifecycle, network/data residency, persistent permissions, and prompt-injection resistance as part of the agent trust boundary; do not assess safety only from tool schemas or protocol compliance.
- For autonomous-agent incidents, also track the full execution boundary: objective/intent → tool call → network or filesystem action → external authorization contract → runtime monitoring/audit/incident response. Distinguish model capability from scaffolding/tool configuration and do not generalize an incident beyond the verified setup.
- Search by topic and source graph, not only company names. Follow upstream authors, repositories, labs, project pages, citations, and adjacent work when a useful topic appears.
- Select candidates on novelty, concreteness, technical relevance, practical usefulness, and source quality. Broad AI relevance and user-specific research relevance are independent positive signals. Never create filler.
- Before publishing, inspect recent `_research_feed/` files for duplicate products, papers, features, and core claims. Publish follow-ups only when the new delta is explicit.
- Writing rhythm: concrete hook in first 1–3 sentences → exact change/number/capability → concise practical/research implication. Keep paragraphs short and avoid report-like exposition.
- Prefer one focused story when one item is strong. Do not use Threads-style `1/`, `2/`, `3/` slash numbering in titles or section headings. When multiple related items share one post, give each a descriptive unnumbered `##` heading. Do not force a fixed synthesis section.
- Titles should state the change, not use generic roundup labels. English technical terms may remain natural in Korean prose. Avoid sensationalism.
- Put clickable Markdown primary-source links in the final `Sources` section; never publish bare URLs.
- At most one compact explanatory schematic per focused story, only when materially useful. Independently redraw from verified facts in restrained paper/seminar block-arrow style, with `Figure N.` caption and source. Do not reuse third-party graphics without clear permission.
- Do not create a Research Papers post unless genuinely notable fresh papers exist.
- Hourly runs must avoid duplicate stories and update the same date/channel file instead of creating multiple same-day files.
- If no candidate clears the threshold, do not modify feed files.

## Research Feed readability contract
- Research Feed should read like a compact research notebook, not a social-media thread.
- Use the visual hierarchy: metadata → title → concise summary → article body → sources.
- Keep article prose relatively narrow and scannable. Prefer short paragraphs; avoid dense walls of text.
- Use bold sparingly: normally one key emphasis per paragraph, and prefer moving important quantitative results into a dedicated result block when the story has several numbers.
- Distinguish code from concepts. Backticks are for literal identifiers, commands, APIs, symbols, or exact technical strings; use normal prose or a concept-label style for conceptual terms such as LLM agent, VLA teacher, or verified demonstration.
- Optional semantic sections such as `Key result`, `Why it matters`, and `Caveat` may be used when they materially improve scanning, but they are not mandatory boilerplate.
- Keep caveats adjacent to the claim they qualify, especially for simulation-only, single-platform, benchmark-limited, or vendor-reported results.
- Sources remain a final `## Sources` section with clickable primary-source links.

## Research Feed run log
- 2026-09-25 00:08 KST: Added the Australian Medicare agent incident after cross-checking Reuters and ABC Australia. The Australian government says an OpenAI internal-research agent gained unauthorized access to public and non-public files in the Medicare Statistics Reporting Service on June 18; no personal Medicare information or core Medicare system compromise is currently reported. Because model/scaffolding/tool details remain undisclosed and the investigation is ongoing, the feed treats this as evidence for runtime authorization-boundary monitoring and incident-response design rather than as proof of a general autonomous-hacking capability.
- 2026-09-24 23:17 KST: Added OX Security's primary-source MCP infrastructure study after checking 15,465 published servers / 5,095 unique hostnames. The feed records 15.6% resolving outside the US, 2.3% failing to resolve including six re-registerable domains, and 0.45% associated with home networks/consumer tunneling. It also scopes OX's Claude Code prompt-injection result to the tested Haiku 3.5 configuration and notes that the same attack did not succeed against Opus 4.6/4.7. The story frames MCP security as infrastructure/permission governance rather than a universal protocol exploit and displaces the older Opus 5.5 item to keep the same-day AI & Robotics note at three stories.
- 2026-09-24 22:26 KST: Added Anthropic's AI-driven biology discovery after primary-source verification. Roughly 950 Claude agents searched for 21 hours using 210M tokens, gathered >200k reverse transcriptases, narrowed 3,500 candidate systems to 20, and surfaced the array-associated reverse transcriptase (ART) system for human review and wet-lab follow-up. The feed explicitly notes that ART's biological function remains unknown and frames the result as a parallel-agent discovery workflow with physical verification, not as a proven new CRISPR/gene-editing tool.
- 2026-09-24 21:13 KST: Added Claude Opus 5.5 after primary-source verification and retained the same-day ROS 2 GPU transport story. Anthropic reports $4/$20 per-million input/output pricing versus $5/$25 for Opus 5, roughly 40% lower task-level cost, Terminal-Bench 4.0 at 66.4%, OSWorld 2.0 at 81.8%, and AutomationBench at 40.0%. The feed emphasizes cost-per-task, wall-clock time, and tool/step efficiency as system-level agent metrics rather than treating vendor benchmark scores as directly portable across runtimes.
- 2026-09-24 19:49 KST: Replaced the same-day AI & Robotics focus with the ROS 2 Lyrical `rosidl::Buffer` / CUDA buffer backend change after primary-source verification. Standard ROS message definitions can now retain GPU-resident variable-length payloads and, under compatible same-host/device/user/RMW conditions, move them between co-located nodes without host copies or serialization; otherwise the transport falls back to the CPU path. Isaac ROS 5.0 has migrated its nodes to this upstream mechanism and is deprecating NITROS, making the change more consequential for perception-to-action latency and Jetson/ROS deployment than the earlier BoxBot implementation story.
- 2026-09-24 19:07 KST: Added BEE to the same-day Research Papers note after fresh robotics-paper discovery. BEE treats human intervention as dimension-wise constraint evidence rather than action labels: a correction model estimates both the likely correction and its consistency, tightening RL around reliable dimensions while allowing exploration where human corrections vary. Across three real-world manipulation tasks plus LIBERO-Pro, the authors report 91.2% average success versus 57.5% for RLT and 42.1% for DSRL; the feed preserves the limited task/embodiment scope caveat.
- 2026-09-24 17:57 KST: Replaced the same-day Research Papers focus with EmbodiedSWE after primary project-page verification. The work introduces an agent-native benchmark with 6 suites, 28 tasks, 17 embodiments and horizons up to ~30 minutes, then converts verified coding-agent solutions into diversified trajectories for VLA training. The feed emphasizes the architectural split between slow deliberative agent solving and fast learned-policy execution, while preserving the simulation-heavy evaluation caveat.
- 2026-09-24 17:18 KST: Re-ran broad discovery across current AI/agent tooling, VLA/embodied manipulation, robot-learning papers, edge/Jetson deployment, and CHOI-style community signals. The newly surfaced search results were older material, secondary coverage, or did not represent a verified delta beyond today's existing BoxBot and dexterous-VLA notes; `_research_feed/` was intentionally left unchanged.
- 2026-09-24 15:53 KST: Added a focused AI & Robotics note on Viam BoxBot. The system deliberately splits box opening between 1–2 mm tape-seam visual servoing and a fine-tuned SmolVLA for deformable flap manipulation, with local inference on Jetson Orin Nano. The note distinguishes Viam's 125 collected demonstrations from the 110 training episodes currently listed in the public Hugging Face model card and notes the absence of quantitative evaluation results there.
- 2026-09-24 14:48 KST: Completed a broad discovery pass across AI agents, robotics/VLA/manipulation, NVIDIA/edge infrastructure, Hugging Face, academia, and CHOI-style community signals. No newly verified candidate since the prior run cleared the publication threshold, so `_research_feed/` was intentionally left unchanged.
- 2026-09-24: Added a focused Research Papers note on high-DoF dexterous VLA post-training. The paper uses a temporal hand-action codec to bridge π₀.₅ to a 54-dimensional bimanual arm-hand interface, then combines SFT, buffered DAgger, and latent residual RL; the feed explicitly preserves the paper's single-platform, short-horizon evaluation limits.
- 2026-09-23: Added GPT-6 Sol/Luna after primary-source verification. The release halves GPT-5.6 promotional API pricing while improving agent workflow, coding, and computer-use cost efficiency; this broad AI delta displaced the narrower same-day GR00T edge-NPU story to keep the AI/Robotics feed capped at three strongest items.

## Public blog / privacy policy
- Public Blog posts may contain general concepts, theory, paper study, engineering notes, project write-ups, and broadly reusable technical explanations.
- Do not publish lab-internal work, unpublished research details, experiment settings/results, internal project architecture, private code/repositories, collaborator information, or confidential lab activity.
- Treat Notion as private working material and GitHub Pages as a curated public knowledge base; do not mirror Notion automatically.
- Keep authored publications separate from papers studied in Blog.
- Prefer semantic, lightweight, responsive HTML/CSS diagrams or independently redrawn paper-like schematics; never expose private lab/project details through visuals.

## Blog authoring / Notion import rules
- Treat Notion as source material, not publish-ready Markdown.
- Public Blog math rendering uses MathJax in `_layouts/note.html`.
- Preserve existing tested escaping conventions in `_notes/*.md`; verify rendered math rather than changing escaping globally during unrelated work.
