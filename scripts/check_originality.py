#!/usr/bin/env python3
"""Check repository-owned behavior prompts for internal reuse risks."""

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "tests" / "cases"
MODULE_DIR = ROOT / "references" / "tasks"
WINDOW = 8


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def main() -> int:
    requests: dict[str, str] = {}
    spans: dict[tuple[str, ...], set[str]] = defaultdict(set)
    cases = 0

    for path in sorted(CASE_DIR.glob("*.json")):
        if path.name == "core.json":
            continue
        for case in json.loads(path.read_text(encoding="utf-8")):
            cases += 1
            request = case["request"].strip()
            if request in requests:
                raise SystemExit(
                    f"Duplicate request in {requests[request]} and {path.name}: {request}"
                )
            requests[request] = path.name
            tokens = words(request)
            for index in range(len(tokens) - WINDOW + 1):
                spans[tuple(tokens[index : index + WINDOW])].add(case["id"])

    overlaps = {span: ids for span, ids in spans.items() if len(ids) > 1}
    if overlaps:
        sample, ids = next(iter(overlaps.items()))
        raise SystemExit(
            f"Repeated {WINDOW}-word span in {sorted(ids)}: {' '.join(sample)}"
        )

    modules = list(MODULE_DIR.glob("*.md"))
    contract = re.compile(
        r"(?:do not copy or closely paraphrase ETS|avoid copying or closely paraphrasing ETS)",
        re.IGNORECASE,
    )
    missing = [path.name for path in modules if not contract.search(path.read_text(encoding="utf-8"))]
    if missing:
        raise SystemExit(f"Missing ETS originality contract: {', '.join(sorted(missing))}")

    print(
        f"Originality check passed: {cases} task-specific cases, "
        f"{len(modules)} modules, no duplicate requests or repeated {WINDOW}-word spans."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
