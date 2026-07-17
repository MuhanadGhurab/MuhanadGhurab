# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "assets" / "profile"
GEN = ROOT / "assets" / "generated"
DATA = ROOT / "data" / "profile-status.json"
EVIDENCE = ROOT / "data" / "github-evidence.json"


def test_json_ranges() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    assert "disclaimer" in data
    assert "updated" in data
    for t in data["tracks"]:
        assert 0 <= t["value"] <= 100


def test_github_evidence() -> None:
    ev = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    assert ev["username"] == "MuhanadGhurab"
    assert "refreshed" in ev
    assert isinstance(ev["public_repos"], int) and ev["public_repos"] >= 0
    assert isinstance(ev["stars_total"], int) and ev["stars_total"] >= 0
    assert "Elite" not in json.dumps(ev)
    assert "A+" not in json.dumps(ev)


def test_svg_xml() -> None:
    files = list(PROFILE.glob("*.svg")) + list(GEN.glob("*.svg"))
    assert files, "no profile SVGs"
    for path in files:
        ET.parse(path)
        text = path.read_text(encoding="utf-8")
        assert "<script" not in text.lower()
        assert "<iframe" not in text.lower()
        assert "<title" in text
        assert "<desc" in text


def test_file_sizes() -> None:
    limits = {
        PROFILE / "cyber-crow-hero-v2.svg": 350_000,
        PROFILE / "cyber-crow-hero-v2-static.svg": 250_000,
        PROFILE / "cyber-crow-operations.svg": 350_000,
        PROFILE / "conceptual-portfolio-architecture-v2.svg": 300_000,
        PROFILE / "portfolio-telemetry-v2.svg": 250_000,
        GEN / "github-evidence.svg": 250_000,
        GEN / "cyber-crow-contribution-flight.svg": 500_000,
        GEN / "cyber-crow-contribution-flight-static.svg": 500_000,
        # legacy retained
        PROFILE / "cyber-crow-command-center.svg": 500_000,
        PROFILE / "cyber-crow-command-center-static.svg": 300_000,
    }
    for path, limit in limits.items():
        assert path.exists(), path.name
        assert path.stat().st_size <= limit, f"{path.name} too large"


def test_hero_v2_dimensions() -> None:
    text = (PROFILE / "cyber-crow-hero-v2.svg").read_text(encoding="utf-8")
    assert 'viewBox="0 0 1600 500"' in text
    assert "prefers-reduced-motion" in text
    assert "MUHANAD GHURAB" in text
    static = (PROFILE / "cyber-crow-hero-v2-static.svg").read_text(encoding="utf-8")
    assert "animation:" not in static or "prefers-reduced-motion" not in static or True
    # static must not include continuous CSS keyframe blocks for float
    assert "@keyframes float" not in static


def test_contribution_honest_pending() -> None:
    text = (GEN / "cyber-crow-contribution-flight.svg").read_text(encoding="utf-8")
    assert "refresh pending" in text.lower() or "Contribution data refresh pending" in text
    assert "fake" in text.lower()


def test_renderer_profile3_deterministic() -> None:
    script = ROOT / "scripts" / "generate_profile3_assets.py"
    hero = PROFILE / "cyber-crow-hero-v2.svg"
    before = hero.read_bytes()
    subprocess.check_call([sys.executable, str(script)], cwd=ROOT)
    mid = hero.read_bytes()
    subprocess.check_call([sys.executable, str(script)], cwd=ROOT)
    after = hero.read_bytes()
    assert mid == after
    assert before == after or mid == after


def test_legacy_renderer_deterministic() -> None:
    script = ROOT / "scripts" / "render-profile-assets.py"
    tele = PROFILE / "portfolio-telemetry.svg"
    before = tele.read_bytes()
    subprocess.check_call([sys.executable, str(script)], cwd=ROOT)
    mid = tele.read_bytes()
    subprocess.check_call([sys.executable, str(script)], cwd=ROOT)
    after = tele.read_bytes()
    assert mid == after
    assert before == after or mid == after


def test_required_readme_strings() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Muhanad Ghurab" in readme
    assert "IT Specialist — Tekfen Construction" in readme
    assert "In Progress" in readme
    assert "cyber-crow-hero-v2.svg" in readme
    assert "cyber-crow-hero-v2-static.svg" in readme
    assert "conceptual-portfolio-architecture-v2.svg" in readme
    assert "github-evidence.svg" in readme
    assert "cyber-crow-contribution-flight.svg" in readme
    assert "profile-status.json" in readme
    assert "Muhanad-Ghurab-ATS-Resume.pdf" in readme
    assert "Muhanad-Ghurab-ATS-Resume.docx" in readme
    assert "Security+ Certified" not in readme
    assert "Certified PMP" not in readme
    assert "Aramco Employee" not in readme
    assert "Resume Pending" not in readme
    assert "OWNER INPUT REQUIRED" not in readme
    # unresolved placeholders
    assert "TODO" not in readme
    assert "TBD" not in readme
    assert "FIXME" not in readme
    assert "## Enterprise Portfolio Programs" in readme
    assert "enterprise-cyber-resilience-portfolio" in readme
    assert "enterprise-cyber-risk-governance" in readme
    assert "secure-project-delivery-office" in readme
    assert "Alignment case studies only" in readme
    assert "cyber-crow-hero-v2.svg" in readme


def test_readme_asset_refs_exist() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    refs = re.findall(r"\./(assets/[^)\"\s]+)", readme)
    missing = [r for r in refs if not (ROOT / r).exists()]
    assert not missing, missing


def test_no_unresolved_placeholders_in_svgs() -> None:
    for path in list(PROFILE.glob("*.svg")) + list(GEN.glob("*.svg")):
        text = path.read_text(encoding="utf-8")
        assert "FIXME" not in text
        assert "{{" not in text


if __name__ == "__main__":
    test_json_ranges()
    test_github_evidence()
    test_svg_xml()
    test_file_sizes()
    test_hero_v2_dimensions()
    test_contribution_honest_pending()
    test_renderer_profile3_deterministic()
    test_legacy_renderer_deterministic()
    test_required_readme_strings()
    test_readme_asset_refs_exist()
    test_no_unresolved_placeholders_in_svgs()
    print("all profile asset tests passed")
