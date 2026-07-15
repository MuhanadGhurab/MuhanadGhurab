# Animation Rebuild Decision — MGH.GITHUB.PROFILE.3

## 1. Existing animation behavior

Current `cyber-crow-command-center.svg` uses CSS `@keyframes` (float ~8px, pulse, stream, orbit, scan, trace). Crow shares space with architecture, telemetry, navigation, and dense labels on `1800×640`.

## 2. Existing weaknesses

- **Information cramming:** crow + identity + orbit + mini bars + nav rail in one asset  
- **Amplitude too small:** float ±8 units is hard to notice after GitHub downscales  
- **Crow scale too small:** ~30–35% effective width after competing panels  
- **Microtext dies at profile scale**  
- **Motion density without clarity:** many tiny effects instead of few large ones  
- **Picture reduced-motion source** may prefer static for some users (acceptable) but animated default still looks quiet after scale

## 3. GitHub compatibility findings

- Prefer **SMIL + CSS** dual animation so at least one path runs in Chromium/`<img>` embedding  
- Avoid depending on heavy filters/blur  
- Do not rely on animation for essential text (keep Markdown identity)

## 4. Three concepts explored

1. **Sentinel Crow** — crow dominates left; identity right; minimal status  
2. **Binary Flight** — strong wing binary rivers + particle drift  
3. **Enterprise Guardian** — crow + protected core micro-symbol (still simple)

## 5. Selected concept

**Sentinel Crow** with Binary Flight motion layers (larger float, visible binary feathers, eye pulse, circuit trace, scan, nodes).

## 6–12. System notes

- Timing: float 7s · eye 4s · binary 8–10s · scan 12s · nodes staggered 4s  
- Scaling: crow ~40% of 1600×500 canvas  
- Reduced motion: CSS media + static SVG via `<picture>`  
- Static fallback: polished full composition without continuous motion  
- Performance: keep under 350 KB  
- Originality: geometric crow; no Tux/reference paths

## 13. Existing asset classification

| Asset | Classification |
|-------|----------------|
| `cyber-crow-command-center.svg` | E — Retire from README primary use; keep for legacy |
| `cyber-crow-command-center-static.svg` | E — Legacy static |
| `enterprise-orbit-diagram.svg` | C → replaced by `conceptual-portfolio-architecture-v2.svg` |
| `portfolio-telemetry.svg` | C → replaced by `portfolio-telemetry-v2.svg` (top 6) |
| `security-status.svg` | E — Retire from landing |
| `project-navigation.svg` | E — Retire from landing (Markdown rail/links) |
| `crow-mark*.svg` | A — Preserve |
| `binary-divider.svg` | B — Optional separator (unused if HR sufficient) |
| New hero v2 / ops / arch / evidence / flight | D/new primary set |

## 14. Originality review

No reference penguin paths, snake contribution code, badge rows, or wording copied from TroyMitchell911. Principles adapted: modular rhythm, larger character, grouped badges, real stats, lower contribution visual.
