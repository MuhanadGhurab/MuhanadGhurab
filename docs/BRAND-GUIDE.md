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
| Controlled amber | `#F59E0B` | Optional secondary accent only |

Do not use rainbow palettes, matrix clichés, cartoon mascots, or aggressive skull imagery.

## Typography (SVG / banners)

Prefer (referenced by name only — do not redistribute font files):

- IBM Plex Mono
- JetBrains Mono
- Consolas
- System monospace fallback

## Crow mark

- Original geometric cyber crow
- Binary accents and network nodes allowed
- Animation: SVG/CSS only, controlled, reduced-motion friendly
- Always ship a static fallback

## Domain banner accents

| Domain | Accent pairing |
|--------|----------------|
| Cybersecurity | Cyan + electric blue |
| Infrastructure | Blue + slate |
| Python | Blue + controlled amber |
| Java | Blue + muted orange |
| Drone | Blue + aviation cyan |
| Robotics | Cyan + steel gray |
| Games | Blue + controlled violet |
| Crow Ecosystem | Deep navy + cyan + electric blue |

## Status labels

Use only:

Planning · Scaffolded · Active Development · Functional Prototype · Documentation Complete · Release Candidate · Archived · Private Architecture Summary

Do not label work Production Ready without documented criteria.

## Accessibility

- Meaningful `title` / `desc` on SVGs
- Do not rely on animation for essential information
- Sufficient contrast on navy backgrounds
- Prefer `prefers-reduced-motion` support
- Social preview text must remain readable when scaled down
