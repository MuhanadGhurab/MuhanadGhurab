#!/usr/bin/env python3
"""Generate cyber-crow command center hero and companion marks (deterministic)."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "profile"


def command_center(animated: bool) -> str:
    anim_css = ""
    if animated:
        anim_css = """
      @media (prefers-reduced-motion: no-preference) {
        .scan { animation: scan 9s linear infinite; }
        .float { animation: float 6s ease-in-out infinite; }
        .pulse { animation: pulse 3.5s ease-in-out infinite; }
        .stream { animation: stream 12s linear infinite; }
        .orbit { animation: orbit 18s linear infinite; transform-origin: 1480px 290px; }
        .blink { animation: blink 1.4s steps(1) infinite; }
        .node { animation: node 4s ease-in-out infinite; }
        .trace { stroke-dasharray: 220; stroke-dashoffset: 220; animation: draw 8s ease-in-out infinite; }
      }
      @keyframes scan { 0% { transform: translateY(-30px);} 100% { transform: translateY(520px);} }
      @keyframes float { 0%,100% { transform: translateY(0);} 50% { transform: translateY(-8px);} }
      @keyframes pulse { 0%,100% { opacity: .55;} 50% { opacity: 1;} }
      @keyframes stream { 0% { transform: translateX(0);} 100% { transform: translateX(-90px);} }
      @keyframes orbit { from { transform: rotate(0deg);} to { transform: rotate(360deg);} }
      @keyframes blink { 0%,49% { opacity: 1;} 50%,100% { opacity: 0;} }
      @keyframes node { 0%,100% { opacity: .35;} 50% { opacity: 1;} }
      @keyframes draw { 0%,100% { stroke-dashoffset: 220;} 50% { stroke-dashoffset: 0;} }
"""
    title = "Muhanad Ghurab cyber portfolio command center"
    desc = (
        "Wide command-center canvas with geometric binary crow, professional identity, "
        "conceptual portfolio architecture, telemetry reminders, and navigation rail. "
        "Conceptual Portfolio Architecture only — not an employer network."
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1800 640" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="45%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0.55"/>
    </linearGradient>
    <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </radialGradient>
    <style><![CDATA[
      .name {{ font-family: IBM Plex Mono, JetBrains Mono, Consolas, ui-monospace, monospace; font-size: 46px; font-weight: 700; fill: #FFFFFF; letter-spacing: .08em; }}
      .sub {{ font-family: IBM Plex Mono, Consolas, monospace; font-size: 16px; fill: #22D3EE; letter-spacing: .12em; }}
      .tag {{ font-family: IBM Plex Mono, Consolas, monospace; font-size: 14px; fill: #CBD5E1; }}
      .mini {{ font-family: IBM Plex Mono, Consolas, monospace; font-size: 12px; fill: #94A3B8; }}
      .bin {{ font-family: IBM Plex Mono, Consolas, monospace; font-size: 11px; fill: #22D3EE; opacity: .2; }}
      .outline {{ fill: none; stroke: url(#glow); stroke-width: 2.6; stroke-linejoin: round; stroke-linecap: round; }}
      .wing {{ fill: none; stroke: #2563EB; stroke-width: 1.5; opacity: .85; }}
      .wire {{ stroke: #475569; stroke-width: 1.2; fill: none; opacity: .65; }}
      .panel {{ fill: #0B1224; stroke: #1E293B; stroke-width: 1.5; }}
      .scan {{ fill: #22D3EE; opacity: .08; }}
      {anim_css}
    ]]></style>
  </defs>
  <rect width="1800" height="640" fill="url(#bg)"/>
  <g class="stream">
    <text class="bin" x="30" y="40">01001101 01010101 01001000 01000001 01001110 01000001 01000100 00100000 01000111 01001000 01010101 01010010 01000001 01000010</text>
    <text class="bin" x="120" y="62">11001010 00101101 10010110 01011100 10100101 01101100 01010011 01000101 01000011 01001111 01010000 01010011</text>
    <text class="bin" x="60" y="612">IDENTITY | INFRASTRUCTURE | DETECTION | AUTOMATION | GOVERNANCE | PROJECTS</text>
  </g>
  <rect class="scan" x="0" y="0" width="1800" height="24"/>

  <!-- LEFT: crow -->
  <g transform="translate(280,310)">
    <ellipse class="pulse" cx="10" cy="-40" rx="56" ry="34" fill="url(#eyeGlow)" opacity="0.28"/>
    <path class="outline" d="M-160,70 C-120,10 -60,-90 40,-120 C90,-135 145,-105 170,-50 C185,-10 160,50 110,80 C50,115 -70,125 -160,70 Z"/>
    <path class="wing trace" d="M-110,0 C-40,-55 50,-50 120,5"/>
    <path class="wing" d="M-95,28 C-20,-10 55,0 125,40"/>
    <path class="wing" d="M-85,52 C-15,25 45,35 110,70"/>
    <path class="outline" d="M170,-50 L235,-28 L175,-5 Z"/>
    <circle class="pulse" cx="45" cy="-65" r="7" fill="#22D3EE"/>
    <text class="bin" x="-70" y="-10" opacity="0.55">01</text>
    <text class="bin" x="-40" y="20" opacity="0.55">10</text>
    <text class="bin" x="0" y="45" opacity="0.55">01</text>
    <text class="bin" x="40" y="15" opacity="0.55">11</text>
    <path class="wing" d="M-140,85 L-175,135 M-110,95 L-130,145 M-80,100 L-90,150"/>
    <!-- compact mark badge -->
    <g transform="translate(-200,-170)">
      <circle cx="0" cy="0" r="34" fill="#0B1224" stroke="#22D3EE" stroke-width="2"/>
      <path d="M-14,8 C-6,-10 8,-14 16,-2 C10,10 -4,16 -14,8 Z" fill="none" stroke="#2563EB" stroke-width="2"/>
      <circle cx="8" cy="-6" r="2.5" fill="#22D3EE"/>
    </g>
  </g>

  <!-- CENTER: identity -->
  <text class="name" x="560" y="170">MUHANAD GHURAB</text>
  <text class="sub" x="560" y="210">CYBERSECURITY  |  INFRASTRUCTURE  |  ENTERPRISE TECHNOLOGY</text>
  <text class="tag" x="560" y="250">Securing Enterprise Systems.</text>
  <text class="tag" x="560" y="276">Building Resilient Infrastructure.</text>
  <text class="tag" x="560" y="302">Engineering Trusted Digital Operations.</text>
  <rect class="panel" x="560" y="330" width="420" height="120" rx="12"/>
  <text class="mini" x="580" y="360">$ role</text>
  <text class="tag" x="580" y="384">IT Specialist - Tekfen Construction</text>
  <text class="mini" x="580" y="414">$ location</text>
  <text class="tag" x="580" y="438">Jeddah, Saudi Arabia</text>
  <rect x="580" y="455" width="8" height="12" fill="#22D3EE" class="blink"/>

  <!-- RIGHT: conceptual architecture -->
  <g class="float" transform="translate(0,0)">
    <text class="mini" x="1120" y="120">CONCEPTUAL PORTFOLIO ARCHITECTURE</text>
    <g transform="translate(1480,290)">
      <polygon points="0,-70 64,-35 64,35 0,70 -64,35 -64,-35" fill="#0B1224" stroke="#22D3EE" stroke-width="2.5"/>
      <polygon points="0,-40 34,-20 34,20 0,40 -34,20 -34,-20" fill="none" stroke="#2563EB" stroke-width="1.5"/>
      <text x="0" y="6" text-anchor="middle" font-family="IBM Plex Mono,Consolas,monospace" font-size="11" fill="#FFFFFF">CORE</text>
      <g class="orbit">
        <circle cx="0" cy="-130" r="4" fill="#22D3EE" class="node"/>
        <circle cx="112" cy="-65" r="4" fill="#22D3EE" class="node"/>
        <circle cx="112" cy="65" r="4" fill="#22D3EE" class="node"/>
        <circle cx="0" cy="130" r="4" fill="#22D3EE" class="node"/>
        <circle cx="-112" cy="65" r="4" fill="#22D3EE" class="node"/>
        <circle cx="-112" cy="-65" r="4" fill="#22D3EE" class="node"/>
        <path class="wire" d="M0,-70 L0,-126 M55,-30 L108,-62 M55,30 L108,62 M0,70 L0,126 M-55,30 L-108,62 M-55,-30 L-108,-62"/>
      </g>
      <text class="mini" x="0" y="-150" text-anchor="middle" fill="#CBD5E1">Identity</text>
      <text class="mini" x="145" y="-65" fill="#CBD5E1">Infrastructure</text>
      <text class="mini" x="145" y="70" fill="#CBD5E1">Detection</text>
      <text class="mini" x="0" y="155" text-anchor="middle" fill="#CBD5E1">Automation</text>
      <text class="mini" x="-145" y="70" text-anchor="end" fill="#CBD5E1">Governance</text>
      <text class="mini" x="-145" y="-65" text-anchor="end" fill="#CBD5E1">Projects</text>
    </g>
    <!-- mini telemetry -->
    <rect class="panel" x="1120" y="430" width="520" height="90" rx="12"/>
    <text class="mini" x="1140" y="458">PORTFOLIO PROGRESS (project/learning only)</text>
    <rect x="1140" y="472" width="280" height="8" rx="4" fill="#1E293B"/><rect x="1140" y="472" width="210" height="8" rx="4" fill="#2563EB"/>
    <text class="mini" x="1430" y="480" fill="#22D3EE">Foundation 75%</text>
    <rect x="1140" y="496" width="280" height="8" rx="4" fill="#1E293B"/><rect x="1140" y="496" width="224" height="8" rx="4" fill="#2563EB"/>
    <text class="mini" x="1430" y="504" fill="#22D3EE">Lab Docs 80%</text>
  </g>

  <!-- BOTTOM RAIL -->
  <g>
    <rect class="panel" x="60" y="560" width="1680" height="54" rx="12"/>
    <text class="tag" x="90" y="594">Resume</text>
    <text class="tag" x="280" y="594">Projects</text>
    <text class="tag" x="470" y="594">Lab</text>
    <text class="tag" x="620" y="594">Crow Ecosystem</text>
    <text class="tag" x="900" y="594">Contact</text>
    <text class="mini" x="1180" y="594" fill="#F59E0B">Learning: Security+ | PMP — In Progress</text>
  </g>
</svg>
'''


def crow_mark() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-labelledby="title desc">
  <title id="title">Muhanad Ghurab crow mark</title>
  <desc id="desc">Compact geometric crow head with cyan security node for brand marking.</desc>
  <rect width="128" height="128" rx="24" fill="#020617"/>
  <circle cx="64" cy="64" r="46" fill="#0F172A" stroke="#22D3EE" stroke-width="3"/>
  <path d="M34 78 C42 42 70 30 92 48 C78 74 52 86 34 78 Z" fill="none" stroke="#2563EB" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M92 48 L116 58 L94 68 Z" fill="none" stroke="#22D3EE" stroke-width="2.5"/>
  <circle cx="70" cy="48" r="5" fill="#22D3EE"/>
  <text x="64" y="108" text-anchor="middle" font-family="IBM Plex Mono,Consolas,monospace" font-size="12" fill="#CBD5E1">MG</text>
</svg>
'''


def orbit_diagram() -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" role="img" aria-labelledby="title desc">
  <title id="title">Conceptual portfolio architecture diagram</title>
  <desc id="desc">Pseudo-3D isometric enterprise core with Identity, Infrastructure, Detection, Automation, Governance, and Projects nodes. Conceptual Portfolio Architecture only.</desc>
  <defs>
    <style><![CDATA[
      .label { font-family: IBM Plex Mono, Consolas, monospace; font-size: 14px; fill: #CBD5E1; }
      .title { font-family: IBM Plex Mono, Consolas, monospace; font-size: 20px; fill: #FFFFFF; font-weight: 700; }
      .note { font-family: IBM Plex Mono, Consolas, monospace; font-size: 12px; fill: #94A3B8; }
      @media (prefers-reduced-motion: no-preference) {
        .float { animation: float 7s ease-in-out infinite; }
        .pulse { animation: pulse 3.2s ease-in-out infinite; }
      }
      @keyframes float { 0%,100% { transform: translateY(0);} 50% { transform: translateY(-10px);} }
      @keyframes pulse { 0%,100% { opacity: .5;} 50% { opacity: 1;} }
    ]]></style>
  </defs>
  <rect width="1200" height="560" rx="18" fill="#020617" stroke="#1E293B"/>
  <text class="title" x="40" y="48">Conceptual Portfolio Architecture</text>
  <text class="note" x="40" y="74">Portfolio map — not an employer, Tekfen, or Saudi Aramco network diagram</text>
  <g class="float" transform="translate(600,300)">
    <!-- isometric cube -->
    <polygon points="0,-90 110,-30 110,80 0,140 -110,80 -110,-30" fill="#0B1224" stroke="#22D3EE" stroke-width="3"/>
    <polygon points="0,-90 110,-30 0,20 -110,-30" fill="#132033" stroke="#2563EB" stroke-width="2"/>
    <polygon points="0,20 110,-30 110,80 0,140" fill="#0C1528" stroke="#2563EB" stroke-width="2"/>
    <text x="0" y="20" text-anchor="middle" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="#FFFFFF">SECURE</text>
    <text x="0" y="42" text-anchor="middle" font-family="IBM Plex Mono,Consolas,monospace" font-size="16" fill="#22D3EE">CORE</text>
    <!-- nodes -->
    <g stroke="#475569" stroke-width="1.5" fill="none">
      <path d="M0,-90 L0,-170"/><path d="M110,-30 L190,-70"/><path d="M110,80 L190,130"/><path d="M0,140 L0,210"/><path d="M-110,80 L-190,130"/><path d="M-110,-30 L-190,-70"/>
    </g>
    <circle class="pulse" cx="0" cy="-180" r="8" fill="#22D3EE"/><text class="label" x="0" y="-198" text-anchor="middle">Identity</text>
    <circle class="pulse" cx="200" cy="-78" r="8" fill="#22D3EE"/><text class="label" x="220" y="-74">Infrastructure</text>
    <circle class="pulse" cx="200" cy="138" r="8" fill="#22D3EE"/><text class="label" x="220" y="142">Detection</text>
    <circle class="pulse" cx="0" cy="220" r="8" fill="#22D3EE"/><text class="label" x="0" y="244" text-anchor="middle">Automation</text>
    <circle class="pulse" cx="-200" cy="138" r="8" fill="#22D3EE"/><text class="label" x="-220" y="142" text-anchor="end">Governance</text>
    <circle class="pulse" cx="-200" cy="-78" r="8" fill="#22D3EE"/><text class="label" x="-220" y="-74" text-anchor="end">Projects</text>
  </g>
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cyber-crow-command-center.svg").write_text(command_center(True), encoding="utf-8")
    (OUT / "cyber-crow-command-center-static.svg").write_text(command_center(False), encoding="utf-8")
    (OUT / "crow-mark.svg").write_text(crow_mark(), encoding="utf-8")
    (OUT / "crow-mark-dark.svg").write_text(crow_mark(), encoding="utf-8")
    # light mark: invert surface slightly
    light = crow_mark().replace("#020617", "#F8FAFC").replace("#0F172A", "#E2E8F0").replace("#CBD5E1", "#0F172A")
    (OUT / "crow-mark-light.svg").write_text(light, encoding="utf-8")
    (OUT / "enterprise-orbit-diagram.svg").write_text(orbit_diagram(), encoding="utf-8")
    print("heroes written")


if __name__ == "__main__":
    main()
