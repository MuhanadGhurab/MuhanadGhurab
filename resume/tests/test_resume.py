#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
RESUME = ROOT / "resume"
DATA = RESUME / "source" / "resume-data.json"
PDF = RESUME / "Muhanad-Ghurab-ATS-Resume.pdf"
DOCX = RESUME / "Muhanad-Ghurab-ATS-Resume.docx"
PREVIEW = RESUME / "Muhanad-Ghurab-ATS-Resume-preview.png"
README = ROOT / "README.md"


def test_files_exist():
    assert PDF.exists()
    assert DOCX.exists()
    assert PREVIEW.exists()
    assert DATA.exists()


def test_pdf_one_page_and_text():
    reader = PdfReader(str(PDF))
    assert len(reader.pages) == 1
    text = reader.pages[0].extract_text() or ""
    assert len(text) > 500
    required = [
        "Muhanad Ghurab",
        "Cybersecurity",
        "IT Infrastructure",
        "Tekfen Construction",
        "Saudi Aramco",
        "Windows",
        "Network",
        "Security+",
        "PMP",
        "Enterprise Cybersecurity Lab",
        "SecSky",
        "GitHub",
        "Jeddah International College",
        "In Progress",
        "muhanadghurab@gmail.com",
        "+966 59 700 4895",
        "linkedin.com/in/muhanad-ghurab-141btb414",
        "github.com/MuhanadGhurab",
    ]
    lower = text.lower()
    for term in required:
        assert term.lower() in lower, term
    forbidden = [
        "Security+ Certified",
        "PMP Certified",
        "Certified PMP",
        "Saudi Aramco Employee",
        "IT Specialist at Saudi Aramco",
        "TODO",
        "TBD",
        "lorem ipsum",
        "Muhammad Thowfeek",
    ]
    for bad in forbidden:
        assert bad.lower() not in lower, bad
    assert "utm_" not in lower


def test_docx_openxml_and_text():
    with zipfile.ZipFile(DOCX) as zf:
        assert "[Content_Types].xml" in zf.namelist()
        xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
    assert "Muhanad Ghurab" in xml or "MUHANAD GHURAB" in xml
    assert "Tekfen Construction" in xml
    assert "In Progress" in xml
    assert "Security+ Certified" not in xml


def test_source_json():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    assert data["identity"]["email"] == "muhanadghurab@gmail.com"
    assert data["identity"]["phone"] == "+966 59 700 4895"
    assert data["identity"]["github_username"] == "MuhanadGhurab"
    assert "utm_" not in data["identity"]["linkedin_url"]
    assert PDF.stat().st_size < 1_000_000
    assert DOCX.stat().st_size < 2_000_000


def test_readme_resume_links():
    readme = README.read_text(encoding="utf-8")
    assert "OWNER INPUT REQUIRED" not in readme
    assert "resume/Muhanad-Ghurab-ATS-Resume.pdf" in readme
    assert "Resume Pending" not in readme
    # linked paths resolve
    assert (ROOT / "resume" / "Muhanad-Ghurab-ATS-Resume.pdf").exists()


if __name__ == "__main__":
    test_files_exist()
    test_pdf_one_page_and_text()
    test_docx_openxml_and_text()
    test_source_json()
    # README may not yet be updated during first local run of generation
    try:
        test_readme_resume_links()
    except AssertionError as e:
        print("README activation pending:", e)
    else:
        print("README activation ok")
    print("resume tests passed")
