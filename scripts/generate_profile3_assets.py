#!/usr/bin/env python3
"""Generate PROFILE.3 modular SVG assets (deterministic, original crow)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "assets" / "profile"
GEN = ROOT / "assets" / "generated"


def hero(animated: bool) -> str:
    css = ""
    if animated:
        css = """
      @media (prefers-reduced-motion: no-preference) {
        .float { animation: float 7.5s ease-in-out infinite; }
        .pulse { animation: pulse 4s ease-in-out infinite; }
        .scan { animation: scan 13s linear infinite; }
        .stream { animation: stream 10s linear infinite; }
        .node { animation: node 4.5s ease-in-out infinite; }
        .trace { stroke-dasharray: 320; animation: draw 11s ease-in-out infinite; }
        .particle { animation: drift 8s ease-out infinite; }
      }
      @media (prefers-reduced-motion: reduce) {
        .float,.pulse,.scan,.stream,.node,.trace,.particle { animation: none !important; }
      }
      @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
      @keyframes pulse { 0%,100%{opacity:.7} 50%{opacity:1} }
      @keyframes scan { 0%{transform:translateY(-30px)} 100%{transform:translateY(480px)} }
      @keyframes stream { 0%{transform:translateX(0)} 100%{transform:translateX(-80px)} }
      @keyframes node { 0%,100%{opacity:.35} 50%{opacity:1} }
      @keyframes draw { 0%,100%{stroke-dashoffset:320} 50%{stroke-dashoffset:0} }
      @keyframes drift { 0%{opacity:.55;transform:translate(0,0)} 100%{opacity:0;transform:translate(55px,-40px)} }
"""
    smil_float = (
        '<animateTransform attributeName="transform" type="translate" values="0 0; 0 -12; 0 0" '
        'dur="7.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1; 0.45 0 0.55 1"/>'
        if animated
        else ""
    )
    smil_eye = (
        '<animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>'
        if animated
        else ""
    )
    smil_scan = (
        '<animateTransform attributeName="transform" type="translate" values="0 -30; 0 480" '
        'dur="13s" repeatCount="indefinite"/>'
        if animated
        else ""
    )
    smil_bin = (
        '<animateTransform attributeName="transform" type="translate" values="0 0; -80 0" '
        'dur="10s" repeatCount="indefinite"/>'
        if animated
        else ""
    )
    particles = ""
    if animated:
        for i, (x, y, d) in enumerate(
            [(180, -20, "0s"), (200, 10, "1.2s"), (160, 40, "2.4s"), (220, -5, "3.1s"), (150, 70, "4s")]
        ):
            particles += (
                f'<circle class="particle" cx="{x}" cy="{y}" r="3.2" fill="#22D3EE" opacity="0.45">'
                f'<animate attributeName="opacity" values="0.55;0;0.55" dur="8s" begin="{d}" '
                f'repeatCount="indefinite"/>'
                f"</circle>"
            )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" role="img" aria-labelledby="title desc">
  <title id="title">Muhanad Ghurab animated cyber-crow hero</title>
  <desc id="desc">Sentinel composition: large geometric binary cyber crow on the left with identity text on the right. Controlled float, binary streams, eye pulse, circuit trace, and scan line. Original cyber-crow brand art.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#020617"/><stop offset="45%" stop-color="#0B1630"/><stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#2563EB"/><stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
    <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#13233F"/><stop offset="100%" stop-color="#07101F"/>
    </linearGradient>
    <style><![CDATA[
      .name{{font-family:IBM Plex Mono,Consolas,monospace;font-size:52px;font-weight:700;fill:#FFFFFF;letter-spacing:.08em}}
      .sub{{font-family:IBM Plex Mono,Consolas,monospace;font-size:17px;fill:#22D3EE;letter-spacing:.1em}}
      .tag{{font-family:IBM Plex Mono,Consolas,monospace;font-size:16px;fill:#CBD5E1}}
      .mini{{font-family:IBM Plex Mono,Consolas,monospace;font-size:13px;fill:#94A3B8}}
      .bin{{font-family:IBM Plex Mono,Consolas,monospace;font-size:15px;fill:#22D3EE;opacity:.4}}
      .grid{{stroke:#1E293B;stroke-width:1;opacity:.45}}
      .outline{{fill:url(#fill);stroke:url(#glow);stroke-width:3.4;stroke-linejoin:round}}
      .wing{{fill:none;stroke:#38BDF8;stroke-width:2.2;opacity:.95}}
      .plate{{fill:#0B1224;stroke:#2563EB;stroke-width:1.6}}
      .scan{{fill:#22D3EE;opacity:.08}}
      {css}
    ]]></style>
  </defs>
  <rect width="1600" height="500" fill="url(#bg)"/>
  <g class="grid">
    <path d="M40 80 H700 M40 140 H680 M40 200 H660 M40 260 H640 M40 320 H620 M40 380 H600"/>
    <path d="M120 40 V460 M200 40 V460 M280 40 V460 M360 40 V460 M440 40 V460"/>
  </g>
  <g class="stream">{smil_bin}
    <text class="bin" x="36" y="36">01001101 01010101 01001000 01000001 01001110 01000001 01000100</text>
    <text class="bin" x="60" y="58">11001001 10100101 01101100 01010011 01000101 01000011</text>
  </g>
  <rect class="scan" x="0" y="0" width="1600" height="26">{smil_scan}</rect>
  <!-- crow ~40% width; nested g keeps base translate while SMIL floats -->
  <g transform="translate(330,275)">
    <g class="float">{smil_float}
      <ellipse class="pulse" cx="30" cy="-55" rx="78" ry="48" fill="#22D3EE" opacity="0.18">{smil_eye}</ellipse>
      <path class="outline" d="M-230,95 C-175,15 -85,-125 55,-165 C140,-182 225,-130 255,-48 C278,12 240,85 160,122 C70,168 -105,175 -230,95 Z"/>
      <path class="plate" d="M-150,5 L-60,-55 L10,-35 L-40,45 Z"/>
      <path class="plate" d="M-90,45 L0,-5 L70,25 L-10,85 Z"/>
      <path class="plate" d="M-40,85 L50,40 L110,75 L20,120 Z"/>
      <path class="wing trace" d="M-160,5 C-40,-85 100,-75 205,20"/>
      <path class="wing" d="M-135,40 C-20,-15 105,5 210,65"/>
      <path class="wing" d="M-115,78 C-15,35 95,55 195,110"/>
      <path class="outline" d="M255,-48 L345,-12 L260,22 Z" fill="#0B1224"/>
      <circle class="pulse" cx="62" cy="-92" r="11" fill="#22D3EE">{smil_eye}</circle>
      <text class="bin" x="-120" y="-15">01</text>
      <text class="bin" x="-55" y="30">10</text>
      <text class="bin" x="15" y="62">01</text>
      <text class="bin" x="85" y="22">11</text>
      <text class="bin" x="40" y="95">00</text>
      <circle class="node" cx="-185" cy="45" r="7" fill="#22D3EE"/>
      <circle class="node" cx="-105" cy="-45" r="7" fill="#22D3EE"/>
      <circle class="node" cx="-10" cy="-100" r="7" fill="#22D3EE"/>
      <circle class="node" cx="130" cy="-35" r="7" fill="#22D3EE"/>
      <circle class="node" cx="185" cy="55" r="7" fill="#22D3EE"/>
      <circle class="node" cx="90" cy="95" r="6" fill="#38BDF8"/>
      {particles}
    </g>
  </g>
  <text class="name" x="720" y="165">MUHANAD GHURAB</text>
  <text class="sub" x="720" y="205">CYBERSECURITY  ·  INFRASTRUCTURE  ·  ENTERPRISE TECHNOLOGY</text>
  <text class="tag" x="720" y="255">Securing Enterprise Systems.</text>
  <text class="tag" x="720" y="285">Building Resilient Infrastructure.</text>
  <text class="tag" x="720" y="315">Engineering Trusted Digital Operations.</text>
  <rect x="720" y="345" width="220" height="28" rx="6" fill="#0F172A" stroke="#22D3EE" stroke-width="1.5"/>
  <text class="mini" x="734" y="364" fill="#22D3EE">CROW NODE // ONLINE</text>
  <text class="mini" x="720" y="405">JEDDAH, SAUDI ARABIA</text>
  <text class="mini" x="720" y="430">IT SPECIALIST // TEKFEN CONSTRUCTION</text>
</svg>
'''


def operations(animated: bool) -> str:
    anim = ""
    if animated:
        anim = """
      @media (prefers-reduced-motion: no-preference) {
        .packet { animation: move 9s ease-in-out infinite; }
        .beacon { animation: pulse 3.2s ease-in-out infinite; }
        .float { animation: float 7s ease-in-out infinite; }
      }
      @media (prefers-reduced-motion: reduce) {
        .packet,.beacon,.float { animation: none !important; }
      }
      @keyframes move {
        0%{transform:translate(0,0)}
        40%{transform:translate(240px,-18px)}
        65%{transform:translate(400px,70px)}
        100%{transform:translate(400px,70px)}
      }
      @keyframes pulse { 0%,100%{opacity:.5} 50%{opacity:1} }
      @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
"""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 420" role="img" aria-labelledby="title desc">
  <title id="title">Cyber-crow defensive operations illustration</title>
  <desc id="desc">Conceptual defensive story: suspicious packet approaches enterprise core, crow scans, detection activates, packet redirected to quarantine. Not a live SOC or employer network.</desc>
  <defs><style><![CDATA[
    .t{{font-family:IBM Plex Mono,Consolas,monospace;font-size:18px;fill:#FFFFFF;font-weight:700}}
    .n{{font-family:IBM Plex Mono,Consolas,monospace;font-size:12px;fill:#94A3B8}}
    .l{{font-family:IBM Plex Mono,Consolas,monospace;font-size:13px;fill:#CBD5E1}}
    {anim}
  ]]></style></defs>
  <rect width="1500" height="420" rx="18" fill="#020617" stroke="#1E293B"/>
  <text class="t" x="40" y="42">Conceptual Defensive Operations — Portfolio Illustration</text>
  <text class="n" x="40" y="66">Not a live SOC, Tekfen, or Saudi Aramco network diagram</text>
  <g stroke="#1E293B" stroke-width="1" opacity="0.6">
    <path d="M80 120 H560 M80 180 H540 M80 240 H520"/>
  </g>
  <g transform="translate(980,230)">
    <polygon points="0,-75 85,-38 85,48 0,85 -85,48 -85,-38" fill="#0B1224" stroke="#22D3EE" stroke-width="3"/>
    <text class="l" x="0" y="10" text-anchor="middle" fill="#FFFFFF" font-size="14">SECURE CORE</text>
  </g>
  <rect x="1180" y="285" width="190" height="72" rx="10" fill="#0B1224" stroke="#F59E0B" stroke-width="2"/>
  <text class="l" x="1275" y="327" text-anchor="middle" fill="#F59E0B">QUARANTINE</text>
  <g class="float" transform="translate(420,175)">
    <path d="M-80,35 C-45,-25 25,-48 80,-8 C92,28 45,58 -15,62 C-45,62 -80,45 -80,35 Z" fill="#0B1224" stroke="#2563EB" stroke-width="3"/>
    <circle cx="30" cy="-18" r="6" fill="#22D3EE" class="beacon"/>
    <path d="M80,-8 L120,2 L82,14" fill="none" stroke="#22D3EE" stroke-width="2.4"/>
  </g>
  <path d="M120 245 C280 205, 520 200, 780 235" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="7 7"/>
  <path d="M900 255 C1030 275, 1110 305, 1185 318" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="5 5"/>
  <g class="packet">
    <rect x="110" y="230" width="30" height="20" rx="3" fill="#F87171"/>
    <text x="125" y="244" text-anchor="middle" font-size="10" fill="#020617" font-family="Consolas,monospace">?</text>
  </g>
  <circle class="beacon" cx="640" cy="168" r="9" fill="#22D3EE"/>
  <text class="l" x="660" y="173">DETECTION</text>
  <text class="n" x="120" y="392">Suspicious packet scanned by crow node and redirected away from the protected core.</text>
</svg>
'''


def architecture() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" role="img" aria-labelledby="title desc">
  <title id="title">Conceptual portfolio architecture</title>
  <desc id="desc">Large isometric portfolio map: secure core with Identity, Infrastructure, Detection, Automation, Governance, Projects. Conceptual only — not an employer network.</desc>
  <defs>
    <style><![CDATA[
      .t{font-family:IBM Plex Mono,Consolas,monospace;font-size:22px;fill:#FFFFFF;font-weight:700}
      .n{font-family:IBM Plex Mono,Consolas,monospace;font-size:13px;fill:#94A3B8}
      .l{font-family:IBM Plex Mono,Consolas,monospace;font-size:15px;fill:#CBD5E1}
      @media (prefers-reduced-motion:no-preference){.float{animation:float 8s ease-in-out infinite}.p{animation:pulse 3.5s ease-in-out infinite}}
      @media (prefers-reduced-motion:reduce){.float,.p{animation:none!important}}
      @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
      @keyframes pulse{0%,100%{opacity:.45}50%{opacity:1}}
    ]]></style>
  </defs>
  <rect width="1600" height="520" rx="18" fill="#020617" stroke="#1E293B"/>
  <text class="t" x="48" y="52">Conceptual Portfolio Architecture</text>
  <text class="n" x="48" y="78">Not an employer or client network diagram</text>
  <g class="float" transform="translate(800,280)">
    <polygon points="0,-100 130,-45 130,70 0,125 -130,70 -130,-45" fill="#0B1224" stroke="#22D3EE" stroke-width="3.5"/>
    <polygon points="0,-100 130,-45 0,10 -130,-45" fill="#132033" stroke="#2563EB" stroke-width="2"/>
    <text x="0" y="8" text-anchor="middle" class="l" fill="#FFFFFF" font-size="18">SECURE CORE</text>
    <g stroke="#475569" stroke-width="2" fill="none">
      <path d="M0,-100 L0,-190"/><path d="M130,-45 L230,-90"/><path d="M130,70 L230,130"/><path d="M0,125 L0,210"/><path d="M-130,70 L-230,130"/><path d="M-130,-45 L-230,-90"/>
    </g>
    <circle class="p" cx="0" cy="-200" r="10" fill="#22D3EE"/><text class="l" x="0" y="-220" text-anchor="middle">Identity</text>
    <circle class="p" cx="240" cy="-95" r="10" fill="#22D3EE"/><text class="l" x="260" y="-90">Infrastructure</text>
    <circle class="p" cx="240" cy="138" r="10" fill="#22D3EE"/><text class="l" x="260" y="143">Detection</text>
    <circle class="p" cx="0" cy="220" r="10" fill="#22D3EE"/><text class="l" x="0" y="245" text-anchor="middle">Automation</text>
    <circle class="p" cx="-240" cy="138" r="10" fill="#22D3EE"/><text class="l" x="-260" y="143" text-anchor="end">Governance</text>
    <circle class="p" cx="-240" cy="-95" r="10" fill="#22D3EE"/><text class="l" x="-260" y="-90" text-anchor="end">Projects</text>
  </g>
</svg>
'''


def telemetry(data: dict) -> str:
    want = ["github-profile", "enterprise-lab", "crow-ecosystem", "drone-security", "security-plus", "pmp"]
    by_id = {t["id"]: t for t in data["tracks"]}
    tracks = [by_id[i] for i in want if i in by_id]
    h = 90 + len(tracks) * 48
    rows = []
    y = 90
    for t in tracks:
        val = int(t["value"])
        bw = int(1100 * val / 100)
        color = "#F59E0B" if t["id"] in {"security-plus", "pmp"} else "#2563EB"
        rows.append(
            f'<text x="48" y="{y}" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="#CBD5E1">{t["label"]}</text>'
            f'<text x="1200" y="{y}" text-anchor="end" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="#22D3EE">{val}%</text>'
            f'<rect x="48" y="{y+10}" width="1152" height="14" rx="7" fill="#1E293B"/>'
            f'<rect x="48" y="{y+10}" width="{bw}" height="14" rx="7" fill="{color}"/>'
        )
        y += 48
    body = "\n  ".join(rows)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 {h}" role="img" aria-labelledby="title desc">
  <title id="title">Portfolio development telemetry</title>
  <desc id="desc">{data["disclaimer"]} Updated {data["updated"]}. Strongest six tracks shown.</desc>
  <rect width="1280" height="{h}" rx="16" fill="#020617" stroke="#1E293B"/>
  <text x="48" y="40" font-family="IBM Plex Mono,Consolas,monospace" font-size="20" fill="#FFFFFF" font-weight="700">CURRENT DEVELOPMENT</text>
  <text x="48" y="64" font-family="IBM Plex Mono,Consolas,monospace" font-size="13" fill="#22D3EE">{data["disclaimer"]}</text>
  {body}
  <text x="48" y="{h-18}" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="#64748B">Last verified: {data["updated"]}</text>
</svg>
'''


def evidence_svg(ev: dict) -> str:
    langs = ev.get("languages") or {}
    lang_bits = ", ".join(f"{k} ×{v}" for k, v in langs.items()) or "n/a"
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 280" role="img" aria-labelledby="title desc">
  <title id="title">Verified public GitHub evidence</title>
  <desc id="desc">{ev["disclaimer"]} Refreshed {ev["refreshed"]}. Public repos {ev["public_repos"]}, stars {ev["stars_total"]}.</desc>
  <rect width="1280" height="280" rx="16" fill="#020617" stroke="#1E293B"/>
  <text x="48" y="42" font-family="IBM Plex Mono,Consolas,monospace" font-size="20" fill="#FFFFFF" font-weight="700">VERIFIED PUBLIC GITHUB EVIDENCE</text>
  <text x="48" y="68" font-family="IBM Plex Mono,Consolas,monospace" font-size="13" fill="#22D3EE">Last refreshed {ev["refreshed"]} — {ev["method"]}</text>
  <rect x="48" y="100" width="360" height="100" rx="12" fill="#0F172A" stroke="#2563EB"/>
  <text x="70" y="140" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="#94A3B8">Public repositories</text>
  <text x="70" y="175" font-family="IBM Plex Mono,Consolas,monospace" font-size="36" fill="#22D3EE">{ev["public_repos"]}</text>
  <rect x="440" y="100" width="360" height="100" rx="12" fill="#0F172A" stroke="#2563EB"/>
  <text x="460" y="140" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="#94A3B8">Public stars (total)</text>
  <text x="460" y="175" font-family="IBM Plex Mono,Consolas,monospace" font-size="36" fill="#22D3EE">{ev["stars_total"]}</text>
  <rect x="832" y="100" width="400" height="100" rx="12" fill="#0F172A" stroke="#22D3EE"/>
  <text x="852" y="140" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="#94A3B8">Languages (repo primary)</text>
  <text x="852" y="175" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="#CBD5E1">{lang_bits}</text>
  <text x="48" y="250" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="#64748B">Actual public data only — not competency grades. Forks excluded from API query.</text>
</svg>
'''


def contribution_pending() -> tuple[str, str]:
    grid = "".join(
        f'<rect x="{60 + (i % 24) * 46}" y="{110 + (i // 24) * 28}" width="40" height="22" rx="4" '
        f'fill="#0F172A" stroke="#1E293B"/>'
        for i in range(48)
    )
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 220" role="img" aria-labelledby="title desc">
  <title id="title">Cyber-crow contribution flight path pending</title>
  <desc id="desc">Placeholder for contribution calendar visualization. Actual contribution cells are not fabricated. Contribution data refresh pending.</desc>
  <rect width="1280" height="220" rx="16" fill="#020617" stroke="#1E293B"/>
  <text x="48" y="50" font-family="IBM Plex Mono,Consolas,monospace" font-size="20" fill="#FFFFFF" font-weight="700">CYBER-CROW CONTRIBUTION FLIGHT PATH</text>
  <text x="48" y="85" font-family="IBM Plex Mono,Consolas,monospace" font-size="14" fill="#22D3EE">Contribution data refresh pending — no fake cells published.</text>
  <g>{grid}</g>
  <text x="48" y="200" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="#64748B">Renderer ready; load real contribution calendar via manual workflow_dispatch when approved.</text>
</svg>
'''
    return svg, svg


def main() -> None:
    PROFILE.mkdir(parents=True, exist_ok=True)
    GEN.mkdir(parents=True, exist_ok=True)
    status = json.loads((ROOT / "data" / "profile-status.json").read_text(encoding="utf-8"))
    evidence = json.loads((ROOT / "data" / "github-evidence.json").read_text(encoding="utf-8"))

    (PROFILE / "cyber-crow-hero-v2.svg").write_text(hero(True), encoding="utf-8")
    (PROFILE / "cyber-crow-hero-v2-static.svg").write_text(hero(False), encoding="utf-8")
    (PROFILE / "cyber-crow-operations.svg").write_text(operations(True), encoding="utf-8")
    (PROFILE / "conceptual-portfolio-architecture-v2.svg").write_text(architecture(), encoding="utf-8")
    (PROFILE / "portfolio-telemetry-v2.svg").write_text(telemetry(status), encoding="utf-8")
    (GEN / "github-evidence.svg").write_text(evidence_svg(evidence), encoding="utf-8")
    a, s = contribution_pending()
    (GEN / "cyber-crow-contribution-flight.svg").write_text(a, encoding="utf-8")
    (GEN / "cyber-crow-contribution-flight-static.svg").write_text(s, encoding="utf-8")
    print("PROFILE.3 assets generated")


if __name__ == "__main__":
    main()
