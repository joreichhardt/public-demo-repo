#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "LICENSE.text",
    ROOT / "LICENSE.code",
    ROOT / "planung" / "expose.md",
    ROOT / "planung" / "kapitelplan.md",
    ROOT / "planung" / "offene-fragen.md",
    ROOT / "manuskript" / "geschichte.md",
    ROOT / "manuskript" / "kapitel-01.md",
    ROOT / "manuskript" / "kapitel-02.md",
    ROOT / "scripts" / "build.sh",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        for path in missing:
            print(f"missing: {path}", file=sys.stderr)
        return 1

    story = (ROOT / "manuskript" / "geschichte.md").read_text(encoding="utf-8")
    if "Der Ordner war schon offen." not in story:
        print("story smoke test failed: missing key sentence", file=sys.stderr)
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "CC BY-SA 4.0" not in readme or "MIT" not in readme:
        print("readme smoke test failed: licenses not documented", file=sys.stderr)
        return 1

    print("demo repo smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
