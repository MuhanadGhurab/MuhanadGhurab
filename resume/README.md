# Resume

## Purpose

Recruiter-facing ATS résumé for Muhanad Ghurab, aligned with the GitHub profile command center.

## Current version

**1.0.0** — 2026-07-15

## Files

| File | Purpose |
|------|---------|
| [Muhanad-Ghurab-ATS-Resume.pdf](./Muhanad-Ghurab-ATS-Resume.pdf) | Primary ATS PDF |
| [Muhanad-Ghurab-ATS-Resume.docx](./Muhanad-Ghurab-ATS-Resume.docx) | Editable OpenXML source export |
| [Muhanad-Ghurab-ATS-Resume-preview.png](./Muhanad-Ghurab-ATS-Resume-preview.png) | Full-page visual preview only |
| [ATS-CHECK.md](./ATS-CHECK.md) | Validation record |
| [source/resume-data.json](./source/resume-data.json) | Shared structured source of truth |
| [scripts/build_resume.py](./scripts/build_resume.py) | Deterministic builder |

## Accuracy statement

- CompTIA Security+ and PMP are listed as **In Progress**.
- The résumé does **not** imply direct employment by Saudi Aramco.
- Content is generated from the shared structured source (`resume-data.json`).
- SecureSkies / SecSky is described as a university project with documented historical/public boundaries.

## Privacy statement

No date of birth, national ID, full residential address, salary, or confidential employer systems are included.

## Build

```bash
python resume/scripts/build_resume.py
python resume/tests/test_resume.py
```

## Update instructions

1. Edit `source/resume-data.json`
2. Rebuild with `python resume/scripts/build_resume.py`
3. Re-run tests
4. Commit PDF, DOCX, preview, and source together
