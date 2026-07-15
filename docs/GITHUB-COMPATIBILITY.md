# GitHub Compatibility

## What GitHub README supports

- Markdown + limited HTML (`img`, `picture`, `details`, centered headings)
- Local SVG/PNG/JPG
- SVG with CSS animation (browser-dependent)
- Mermaid (optional)
- Badges and links
- Collapsible sections

## What GitHub blocks / is unreliable for

- Arbitrary JavaScript / React / WebGL / Canvas
- iframes for apps
- Autoplay audio
- Client API keys
- Guaranteed CSS hover across themes

## Why SVG

Local, scalable, animatable without JS, size-efficient, accessible with title/desc.

## Why not WebGL / JS

Profile READMEs cannot depend on execution environments beyond GitHub’s markdown rendering.

## Simulated interactivity

- Animated SVG for presence
- Clickable links / badges
- Anchors and `details/summary`
- Action rail buttons

## Fallback behavior

Static hero + markdown text equivalents if animation fails or images fail.

## External-widget policy

Optional and secondary. Prefer local assets; never hard-code fake GitHub stats.
