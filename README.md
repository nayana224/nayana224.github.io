# Inpyo Lee — Robotics Engineer / Researcher

Personal website for robotics projects, research interests, engineering experience, and technical notes.

**Live site:** [https://nayana224.github.io](https://nayana224.github.io)

## Overview

The site is designed as a minimal academic and engineering portfolio rather than a conventional developer landing page.

Main topics include:

- Robotic manipulation
- RGB-D perception
- ROS 2 system integration
- Robot learning
- Engineering and research notes

## Selected Work

The website currently highlights projects such as:

- QR-Based Digital Twin Logistics System
- RGB-D Robot Arm Pick-and-Place
- Autonomous Following & Towing Robot

Each project summarizes the system, contribution, technical stack, and key engineering challenges.

## Repository Structure

```text
.
├── index.html
├── css/
│   ├── variables.css
│   ├── main.css
│   ├── enhancements.css
│   └── reset.css
├── js/
│   ├── main.js
│   └── config.js
└── README.md
```

- `index.html`: page content and project details
- `css/main.css`: base layout and component styles
- `css/enhancements.css`: current academic-style visual overrides
- `css/variables.css`: shared design variables
- `js/main.js`: theme switching, navigation, and project modal interactions

## Local Preview

Clone the repository and run a small local HTTP server:

```bash
git clone https://github.com/nayana224/nayana224.github.io.git
cd nayana224.github.io
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

No build step or external framework is required.

## Deployment

GitHub Pages serves the website from the `main` branch.

After changes are reviewed and merged into `main`, the live site is updated through GitHub Pages.

For local work:

```bash
git pull origin main
```

Then edit the relevant HTML, CSS, or JavaScript files and preview them locally before publishing.

## Design Direction

The current design follows a restrained **Minimal Academic / Robotics Lab Notebook** style:

- typography and spacing over decorative cards
- neutral dark/light themes
- minimal gradients and visual effects
- project-first information hierarchy
- responsive desktop and mobile layouts

The goal is to keep the website focused on actual robotics work, technical decisions, and research direction.
