# AGENTS.md

## Project
Personal GitHub Pages site for Inpyo Lee.

## Current task
Design an AI / research briefing experience that can later accept ChatGPT-generated daily posts.

## Goal
Add a compact, high-signal briefing surface inspired by short-form AI trend posts, while keeping the existing academic robotics portfolio identity.

## Invariants
- Keep the site usable as a robotics / AI research portfolio.
- Preserve the current static HTML/CSS/JS deployment model unless a later task explicitly changes it.
- Do not introduce Codex-based content generation or publishing.
- ChatGPT is the intended source for future scheduled briefing generation.
- Existing About, Skills, Projects, Background, and Notes content must remain intact unless explicitly redesigned.
- Support both dark and light themes.

## Content direction
- Short, dense AI trend briefs: what changed, why it matters, and source links.
- Research-focused additions should prioritize LLM/agents, VLM/vision, robotics, embodied/physical AI, robot learning, Isaac Sim/Lab, and relevant papers.
- Prefer primary sources for claims when available.
- Avoid turning the site into a generic news portal.

## UI direction under evaluation
- Maintain the Minimal Academic / Robotics Lab Notebook visual language.
- Prefer editorial feed / research notebook layouts over dashboard-style metric cards.
- Each briefing item should expose date, category, title, concise summary, relevance/interpretation, and original source.
- Separate transient daily briefs from durable portfolio/project content.

## Non-goals for this task
- No automated publishing pipeline yet.
- No migration to React, Next.js, Jekyll, or another framework yet.
- No live scraping or backend service yet.

## Acceptance criteria for the design phase
- A clear location for the briefing feature in site navigation.
- A reusable post/card schema suitable for ChatGPT output.
- A mobile-friendly feed and readable detail view.
- A structure that can later be populated by simple files without rewriting the portfolio.


## Implementation status
- Branch policy: make requested website changes directly on `main`.
- Implementing a dedicated `/briefing/` feed and a portfolio entry point.
- Current phase is UI/data-contract validation only; automated publishing remains out of scope.


## Branch policy
- Always apply requested repository changes directly to `main` unless the user explicitly asks for another branch or PR.


## Current design revision
- Direction: Editorial Research Journal with subtle Lab Notebook details.
- Reduce card-heavy presentation in favor of strong typography, generous whitespace, thin rules, list-based content, and mono metadata.
- Keep the portfolio identity primary; Briefing remains a dedicated research/news surface.
- Reuse the existing static HTML/CSS/JS architecture and preserve bilingual Briefing behavior.


## Theme default
- Default visual theme is warm light, not pure white.
- Use a soft ivory/off-white background with restrained contrast.
- Dark theme remains available as an explicit user toggle.


## Modern Research Archive direction
- Treat the site as a personal research archive rather than a conventional portfolio or generic blog.
- Homepage hierarchy: identity -> current research focus -> selected work -> briefing -> notes/archive.
- Briefing should feel like a research feed, not a dashboard.
- Use warm off-white as the default background; avoid pure white.
- Prefer sans-serif editorial hierarchy, mono metadata, thin rules, flat lists, and restrained accent color.
- Minimize decorative cards, gradients, and SaaS-style UI patterns.


## Personal blog refinement
- Homepage must expose KO/EN language switching, synchronized with Briefing language preference.
- Warm light remains default, but body copy and metadata need stronger contrast than the previous archive palette.
- The homepage should feel like a personal research blog first, with latest writing and notes visibly integrated into the archive.


## Site information architecture
- Root `/` is the personal navigation hub, not the portfolio.
- `/portfolio/` contains the full portfolio/research archive.
- `/briefing/` contains AI & research news/briefings.
- Velog remains the external personal blog and must be reachable from the hub and major page headers.
- GitHub is also a first-class hub destination.
- Cross-site navigation should make Home / Portfolio / News / Velog reachable without backtracking.


## Current prioritized refinements
- Home now includes a Latest section.
- Latest AI/Research News is read dynamically from `data/briefings.json`.
- Velog is represented as the long-form notes/blog destination; do not claim an exact latest Velog post unless it has been verified or synchronized.
- Portfolio is intentionally English-only. Do not show a KO/EN toggle there unless the entire portfolio body is translated.
- Home and Briefing remain bilingual and share the saved language preference.
- Mobile navigation must keep Portfolio / News / Velog / GitHub reachable on small screens.
