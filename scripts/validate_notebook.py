"""Validate notebook structure and Python syntax without executing cells."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


def validate(path: Path) -> None:
    with path.open("r", encoding="utf-8") as stream:
        notebook = json.load(stream)

    if notebook.get("nbformat") != 4:
        raise ValueError(f"Expected nbformat 4, found {notebook.get('nbformat')!r}")

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        raise ValueError("Notebook has no cells")

    code_cells = 0
    for index, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        code_cells += 1
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        try:
            ast.parse(source, filename=f"{path}:cell-{index}")
        except SyntaxError as exc:
            raise SyntaxError(f"Invalid Python in cell {index}: {exc}") from exc

    if code_cells == 0:
        raise ValueError("Notebook has no Python code cells")

    print(f"Validated {path}: {len(cells)} cells, {code_cells} code cells")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} NOTEBOOK.ipynb", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Notebook not found: {path}", file=sys.stderr)
        return 2

    validate(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
