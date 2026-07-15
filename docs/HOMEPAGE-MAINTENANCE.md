# Homepage Maintenance

## Updating project status

1. Change values in the `PROFILE CONFIGURATION` comment at the top of `README.md`  
2. Update matching rows in the Current operating status table  
3. Regenerate or edit `assets/learning-progress.svg` and `assets/project-status.svg` bar widths  
4. Never invent percentages — update only after verified milestones  

## Updating learning progress

- Security+ and PMP percentages change only when the owner provides updated progress  
- Status text remains **In Progress** until credentials are verified  

## Adding new repositories

1. Confirm public URL and privacy review  
2. Prefer replacing a weaker featured card over expanding beyond six  
3. Add Start Here links if role-relevant  
4. Update [`PROJECT-INVENTORY.md`](PROJECT-INVENTORY.md)  

## Removing stale projects

Remove from featured surface when links break, claims expire, or stronger evidence replaces them. Keep historical notes in inventory/changelog.

## Link checks

After edits, verify featured URLs and deep links still resolve. CI also checks required assets and forbidden certification claims.

## Visual consistency

Use locked colors from [`BRAND-GUIDE.md`](BRAND-GUIDE.md). Hero: `cyber-crow-home.svg` + static fallback. Preserve legacy crow assets until intentionally retired.

## Evidence requirements

Featured claims need repository docs, tests, CI, or architecture artifacts. Do not hard-code fragile “N tests passing” totals on the homepage.

## Claim-verification rules

Forbidden without verification:

- Senior / executive titles  
- Direct Aramco employment  
- Completed Security+ or PMP  
- Fully autonomous / production-ready drone  
- Successful AI detection as historical fact  
- Fake stars, streaks, or visitor counters  
- Skill percentages  
