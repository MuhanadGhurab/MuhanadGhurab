#!/usr/bin/env python3
"""Refresh public GitHub evidence JSON (local/manual). No scheduled commits."""
from __future__ import annotations

import collections
import json
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "github-evidence.json"


def main() -> None:
    raw = subprocess.check_output(
        [
            "gh",
            "api",
            "user/repos",
            "--paginate",
            "--jq",
            "[.[] | select(.fork==false and .private==false) | {name, language, stargazers_count, archived}]",
        ],
        text=True,
    )
    repos = json.loads(raw)
    langs: collections.Counter[str] = collections.Counter()
    stars = 0
    for r in repos:
        if r.get("archived"):
            continue
        stars += int(r.get("stargazers_count") or 0)
        if r.get("language"):
            langs[r["language"]] += 1
    names = {r["name"] for r in repos}
    highlighted = [
        n
        for n in [
            "crow-ecosystem-platform",
            "enterprise-cybersecurity-lab",
            "secureskies-drone-security",
            "mini-it-cyber-projects",
            "MuhanadGhurab",
        ]
        if n in names
    ]
    out = {
        "username": "MuhanadGhurab",
        "refreshed": str(date.today()),
        "disclaimer": "Verified public GitHub evidence — forks excluded; archived excluded from language/star tallies where noted.",
        "public_repos": len(repos),
        "non_archived": len([r for r in repos if not r.get("archived")]),
        "stars_total": stars,
        "languages": dict(langs.most_common(8)),
        "highlighted_repos": highlighted,
        "method": "gh api user/repos for authenticated MuhanadGhurab public non-fork repos",
    }
    assert out["username"] == "MuhanadGhurab"
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
