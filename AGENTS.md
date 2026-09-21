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
- Do not keep a generic Recent Activity block on the homepage; only reintroduce it later if there are concrete dated updates worth surfacing.
- Keep authored publications and research outputs separate from papers studied in Notes.
- Homepage Research Feed copy must reflect that the feed automation is already active.
- Preserve the sparse academic layout and top-level navigation while keeping the homepage information hierarchy compact.
- Put Projects immediately after Research Interests; keep Outside Research near the end of the homepage.
- Keep homepage Projects text-first: do not render project thumbnail images. Show project title, category, concise description, and stack, then link the section to the public GitHub profile rather than guessing private or ambiguous per-project repository URLs.
- Group Research Feed, Notes, and Publications visually as compact destination rows while preserving their individual anchors and pages.

## Research Feed automation contract
- Research Feed is backed by the Jekyll collection `research_feed`.
- Automated posts are Markdown files under `_research_feed/`.
- Required front matter: layout: feed_note, title, timezone-aware date, channel, channel_label, summary.
- Channels: ai-robotics and research-papers.
- Jekyll timezone is Asia/Seoul; feed dates must include +0900.
- Use public @choi.openai Threads posts for discovery/context when useful, then verify factual claims against primary sources whenever possible.
- If ordinary primary-source discovery yields no publishable update, use recent public @choi.openai Threads posts as a fallback discovery queue: select an unduplicated relevant topic, independently verify it against primary/reliable sources, and rewrite it from scratch. Never use the Threads wording as the final factual source or imitate distinctive phrasing.
- Treat @choi.openai as an editorial reference for topic discovery and structural patterns, not as prose to imitate verbatim.
- Target feed rhythm: concrete hook first, then the exact change/number/product, then one concise practical implication. Keep paragraphs short and avoid report-like exposition.
- For a single strong story, prefer one focused short-form update. For multiple related stories, use `1/`, `2/`, `3/` thread-style sections.
- Titles should communicate the change itself rather than generic labels such as daily roundup. Avoid forced sensationalism; one restrained emoji in the opening is optional when it genuinely fits.
- Do not force a fixed `Why it matters` or `지금 봐야 할 포인트` section. Add synthesis only when it improves understanding.
- Keep source verification rigorous even when the visible post is short: social posts are discovery signals, while primary sources support factual claims.
- Broaden discovery beyond only frontier-model launches to useful AI workflow, coding-agent, robotics/Physical AI, open-source, benchmark, and deployment changes that a technical reader would plausibly want to know that day.
- Never copy a creator's distinctive wording or exact voice.
- Use a concrete hook in the first 1-3 sentences, short paragraphs, thread-like 1/ 2/ 3/ sections for multi-item updates, implications immediately after facts, and a short '지금 봐야 할 포인트' synthesis.
- Prefer numbers, product changes, research/workflow implications, and explicit caveats over abstract trend language.
- All external sources must be clickable Markdown hyperlinks; never publish bare URLs.
- Research Feed may include at most one compact explanatory schematic per focused story when a visual materially improves comprehension. Build the schematic from verified facts in the linked primary source; do not copy a news graphic or social-media image merely for decoration.
- Research Feed visuals should use the same paper-like block/arrow visual grammar as Notes, remain short enough for mobile, and include a caption plus source link. Prefer original redraws over rehosting third-party graphics unless reuse rights are explicit.
- Do not create a Research Papers post unless there are genuinely notable papers in the requested freshness window.
- Hourly runs must avoid duplicate stories; update the same date/channel file rather than creating multiple same-day files.

## Research Feed run log
- 2026-09-19 08:38 +0900: refreshed `_research_feed/2026-09-19-ai-robotics.md` with Anthropic internal AI-R&D measurements, Jetson Orin Nano 2 edge-AI performance, and Spirit AI real-world humanoid learning/deployment. No separate Research Papers post was added because the last-24-hour search did not surface a sufficiently strong primary-source paper update.
- 2026-09-19 11:30 +0900: added Anthropic × Accenture embedded evaluation to the existing AI & Robotics daily file after confirming Anthropic's Sep 18 announcement. The partnership commits at least $1B from each company over five years and places independent evaluators inside Anthropic with employee-comparable access. No duplicate daily file was created.
- 2026-09-19 hourly check: searched current OpenAI, Anthropic, Google DeepMind, NVIDIA and recent VLA/robotics sources. No new item cleared the significance and freshness threshold beyond stories already present in the Sep 19 feed, so no Research Feed post was created or modified.
- 2026-09-19 latest hourly check: rechecked public discovery sources plus current OpenAI, Anthropic, Google DeepMind, NVIDIA, Reuters/news coverage, and recent VLA/robotics papers. Results were duplicates of the existing Anthropic R&D/embedded-evaluation items, older robotics material, event notices, or lower-signal updates; no feed file was modified.
- 2026-09-19 current hourly check: checked fresh AI/Robotics reporting, primary-source domains, public discovery sources, and recent VLA papers. The Anthropic × Accenture item was already in today's feed; other surfaced items were duplicate, older than the freshness window, event-only, or lacked sufficient primary-source confirmation/significance. No Research Feed file was modified.
- 2026-09-19 latest run: rechecked fresh OpenAI, Anthropic, Google DeepMind, NVIDIA, arXiv robotics/VLA, and public @choi.openai discovery results. The only fresh high-signal primary-source result was Anthropic × Accenture embedded evaluation, which is already present in today's feed. Other surfaced material was older or duplicate, so no `_research_feed/` file was modified.
- 2026-09-19 hourly run: checked fresh AI/Robotics news and primary-source domains again. Spirit AI and Anthropic × Accenture were already present in today's feed; OpenAI robotics hiring coverage lacked a new first-party announcement, while other surfaced DeepMind/NVIDIA items were older than the freshness window. No Research Feed file was modified.
- 2026-09-19 newest hourly run: rechecked OpenAI, Anthropic, Google DeepMind, NVIDIA, arXiv VLA/robotics, and public @choi.openai discovery results. The only fresh primary-source hit was Anthropic × Accenture embedded evaluation, already recorded in today's feed; other results were older or duplicates. No `_research_feed/` file was modified.

- 2026-09-21 manual test run: searched fresh AI/Robotics and coding-agent updates, checked existing feed files for duplication, and published `_research_feed/2026-09-21-ai-robotics.md` covering Anthropic's redesigned Claude Code Projects beta. Primary confirmation came from Anthropic's current Projects help documentation; The Verge was used as secondary context. No separate Research Papers file was created.

## Public notes / privacy policy
- Public Notes may contain general concepts, theory, paper study, and broadly reusable technical explanations derived from the user's personal study notes.
- Do not publish lab-internal work, unpublished research details, experiment settings/results, internal project architecture, private code/repositories, collaborator information, or other information that could reveal confidential lab activity.
- When a Notion page mixes general theory with lab/project context, extract only the standalone public-safe concept and rewrite it independently; omit the lab/project context entirely.
- Treat Notion as a private working notebook and GitHub Pages as a curated public knowledge base. Do not mirror Notion automatically.
- Use the Notes library type `concept` for public concept/theory articles. Keep Papers for paper reading notes and Implementations for reproducible public implementation notes. Do not expose a Project Logs category in public Notes.
- Concept/theory notes should use reusable HTML/CSS visualization blocks when they materially improve comprehension: callouts for key takeaways, comparison cards for contrasts, concept cards for components, flow diagrams for process/agent loops, and hierarchy blocks for layered systems.
- Keep visualizations semantic, lightweight, responsive, and compatible with the sparse academic Notes design. Prefer HTML/CSS over decorative images for conceptual diagrams, and never expose private lab/project details through diagrams.
- Visual style should blend two layers: compact explanatory cards for definitions/comparisons and paper-like schematic figures for architecture, data flow, mechanisms, or equations. Do not force every concept into cards.
- Paper-like figures should follow the visual grammar of the user's VLM seminar reference: restrained colors, rectangular modules, directional arrows, explicit input/output labels, short annotations, and a figure caption. Reuse only the visual grammar, never confidential lab content.
- For paper-derived Notes, locate and link the original paper/project URL. Prefer independently redrawn schematics that explain the mechanism while citing the source. Reuse an original paper figure only when its license/reuse terms clearly permit it; otherwise do not rehost it.
- When redrawing from a paper, use captions such as `Figure N. ... (adapted from <paper>)` and include the paper URL in References.


## Notes authoring / Notion import rules
- Treat Notion as source material, not publish-ready Markdown. Never copy Notion math delimiters or HTML blindly into public Notes.
- Public Notes math rendering uses MathJax in `_layouts/note.html`.
- Because Jekyll/Kramdown consumes one level of backslash escaping, canonical source syntax stored in `_notes/*.md` is `\\\\(...\\\\)` for inline math. The rendered HTML must contain `\\(...\\)` for MathJax.
- Canonical display math source syntax is `\\\\[...\\\\]` on its own block so Jekyll renders `\\[...\\]` into HTML for MathJax. Example source:
  ```text
  \\\\[
  \\operatorname{Attention}(Q,K,V)=\\operatorname{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V
  \\\\]
  ```
- Do not publish raw `$...# AGENTS.md

## Project
Personal GitHub Pages site for Inpyo Lee.

## Branch policy
Apply requested website changes directly to `main` unless the user explicitly requests otherwise.


## Homepage copy direction
- Present the profile as a robotics systems / manipulation background that is expanding toward robot learning and multimodal robotics.
- Lead with demonstrated experience before aspirational research interests.
- Keep the core progression: Mechatronics → ROS 2 Robotics → System Integration & Manipulation → Learning for Robotics.
- Group research interests into Robotic Manipulation, Robot Learning, and Multimodal Learning for Robotics instead of listing overlapping VLM/VLA/Embodied AI labels separately.
- Do not keep a generic Recent Activity block on the homepage; only reintroduce it later if there are concrete dated updates worth surfacing.
- Keep authored publications and research outputs separate from papers studied in Notes.
- Homepage Research Feed copy must reflect that the feed automation is already active.
- Preserve the sparse academic layout and top-level navigation while keeping the homepage information hierarchy compact.
- Put Projects immediately after Research Interests; keep Outside Research near the end of the homepage.
- Keep homepage Projects text-first: do not render project thumbnail images. Show project title, category, concise description, and stack, then link the section to the public GitHub profile rather than guessing private or ambiguous per-project repository URLs.
- Group Research Feed, Notes, and Publications visually as compact destination rows while preserving their individual anchors and pages.

## Research Feed automation contract
- Research Feed is backed by the Jekyll collection `research_feed`.
- Automated posts are Markdown files under `_research_feed/`.
- Required front matter: layout: feed_note, title, timezone-aware date, channel, channel_label, summary.
- Channels: ai-robotics and research-papers.
- Jekyll timezone is Asia/Seoul; feed dates must include +0900.
- Use public @choi.openai Threads posts for discovery/context when useful, then verify factual claims against primary sources whenever possible.
- If ordinary primary-source discovery yields no publishable update, use recent public @choi.openai Threads posts as a fallback discovery queue: select an unduplicated relevant topic, independently verify it against primary/reliable sources, and rewrite it from scratch. Never use the Threads wording as the final factual source or imitate distinctive phrasing.
- Treat @choi.openai as an editorial reference for topic discovery and structural patterns, not as prose to imitate verbatim.
- Target feed rhythm: concrete hook first, then the exact change/number/product, then one concise practical implication. Keep paragraphs short and avoid report-like exposition.
- For a single strong story, prefer one focused short-form update. For multiple related stories, use `1/`, `2/`, `3/` thread-style sections.
- Titles should communicate the change itself rather than generic labels such as daily roundup. Avoid forced sensationalism; one restrained emoji in the opening is optional when it genuinely fits.
- Do not force a fixed `Why it matters` or `지금 봐야 할 포인트` section. Add synthesis only when it improves understanding.
- Keep source verification rigorous even when the visible post is short: social posts are discovery signals, while primary sources support factual claims.
- Broaden discovery beyond only frontier-model launches to useful AI workflow, coding-agent, robotics/Physical AI, open-source, benchmark, and deployment changes that a technical reader would plausibly want to know that day.
- Never copy a creator's distinctive wording or exact voice.
- Use a concrete hook in the first 1-3 sentences, short paragraphs, thread-like 1/ 2/ 3/ sections for multi-item updates, implications immediately after facts, and a short '지금 봐야 할 포인트' synthesis.
- Prefer numbers, product changes, research/workflow implications, and explicit caveats over abstract trend language.
- All external sources must be clickable Markdown hyperlinks; never publish bare URLs.
- Do not create a Research Papers post unless there are genuinely notable papers in the requested freshness window.
- Hourly runs must avoid duplicate stories; update the same date/channel file rather than creating multiple same-day files.

## Research Feed run log
- 2026-09-19 08:38 +0900: refreshed `_research_feed/2026-09-19-ai-robotics.md` with Anthropic internal AI-R&D measurements, Jetson Orin Nano 2 edge-AI performance, and Spirit AI real-world humanoid learning/deployment. No separate Research Papers post was added because the last-24-hour search did not surface a sufficiently strong primary-source paper update.
- 2026-09-19 11:30 +0900: added Anthropic × Accenture embedded evaluation to the existing AI & Robotics daily file after confirming Anthropic's Sep 18 announcement. The partnership commits at least $1B from each company over five years and places independent evaluators inside Anthropic with employee-comparable access. No duplicate daily file was created.
- 2026-09-19 hourly check: searched current OpenAI, Anthropic, Google DeepMind, NVIDIA and recent VLA/robotics sources. No new item cleared the significance and freshness threshold beyond stories already present in the Sep 19 feed, so no Research Feed post was created or modified.
- 2026-09-19 latest hourly check: rechecked public discovery sources plus current OpenAI, Anthropic, Google DeepMind, NVIDIA, Reuters/news coverage, and recent VLA/robotics papers. Results were duplicates of the existing Anthropic R&D/embedded-evaluation items, older robotics material, event notices, or lower-signal updates; no feed file was modified.
- 2026-09-19 current hourly check: checked fresh AI/Robotics reporting, primary-source domains, public discovery sources, and recent VLA papers. The Anthropic × Accenture item was already in today's feed; other surfaced items were duplicate, older than the freshness window, event-only, or lacked sufficient primary-source confirmation/significance. No Research Feed file was modified.
- 2026-09-19 latest run: rechecked fresh OpenAI, Anthropic, Google DeepMind, NVIDIA, arXiv robotics/VLA, and public @choi.openai discovery results. The only fresh high-signal primary-source result was Anthropic × Accenture embedded evaluation, which is already present in today's feed. Other surfaced material was older or duplicate, so no `_research_feed/` file was modified.
- 2026-09-19 hourly run: checked fresh AI/Robotics news and primary-source domains again. Spirit AI and Anthropic × Accenture were already present in today's feed; OpenAI robotics hiring coverage lacked a new first-party announcement, while other surfaced DeepMind/NVIDIA items were older than the freshness window. No Research Feed file was modified.
- 2026-09-19 newest hourly run: rechecked OpenAI, Anthropic, Google DeepMind, NVIDIA, arXiv VLA/robotics, and public @choi.openai discovery results. The only fresh primary-source hit was Anthropic × Accenture embedded evaluation, already recorded in today's feed; other results were older or duplicates. No `_research_feed/` file was modified.

- 2026-09-21 manual test run: searched fresh AI/Robotics and coding-agent updates, checked existing feed files for duplication, and published `_research_feed/2026-09-21-ai-robotics.md` covering Anthropic's redesigned Claude Code Projects beta. Primary confirmation came from Anthropic's current Projects help documentation; The Verge was used as secondary context. No separate Research Papers file was created.

## Public notes / privacy policy
- Public Notes may contain general concepts, theory, paper study, and broadly reusable technical explanations derived from the user's personal study notes.
- Do not publish lab-internal work, unpublished research details, experiment settings/results, internal project architecture, private code/repositories, collaborator information, or other information that could reveal confidential lab activity.
- When a Notion page mixes general theory with lab/project context, extract only the standalone public-safe concept and rewrite it independently; omit the lab/project context entirely.
- Treat Notion as a private working notebook and GitHub Pages as a curated public knowledge base. Do not mirror Notion automatically.
- Use the Notes library type `concept` for public concept/theory articles. Keep Papers for paper reading notes and Implementations for reproducible public implementation notes. Do not expose a Project Logs category in public Notes.
- Concept/theory notes should use reusable HTML/CSS visualization blocks when they materially improve comprehension: callouts for key takeaways, comparison cards for contrasts, concept cards for components, flow diagrams for process/agent loops, and hierarchy blocks for layered systems.
- Keep visualizations semantic, lightweight, responsive, and compatible with the sparse academic Notes design. Prefer HTML/CSS over decorative images for conceptual diagrams, and never expose private lab/project details through diagrams.
 or `$...$` delimiters. These are considered import artifacts and must be normalized before commit.
- Do not mix heading/list Markdown inside an open math block. Close `\\]` before the next heading, list, table, or paragraph.
- MathJax skips `pre` and `code` tags; use code blocks only for pseudocode/code, never for equations that should render mathematically.
- Preserve LaTeX commands such as `\\frac`, `\\sqrt`, `\\operatorname`, `\\text`, matrices, subscripts, and superscripts inside MathJax delimiters.
- After importing or rewriting a Notion note, run a content audit before publishing:
  1. zero raw dollar-sign math delimiters remain,
  2. source `\\\\(` / `\\\\)` and `\\\\[` / `\\\\]` delimiters are balanced and survive the Jekyll build as `\\(` / `\\)` and `\\[` / `\\]`,
  3. no heading/list/table is accidentally inside display math,
  4. no temporary Notion image/file URL remains,
  5. no lab/private/project-sensitive term or context is exposed,
  6. visual HTML blocks remain responsive and semantic,
  7. front matter matches the Notes category/type contract.
- For concept-heavy articles, convert suitable structures into reusable HTML/CSS callout, comparison, concept, flow, hierarchy, or pipeline blocks instead of publishing dense raw Notion prose.
- For paper notes, add a compact visual summary near the top when it improves comprehension, but keep the original technical detail below it.
- The preferred import workflow is: Notion source → extract public-safe content → normalize math → restructure prose → add visual blocks → audit math/privacy/links → commit to `_notes/`.

## Site invariants
- Keep Research Feed separate from Notes at `/research-feed/`.
- Keep homepage top-level navigation mapping: About, Projects, Research Feed, Notes, Publications.
- Notes document content remains independent of the Notes UI language switch.
- Preserve the sparse academic layout and existing responsive behavior.
- Do not overstate the user's VLM/VLA expertise; use studying/exploring/expanding-toward language where relevant.
- Keep Publications for work the user has authored or directly contributed to; studied papers belong in Notes.

## Site change log
- 2026-09-20: began homepage copy refinement to foreground proven robotics systems/manipulation experience, clarify the transition toward robot learning and multimodal robotics, remove duplicated interest labels, and align Research Feed/Publications copy with the site's current state.
- 2026-09-20: removed the VLM Task Monitoring item from homepage Recent Activity at the user's request; keep project-specific experimental work out of the homepage summary unless explicitly promoted later.

- 2026-09-20: approved visual hierarchy cleanup without changing project images: remove generic Recent Activity, move Projects directly after Research Interests, move Outside Research to the bottom, remove duplicate Notes link from the sidebar social row, soften sidebar navigation emphasis, and compact Research Feed / Notes / Publications on the homepage.

- 2026-09-21: changed homepage Projects to a text-only presentation and added a single public GitHub profile link below the project list; project image assets may remain in the repository but are not rendered on the homepage.

- 2026-09-21: Research Feed automation was re-enabled. Editorial direction was refined after reviewing public references to @choi.openai: shorter concrete hooks, denser factual payload, more frequent useful updates, optional numbered thread structure, and less report-style commentary while retaining primary-source verification.

- 2026-09-21: Research Feed fallback policy updated: when ordinary fresh-source discovery yields nothing worth publishing, inspect recent @choi.openai topics for missed relevant items, then independently verify and reconstruct them before posting.

- 2026-09-21: approved a public Concepts & Theory direction for Notes. Lab-internal and project-sensitive material is explicitly excluded; only standalone public-safe theory/concepts may be distilled from private Notion notes.

- 2026-09-21: Notes navigation was simplified to Papers, Concepts & Theory, and Implementations; Project Logs was removed from the public Notes sidebar. Published the first public-safe concept article, `_notes/llm-agent-model-tools-state-loop.md`, distilled from private study notes with all lab-specific context removed.

- 2026-09-21: approved reusable HTML/CSS concept visualizations in public Notes; the first LLM Agent concept article will be upgraded with callouts, cards, comparisons, and flow diagrams while preserving responsive/mobile readability.

- 2026-09-21: completed the Notes visualization rollout: added reusable callout/card/flow/hierarchy/pipeline CSS, upgraded the LLM Agent article, added a separate Context vs Context Window concept article, and added visual summaries to ResNet, U-Net, DeepLabV3+, and Attention Is All You Need notes.

- 2026-09-21: standardized Notes math rendering on MathJax using `\\(...\\)` and `\\[...\\]`; raw `$`/`$$` delimiters are forbidden in published Notes. Existing ResNet, U-Net, and Transformer math was normalized and the malformed Transformer attention blocks were repaired.

- 2026-09-21: verified the deployed GitHub Pages artifact directly. Visual HTML blocks were present, but Kramdown consumed single-backslash MathJax delimiters. Updated all math-bearing Notes to double-escaped source delimiters so rendered HTML preserves MathJax syntax.

- 2026-09-21: refined visualization policy to combine explanatory cards with paper-style schematics. Paper/source URLs should be linked directly; original figures are reused only when licensing clearly permits, otherwise redraw with attribution. Research Feed may use one compact source-grounded schematic when it improves understanding.

- 2026-09-21: rolled paper-style figures through the remaining public Notes and existing Research Feed entries: ResNet, U-Net, DeepLabV3+, Transformer, LLM Agent, Context/Context Window, Sep 19 AI/Robotics, and Sep 19 Research Papers. Paper notes now include direct original-paper links and independent redraws; explanatory cards remain where they help definitions/comparisons.

- 2026-09-21: completed mobile-oriented Notes QA and cross-linking. Paper figures keep local horizontal scrolling on small screens with improved touch behavior/caption sizing; Transformer display-math remnants were repaired; related-note links now connect Transformer↔Attention, Agent↔Context, U-Net↔DeepLabV3+, and ResNet↔DeepLabV3+.
