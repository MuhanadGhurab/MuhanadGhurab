# Hero Design Decision — MGH.GITHUB.PROFILE.3

## Design objective

One memorable animated cyber-crow hero plus multiple large modular panels. No micro-dashboard cramming inside a single `1800×640` asset.

## PROFILE.2 lesson retained

Command-center branding and binary crow identity remain the brand core.

## PROFILE.2 lesson rejected for the hero

Packing architecture, telemetry, navigation, and dense status into the same hero SVG. At GitHub profile scale those layers become visually quiet.

## Concepts explored (PROFILE.3)

1. **Sentinel Crow** — large crow left; identity right; thin status only
2. **Binary Flight** — strong feather data-flow and particle drift
3. **Enterprise Guardian** — crow with small protected-core symbol

## Selected composition

**Sentinel Crow** with Binary Flight motion layers.

Primary assets:

- `assets/profile/cyber-crow-hero-v2.svg` (`viewBox="0 0 1600 500"`)
- `assets/profile/cyber-crow-hero-v2-static.svg`

Crow target share: ~35–45% of hero width. Float amplitude: ~12 SVG units.

## Modular panels extracted from the old command center

| Panel | Asset |
|-------|-------|
| Operations illustration | `cyber-crow-operations.svg` |
| Architecture | `conceptual-portfolio-architecture-v2.svg` |
| Telemetry (top 6 tracks) | `portfolio-telemetry-v2.svg` |
| GitHub evidence | `assets/generated/github-evidence.svg` |
| Contribution flight | `assets/generated/cyber-crow-contribution-flight.svg` (honest pending until real calendar pull) |

## Legacy assets

`cyber-crow-command-center.svg` and related PROFILE.2 panels retained for history/tests; README no longer embeds the overcrowded hero as the primary experience.

## Reduced motion

`<picture>` prefers static hero when `prefers-reduced-motion: reduce`. Animated SVG also disables CSS keyframes under the same media query; SMIL may still be limited by the UA — static fallback remains the guaranteed quiet path.

## Performance

Hero targets: animated &lt; 350 KB, static &lt; 250 KB (current generated assets are well under).
