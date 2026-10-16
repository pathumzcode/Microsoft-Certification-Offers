#!/usr/bin/env python3
"""Validate repository structure, local Markdown links, and safe placeholders."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    ".editorconfig",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/ISSUE_TEMPLATE/documentation-correction.md",
    ".github/ISSUE_TEMPLATE/feature-request.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/markdown-validation.yml",
    "scripts/validate_docs.py",
    "docs/01-program-overview.md",
    "docs/02-eligibility-and-requirements.md",
    "docs/03-account-registration.md",
    "docs/04-finding-and-enrolling-in-courses.md",
    "docs/05-learning-modules-and-practice-assessment.md",
    "docs/06-voucher-claiming-and-delivery.md",
    "docs/07-microsoft-exam-redemption.md",
    "docs/08-faq-and-troubleshooting.md",
    "docs/09-community-checklist.md",
    "docs/10-official-resources.md",
    "docs/11-complete-course-walkthrough.md",
    "screenshots/README.md",
    "screenshots/manifest.md",
)
REQUIRED_DIRS = (".github", ".github/ISSUE_TEMPLATE", ".github/workflows", "docs", "screenshots", "scripts")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCREENSHOT_PLACEHOLDER = re.compile(r"SCREENSHOT PENDING:\s*`([^`]+)`", re.IGNORECASE)
SECRET_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(?:password|voucher\s*code|redemption\s*code)\s*[:=]\s*[A-Z0-9_-]{8,}\b"),
)


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def check_structure(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    for relative in REQUIRED_DIRS:
        if not (ROOT / relative).is_dir():
            errors.append(f"Missing required directory: {relative}")


def check_documents(files: list[Path], errors: list[str]) -> None:
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read Markdown file {path.relative_to(ROOT)}: {exc}")
            continue
        if not content.strip():
            errors.append(f"Empty Markdown file: {path.relative_to(ROOT)}")


def check_local_links(files: list[Path], errors: list[str]) -> None:
    for markdown in files:
        try:
            content = markdown.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for match in MARKDOWN_LINK.finditer(content):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//") or not parsed.path:
                continue
            decoded_path = unquote(parsed.path)
            resolved = (markdown.parent / decoded_path).resolve()
            if not resolved.exists():
                errors.append(
                    f"Broken local link in {markdown.relative_to(ROOT)}: {target}"
                )


def check_screenshot_placeholders(files: list[Path], errors: list[str]) -> None:
    manifest_path = ROOT / "screenshots" / "manifest.md"
    manifest = manifest_path.read_text(encoding="utf-8") if manifest_path.exists() else ""
    for markdown in files:
        content = markdown.read_text(encoding="utf-8")
        for match in SCREENSHOT_PLACEHOLDER.finditer(content):
            filename = match.group(1)
            if filename not in manifest:
                errors.append(
                    f"Screenshot placeholder in {markdown.relative_to(ROOT)} "
                    f"is not listed in screenshots/manifest.md: {filename}"
                )
            if not re.search(
                rf"\| `{re.escape(filename)}` \|.*\| Pending \|",
                manifest,
                re.IGNORECASE,
            ):
                errors.append(
                    f"Screenshot placeholder must have Pending status in "
                    f"screenshots/manifest.md: {filename}"
                )


def check_readme(errors: list[str]) -> None:
    readme_path = ROOT / "README.md"
    if not readme_path.is_file():
        return
    readme = readme_path.read_text(encoding="utf-8")
    required_phrases = {
        "independent-resource disclaimer": "not an official Microsoft or LevelUp publication",
        "official website": "https://skillupwithlevelup.com/",
        "official voucher terms": "https://skillupwithlevelup.com/cert-terms-and-conditions",
        "changelog link": "CHANGELOG.md",
    }
    for label, phrase in required_phrases.items():
        if phrase.casefold() not in readme.casefold():
            errors.append(f"README is missing required {label}: {phrase}")


def check_secrets(files: list[Path], errors: list[str]) -> None:
    text_suffixes = {".md", ".py", ".yml", ".yaml", ".gitignore", ".editorconfig"}
    candidates = (
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and (path.suffix.lower() in text_suffixes or path.name in text_suffixes)
    )
    for path in candidates:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(
                    f"Possible credential or voucher secret in {path.relative_to(ROOT)}"
                )
                break


def main() -> int:
    errors: list[str] = []
    check_structure(errors)
    documents = markdown_files()
    check_documents(documents, errors)
    check_local_links(documents, errors)
    check_screenshot_placeholders(documents, errors)
    check_readme(errors)
    check_secrets(documents, errors)

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Documentation validation passed: {len(REQUIRED_FILES)} required files, "
        f"{len(documents)} Markdown files, local links, screenshot placeholders, "
        "README requirements, and secret-pattern checks."
    )
    print("External links are not checked by this validator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
