# AGENTS.md

## Project
Personal GitHub Pages site for Inpyo Lee.

## Branch policy
Apply requested website changes directly to `main` unless the user explicitly requests otherwise.

## Current baseline
The site uses a minimal academic researcher layout inspired by the public information architecture of `eric-rosen/eric-rosen.github.io`, implemented with original HTML/CSS.

## Profile facts currently represented
- Name: Inpyo Lee
- Current role: Robotics & AI Research Intern @ KITECH
- Undergraduate institution: Tech University of Korea
- Major: Mechatronics Engineering
- Minor: Intelligent Robotics
- Research direction: VLM, VLA, Robot Learning, Robotic Manipulation, Embodied AI
- Current learning stage: building Deep Learning foundations while transitioning from robotics system integration toward learning-based robotics

## Homepage narrative
The homepage should communicate this trajectory:
1. Mechatronics foundation
2. ROS 2 robotics system integration
3. Perception and manipulation
4. Deep Learning / PyTorch
5. VLM, VLA, Robot Learning

Use representative technologies rather than long tool lists. Prefer ROS 2, MoveIt 2, and PyTorch as representative anchors. Avoid overemphasizing individual perception models such as YOLO in the high-level narrative.

## Content structure
- About Me
- My Path
- Research Interests
- Featured Projects
- Other Experience
- News
- Writing / Velog
- Papers & Publications
- Outside Research

## Content accuracy
- Do not describe the user as an established VLA/VLM researcher.
- Prefer language such as "interested in", "studying", "exploring", or "expanding toward" for VLM/VLA/Robot Learning.
- Distinguish actual publications from papers the user has read.
- Do not imply graduate enrollment until it begins or the user explicitly asks to state an incoming/accepted status.

## Style
- Keep the site static HTML/CSS/JS.
- Default user-facing prose to Korean.
- Keep established technical terms in English where natural.
- Preserve the sparse academic layout and avoid oversized typography.
- Personal taste can appear lightly in Outside Research; do not let it dominate the research identity.


## Interaction refinement
- Email in the profile is plain text, not a mailto link.
- Avoid copying Eric Rosen's gray collapsible bars and triangle indicators.
- Expandable secondary content uses a minimal custom `+ / −` disclosure control with thin dividers.
- The current site should increasingly diverge visually from the reference while retaining the useful sparse academic information architecture.
- GitHub/Velog links can remain text links for now. External brand icons are optional, not required assets.


## Asset update
- Profile image is stored as a normal repository asset at `images/profile.jpg`.
- Avoid embedding profile/project images as base64 data URIs in HTML.


## Notes / blog direction
- Remove Velog as a primary site dependency.
- The site now owns its long-form writing through a GitHub Pages Jekyll Notes collection.
- Add new long-form notes as Markdown under `_notes/`.
- Keep `Other Experience` permanently visible; do not hide short lists behind disclosure/toggle controls.
- Profile image must preserve its original aspect ratio using `height:auto`; do not crop it with fixed-height cover behavior.


## Layout viewport handling
- On desktop, the fixed left profile column must remain usable on short-height viewports.
- Keep the profile header fixed, but make the header itself vertically scrollable with a subtle scrollbar.
- Preserve the profile image aspect ratio and use a compact desktop width around 205px.
- On <=960px layouts, return the header to normal document flow and disable the fixed-column scrolling behavior.

## README
- README should document the current personal site purpose, directory structure, Markdown Notes workflow, basic deployment flow, and image asset policy.


## Language
- Default site language is English.
- Korean is available through an EN / KO switch at the bottom of the fixed left profile panel.
- Store the user's language choice in localStorage under `site-lang`.
- Prefer English as the canonical/default content for profile and research sections.
- Preserve technical terms in English in both languages where natural.

## Institution logos
- Institution logos should be stored as normal image assets under `images/`.
- Recommended filenames: `images/kitech-logo.png` and `images/tuk-logo.png`.
- Do not embed institution logos as base64 data URIs.


## Institution logo placement
- Use `images/kitech-logo.png` beside the KITECH affiliation.
- Use `images/tuk-logo.svg` beside Tech University of Korea.
- Keep both logos visually secondary to the profile text, aligned by height rather than fixed width.


## Responsive / zoom behavior
- Do not tune the site for a single Chrome zoom percentage.
- Use a fluid CSS Grid layout with minmax/clamp rather than fixed 860/270/500px layout widths.
- Browser zoom should naturally change the effective CSS viewport and trigger responsive breakpoints.
- Desktop: two-column profile + content layout.
- Medium widths: columns and profile image shrink fluidly.
- At <=720 CSS px: stack the profile above the content.
- Project tables become vertical cards at <=520 CSS px.
- Avoid fixed image heights; preserve intrinsic aspect ratios.


## Sidebar / logo correction
- Desktop sidebar must not have its own scrollbar.
- Keep the left profile sticky and fit its content within the viewport using compact responsive spacing and a viewport-aware profile image.
- Only the main page/document should scroll on desktop.
- Keep EN / KO at the bottom of the left profile by using flex layout with `margin-top:auto`.
- Institution logos are small affiliation badges, not hero graphics: KITECH 26x26px, TUK 28x28px.
- Increment the stylesheet query version after layout fixes to avoid stale browser cache.


## Content planning phase
- Keep the current responsive layout stable while refining content.
- Treat the homepage as a concise research profile, not a full CV.
- Prioritize: current role and trajectory, research interests, representative projects, recent activity, notes/publications, then personal interests.
- Avoid overstating VLM/VLA expertise; describe current study and transition accurately.


## Homepage content finalized for current stage
- About Me explains: current KITECH internship, Tech University of Korea background, ROS 2 autonomous/mobile robotics and manipulation experience, current Deep Learning study, and transition toward VLM/VLA/Robot Learning.
- My Path: Mechatronics -> Robotics Systems -> Robot System Integration -> Learning for Robotics.
- Research Interests: VLM, VLA, Robot Learning, Robotic Manipulation, Embodied AI.
- Featured Projects are limited to three representative projects.
- Project image asset paths are:
  - images/projects/rgbd-pick-and-place.jpg
  - images/projects/autonomous-following-robot.jpg
  - images/projects/digital-twin-logistics.jpg
- News is renamed to Recent Activity.
- Notes links to the internal Markdown/Jekyll blog.
- Papers & Publications remains intentionally lightweight until real publication/reading content is added.
- Outside Research stays short and personal.


## Complete bilingual homepage
- Every user-facing homepage label, explanatory sentence, Recent Activity item, Other Experience item, and project title/subtitle should participate in EN/KO switching.
- Official technical terms may remain in English in Korean mode when that is clearer (ROS 2, MoveIt 2, PyTorch, VLM, VLA, Robot Learning, etc.).
- Institution labels switch to Korean names in KO mode where appropriate.
- Language control is a compact rounded segmented control: EN / 한국어, with one active pill.
- Avoid flags for language selection.


## Outside Research
- Current personal interests to show: reading, playing Overwatch, and software development.
- Keep this section concise and secondary to the research profile.

## Notes design discussion
- Preferred direction: an internal research notebook/blog rather than a generic card-heavy blog.
- Notes index should prioritize readability, categories, dates, short summaries, and a calm academic visual hierarchy.
- Individual notes should support long-form Markdown reading, code blocks, figures, tables, equations, and section navigation when useful.


## Notes / Research Notebook
- Notes is Korean-first. Use a separate `notes-lang` localStorage setting with default `ko`.
- Notes index and note chrome support Korean / English segmented switching.
- Imported Notion research notes preserve the original Korean technical body unless a deliberate English translation is later added.
- Imported notes may use bilingual front matter: title_ko/title_en, summary_ko/summary_en, category_ko/category_en.
- Do not hotlink Notion's expiring signed image URLs. Replace them with placeholders and add permanent repository assets later.
- Research Notebook styling: sparse list, date/category metadata, short summaries, comfortable long-form reading, code/table/math-friendly content.


## README
- Keep README minimal and English-only.
- README should contain only a short repository/site description and a direct link to the deployed GitHub Pages site.


## Notes cache handling
- When making major Notes redesigns, bump the query version on links to /notes/ and on notes.css.
- Keep no-cache meta tags on notes/index.html to reduce stale browser rendering during active development.


## Notes link routing
- All links that navigate to the Notes index must use the canonical absolute path `/notes/?v=20260919-4` during the current cache-sensitive development phase.
- This includes homepage Notes links and note-layout links such as Notes, All Notes, and Back to Notes.
- Avoid mixed relative Notes URLs that can resolve differently depending on the current page path.


## Notes information architecture
- Notes uses a two-part information architecture: Library and Briefing.
- Library top-level folders:
  - Papers
  - Study Notes
  - Implementations
  - Project Logs
- Papers use topic metadata rather than deeper physical folders. Current topics:
  - Computer Vision
  - Transformer
  - Future: VLM/VLA, Robot Learning
- Current imported paper mapping:
  - ResNet, U-Net, DeepLabV3+ -> Papers / Computer Vision
  - Attention Is All You Need -> Papers / Transformer
- Briefing UI is reserved for future automation and currently contains no generated content.
- Planned Briefing channels:
  - AI & Robotics
  - Research Papers
- Keep human-authored Library notes visually and semantically separate from future automated Briefing content.


## Notes language and folder behavior
- Notes is Korean-only. Do not show a Korean/English language switch on the Notes index or individual note pages.
- Keep established technical terms in English where natural inside Korean notes.
- Sidebar folders should behave like a lightweight file browser.
- Parent folders with children can collapse and expand with a caret (› / ▾).
- Current Papers children: Computer Vision and Transformer.
- Preserve the Library / Briefing split.


## Notes UI language vs document language
- Notes UI supports Korean / English switching again.
- The language switch affects interface chrome only: navigation, folder labels, empty states, mode labels, and similar UI text.
- Note documents remain in their original language and must not be dynamically translated or swapped by the UI language control.
- Note titles, summaries, and bodies should render from the canonical document content as written.
- Category/topic labels may switch language because they are navigation metadata.

## Research Feed naming/order
- Rename the former Briefing area to Research Feed.
- Display Research Feed before Library in top-level navigation and sidebar order.
- Keep Library as the default active view until Research Feed has real automated content.
- Current Research Feed channels: AI & Robotics, Research Papers.


## Research Feed separation
- Research Feed is a standalone top-level page, separate from Notes.
- Homepage navigation order should prioritize Research Feed before Notes.
- Homepage includes a Research Feed entry section before Recent Activity.
- Research Feed route: /research-feed/
- Initial channels: AI & Robotics, Research Papers.
- Keep Research Feed automation disabled until the user approves the UI.

## Notes root hierarchy
- Notes no longer uses a Library top-level tab.
- All Notes is the root expandable folder.
- Under All Notes:
  - Papers
    - Computer Vision
    - Transformer
  - Study Notes
  - Implementations
  - Project Logs
- The All Notes caret collapses/expands the entire folder tree.


## Unified interaction rules
- Folder/sidebar rows are full-row interactive controls.
- Clicking a parent folder row both selects its filter and toggles its child folder visibility.
- Clicking a leaf folder row selects its filter.
- Research Feed channel rows use the same full-row hover/active/focus behavior.
- Topbar Home / Notes / Research Feed links use compact pill-like navigation styling.
- All keyboard-focusable controls must have a visible focus state.
- Notes and Research Feed share the same UI language preference key: notes-ui-lang.
- Keep control height, padding, hover, active, and focus behavior visually consistent across Notes and Research Feed.


## Homepage navigation order
- Left profile navigation order: About, Projects, Recent, Research Feed, Notes, Publications.
- Research Feed is a standalone top-level destination beside Notes, not nested inside Notes.


## Homepage top-level navigation mapping
- Sidebar navigation and homepage top-level sections must map 1:1 in the same order:
  1. About
  2. Projects
  3. Research Feed
  4. Notes
  5. Publications
- The right-side top-level heading text must match those sidebar labels.
- My Path, Research Interests, Recent Activity, and Outside Research are About subsections, not top-level navigation items.
- Sidebar links should target in-page anchors for these five homepage sections.


## Research Feed automation contract
- Research Feed is backed by the Jekyll collection `research_feed`.
- Automated posts are Markdown files under `_research_feed/`.
- Required front matter:
  - layout: feed_note
  - title
  - date
  - channel: ai-robotics or research-papers
  - channel_label: AI & Robotics or Research Papers
  - summary
- Feed articles use a concise structure:
  1. one-line takeaway
  2. 3-5 key changes
  3. Why it matters
  4. Sources
- Use @choi.openai Threads posts as discovery/context when useful, but verify factual claims against primary sources whenever possible.
- Do not copy @choi.openai's wording or exact voice; use only high-level editorial traits such as a strong takeaway, practical implications, and concise structure.


## Initial Research Feed seed
- Initial manually seeded posts:
  - 2026-09-19 AI & Robotics update
  - 2026-09-19 Research Papers update
- Seed posts establish the editorial baseline for scheduled automation.
- Korean prose is preferred for feed documents, with established technical terms kept in English.


## Research Feed timezone
- Jekyll site timezone is Asia/Seoul.
- Research Feed front matter dates must include an explicit Asia/Seoul offset, e.g. 2026-09-19 08:00:00 +0900.
- Do not use date-only front matter for Research Feed because GitHub Pages builds may treat same-day Korea posts as future documents under UTC.
