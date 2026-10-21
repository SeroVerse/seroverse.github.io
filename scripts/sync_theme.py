#!/usr/bin/env python3
"""Synchronize canonical SeroVerse Zensical theme components to sibling repositories.

Copies `docs/stylesheets/extra.css` and `docs/overrides/main.html` from
`seroverse.github.io` into `../SeroGen`, `../KBank`, and `../SeroEpi`.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_FILES = (
    Path("docs/stylesheets/extra.css"),
    Path("docs/overrides/main.html"),
)
DEFAULT_TARGETS = (
    ROOT.parent / "SeroGen",
    ROOT.parent / "KBank",
    ROOT.parent / "SeroEpi",
)


def sync_target(target_repo: Path, *, check_only: bool = False) -> list[str]:
    """Sync canonical theme files into a target repository."""
    messages: list[str] = []
    if not target_repo.is_dir():
        messages.append(f"[SKIP] {target_repo} does not exist")
        return messages

    for rel_path in CANONICAL_FILES:
        src = ROOT / rel_path
        dst = target_repo / rel_path
        src_bytes = src.read_bytes()
        dst_bytes = dst.read_bytes() if dst.exists() else None

        if dst_bytes == src_bytes:
            messages.append(f"[OK]   {target_repo.name}/{rel_path} is up to date")
            continue

        if check_only:
            messages.append(f"[DIFF] {target_repo.name}/{rel_path} differs from canonical")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            messages.append(f"[SYNC] {target_repo.name}/{rel_path} updated")

    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify that sibling repositories match canonical theme files without modifying them.",
    )
    parser.add_argument(
        "targets",
        nargs="*",
        type=Path,
        default=list(DEFAULT_TARGETS),
        help="Target repository paths (defaults to ../SeroGen, ../KBank, ../SeroEpi).",
    )
    args = parser.parse_args()

    has_diff = False
    for target in args.targets:
        for line in sync_target(target.resolve(), check_only=args.check):
            print(line)
            if line.startswith("[DIFF]"):
                has_diff = True

    return 1 if (args.check and has_diff) else 0


if __name__ == "__main__":
    raise SystemExit(main())
