#!/usr/bin/env python3
"""Deterministic renderer for profile telemetry and companion panels."""
from __future__ import annotations

import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "profile-status.json"
OUT = ROOT / "assets" / "profile"

COLORS = {
    "bg": "#020617",
    "navy": "#0F172A",
    "blue": "#2563EB",
    "cyan": "#22D3EE",
    "slate": "#475569",
    "light": "#CBD5E1",
    "white": "#FFFFFF",
    "amber": "#F59E0B",
}


def load_tracks() -> dict:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    for t in data["tracks"]:
        v = t["value"]
        if not isinstance(v, (int, float)) or v < 0 or v > 100:
            raise SystemExit(f"Invalid progress value for {t['id']}: {v}")
        t["label"] = str(t["label"])[:80]
        t["status"] = str(t["status"])[:60]
    return data


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def render_telemetry(data: dict) -> str:
    tracks = data["tracks"][:10]
    height = 80 + len(tracks) * 36
    rows = []
    y = 70
    for t in tracks:
        val = int(t["value"])
        bar_w = int(980 * val / 100)
        color = COLORS["amber"] if "Learning" in t["label"] or t["id"] in {"security-plus", "pmp"} else COLORS["blue"]
        rows.append(
            f'<text x="40" y="{y}" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="{COLORS["light"]}">{esc(t["label"])}</text>'
            f'<text x="1040" y="{y}" text-anchor="end" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="{COLORS["cyan"]}">{val}%</text>'
            f'<rect x="40" y="{y+8}" width="1000" height="10" rx="5" fill="#1E293B"/>'
            f'<rect x="40" y="{y+8}" width="{bar_w}" height="10" rx="5" fill="{color}"/>'
        )
        y += 36
    body = "\n  ".join(rows)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 {height}" role="img" aria-labelledby="title desc">
  <title id="title">Portfolio telemetry chart</title>
  <desc id="desc">{esc(data["disclaimer"])} Updated {esc(data["updated"])}.</desc>
  <rect width="1100" height="{height}" rx="16" fill="{COLORS["bg"]}" stroke="#1E293B"/>
  <text x="40" y="36" font-family="IBM Plex Mono,Consolas,monospace" font-size="18" font-weight="700" fill="{COLORS["white"]}">PORTFOLIO TELEMETRY</text>
  <text x="40" y="56" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="{COLORS["cyan"]}">{esc(data["disclaimer"])}</text>
  {body}
  <text x="40" y="{height - 18}" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="{COLORS["slate"]}">Last verified update: {esc(data["updated"])}</text>
</svg>
'''


def render_security_status() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 160" role="img" aria-labelledby="title desc">
  <title id="title">Security and operating status</title>
  <desc id="desc">Compact operating status: documentation validated, twin planned, certifications in progress, privacy protected.</desc>
  <rect width="1100" height="160" rx="16" fill="{COLORS["bg"]}" stroke="#1E293B"/>
  <text x="40" y="40" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="{COLORS["cyan"]}">OPERATING STATUS</text>
  <g font-family="IBM Plex Mono,Consolas,monospace" font-size="13" fill="{COLORS["light"]}">
    <rect x="40" y="60" width="240" height="70" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/>
    <text x="60" y="90" fill="{COLORS["white"]}">Docs validated</text>
    <text x="60" y="112" fill="{COLORS["cyan"]}">Profile CI green</text>
    <rect x="300" y="60" width="240" height="70" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["cyan"]}"/>
    <text x="320" y="90" fill="{COLORS["white"]}">SecureSkies twin</text>
    <text x="320" y="112" fill="{COLORS["amber"]}">Planned</text>
    <rect x="560" y="60" width="240" height="70" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["amber"]}"/>
    <text x="580" y="90" fill="{COLORS["white"]}">Security+ / PMP</text>
    <text x="580" y="112" fill="{COLORS["amber"]}">In Progress</text>
    <rect x="820" y="60" width="240" height="70" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["slate"]}"/>
    <text x="840" y="90" fill="{COLORS["white"]}">Privacy boundary</text>
    <text x="840" y="112" fill="{COLORS["cyan"]}">Public-safe only</text>
  </g>
</svg>
'''


def render_project_navigation() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 140" role="img" aria-labelledby="title desc">
  <title id="title">Project navigation rail</title>
  <desc id="desc">Visual navigation reminder: Resume, Lab, SecureSkies, Crow Ecosystem, Tools, Contact.</desc>
  <rect width="1100" height="140" rx="16" fill="{COLORS["bg"]}" stroke="#1E293B"/>
  <text x="40" y="36" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="{COLORS["cyan"]}">PROJECT NAVIGATION</text>
  <g font-family="IBM Plex Mono,Consolas,monospace" font-size="13" fill="{COLORS["white"]}">
    <rect x="40" y="56" width="160" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/><text x="120" y="88" text-anchor="middle">Resume</text>
    <rect x="220" y="56" width="160" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/><text x="300" y="88" text-anchor="middle">Security Lab</text>
    <rect x="400" y="56" width="160" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/><text x="480" y="88" text-anchor="middle">SecureSkies</text>
    <rect x="580" y="56" width="160" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/><text x="660" y="88" text-anchor="middle">Crow Ecosystem</text>
    <rect x="760" y="56" width="160" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["blue"]}"/><text x="840" y="88" text-anchor="middle">Cyber Tools</text>
    <rect x="940" y="56" width="120" height="54" rx="10" fill="{COLORS["navy"]}" stroke="{COLORS["cyan"]}"/><text x="1000" y="88" text-anchor="middle">Contact</text>
  </g>
</svg>
'''


def render_binary_divider() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 28" role="img" aria-labelledby="title desc">
  <title id="title">Binary divider</title>
  <desc id="desc">Decorative binary stream divider for section separation.</desc>
  <rect width="1100" height="28" fill="{COLORS["bg"]}"/>
  <text x="20" y="18" font-family="IBM Plex Mono,Consolas,monospace" font-size="11" fill="{COLORS["cyan"]}" opacity="0.45">01001101 01000111 01001000 01010101 01010010 01000001 01000010 00100000 01010000 01001111 01010010 01010100 01000110 01001111 01001100 01001001 01001111</text>
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = load_tracks()
    (OUT / "portfolio-telemetry.svg").write_text(render_telemetry(data), encoding="utf-8")
    (OUT / "security-status.svg").write_text(render_security_status(), encoding="utf-8")
    (OUT / "project-navigation.svg").write_text(render_project_navigation(), encoding="utf-8")
    (OUT / "binary-divider.svg").write_text(render_binary_divider(), encoding="utf-8")
    print("rendered", OUT)


if __name__ == "__main__":
    main()
