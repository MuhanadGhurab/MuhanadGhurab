# Brand Guide

Locked visual system for the Muhanad Ghurab GitHub ecosystem.

## Colors

| Token | Hex | Use |
|-------|-----|-----|
| Primary deep navy | `#0F172A` | Primary surfaces |
| Near-black | `#020617` | Backgrounds, terminal panels |
| Electric blue | `#2563EB` | Accents, progress bars, crow outline |
| Cyber cyan | `#22D3EE` | Highlights, status text, nodes |
| Slate gray | `#475569` | Dividers, secondary lines |
| Light slate | `#CBD5E1` | Body text on dark |
| White | `#FFFFFF` | Primary text / name |
| Controlled amber | `#F59E0B` | Learning / in-progress only |
| Controlled violet | `#7C3AED` | Interactive/game projects only |

Do not use rainbow palettes, matrix clichés, cartoon mascots, skulls, or aggressive neon floods.

## Typography (SVG / banners)

IBM Plex Mono · JetBrains Mono · Consolas · Menlo · system monospace/sans. Do not commit font files.

## Crow mark and hero

- Primary hero (PROFILE.3): `assets/profile/cyber-crow-hero-v2.svg`
- Static fallback: `assets/profile/cyber-crow-hero-v2-static.svg` (`viewBox="0 0 1600 500"`)
- Legacy command center retained: `assets/profile/cyber-crow-command-center.svg` (not primary README hero)
- Compact mark: `assets/profile/crow-mark.svg` (+ light/dark variants)
- Animation: SVG CSS + SMIL, slow, reduced-motion safe via `<picture>` + media query
- Hero focus: crow + identity + concise status only — secondary panels are separate assets

## Charts and diagrams

- Telemetry from `data/profile-status.json` only (six primary tracks on landing)
- Never skill percentages
- Architecture: `conceptual-portfolio-architecture-v2.svg` labeled Conceptual Portfolio Architecture
- GitHub evidence from `data/github-evidence.json` only (actual public data)
- No employer/client network claims
- Contribution flight: real calendar or honest pending — never fabricated cells

## Emoji rules (README only)

At most one emoji per main heading. Never emoji-only links. Never rely on emoji in ATS PDF.

## Resume rules

Link ATS PDF only when approved file exists at `resume/Muhanad-Ghurab-ATS-Resume.pdf`.

## Accessibility and animation

- title/desc on SVGs
- Static state must carry identity
- No rapid flashing
- Prefer prefers-reduced-motion
