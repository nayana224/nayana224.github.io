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
