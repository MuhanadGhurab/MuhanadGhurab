# Homepage Audit — MGH.GITHUB.HOME.1

**Audited repository:** `MuhanadGhurab/MuhanadGhurab`  
**Starting HEAD:** `f817e9c`  
**Date:** 2026-07-15

## Previous structure

1. Cyber crow header (`cyber-crow-header.svg` + static fallback)
2. Identity / tagline / location / contact
3. Binary divider
4. Terminal identity block + terminal-status SVG
5. Professional overview
6. Professional highlights (bullet list)
7. Current operating status (two SVG panels + large progress table)
8. Featured portfolio (10-row table including Planned items)
9. Technical capabilities (dense ·-separated lists)
10. Current learning
11. GitHub metrics (link list)
12. Contact
13. Collapsed portfolio notes

## Problems found

| Issue | Detail |
|-------|--------|
| Weak hierarchy for recruiters | Progress and highlights appear before strongest projects |
| Featured table too long | 10 rows including Planning placeholders dilute strongest work |
| Crow Ecosystem featured first | Strong cybersecurity evidence (lab, SecureSkies, triage) should lead |
| Duplicate narrative | Terminal block + highlights + overview repeat the same facts |
| Excess scrolling | Two full progress SVGs + markdown table + 10-row feature table |
| Progress inconsistency | Config comment said Portfolio Foundation 60%; SecureSkies docs already 75% |
| No recruiter “Start Here” paths | Visitors must invent their own browsing order |
| Table-heavy mobile risk | Featured portfolio wide HTML table |
| Missing homepage architecture docs | No visitor-journey documentation |
| Badge discipline | Already low (good); keep avoiding badge walls |
| Crow asset naming | Hero not yet named for homepage rebuild (`cyber-crow-home.svg`) |

## Broken links found

None in current README (featured public repo URLs resolve). Planned rows correctly unlinked.

## Outdated claims found

| Claim | Finding |
|-------|---------|
| “SecSky documentation deferred” in older changelog/roadmap notes | Superseded by public `secureskies-drone-security` |
| Portfolio Foundation 60% | Understates completed 4A–4C + public repos; update to 75% |
| Featured order prioritizing Crow | Recruiter landing should lead with lab security evidence |

## Content preserved

- Professional identity and tagline
- Tekfen IT Specialist role
- Aramco association wording (environment — not employment)
- Security+ / PMP In Progress
- SecureSkies honest status + Second Place qualifier
- Privacy boundaries reference
- Existing crow brand language and color system
- Old crow assets kept as legacy until new hero validated

## Content removed / demoted (in rebuild)

- Long 10-row featured table with Planning stubs (moved to maintenance/inventory)
- Dense “program notes” details as primary surface (kept as docs links)
- Duplicate progress presentation (one consolidated panel + key markdown rows)
- Crow-first featured order

## Hierarchy decisions

1. Hero identity first (5–10 second read)
2. Snapshot strip
3. Compact terminal
4. Overview (~100 words)
5. Featured six (lab → SecureSkies → mini → Crow → Event Triage → Interview/Evidence)
6. Evidence strip
7. Capability matrix (no skill percentages)
8. Project/learning progress only
9. Learning explanations
10. Achievements
11. Recruiter Start Here
12. Contact

## Mobile findings

- Avoid wide feature tables → use list/card markdown
- Keep snapshot and evidence as mobile-safe SVGs with large type
- Hero must remain readable without animation

## Accuracy findings

- No Security+/PMP completion claims present (keep)
- No direct Aramco employment claim present (keep)
- SecureSkies wording must remain partially integrated / not fully deployed
- Screenshots-pending for lab evidence remains honest
