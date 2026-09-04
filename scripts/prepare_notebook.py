"""Create a review-friendly public notebook from the original research run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


INTRO = """# SkyDet on SkySeaLand

Reference implementation for the SkyDet development pipeline on the four-class SkySeaLand satellite dataset.

- Paper: [arXiv:2608.07382](https://arxiv.org/abs/2608.07382)
- Dataset: [Mendeley Data](https://doi.org/10.17632/d42n3cp86p.3) and [Kaggle](https://www.kaggle.com/datasets/mdzahidhasanriad/skysealand-coco)
- Classes: `airplane`, `boat`, `car`, `ship`

> **Artifact note:** this notebook preserves a 100-epoch development configuration. The manuscript reports the finalized 150-epoch reference run. See [`docs/REPRODUCIBILITY.md`](../docs/REPRODUCIBILITY.md) before comparing metrics.
"""


SECTION_MARKERS = (
    ("@dataclass\nclass CFG", "## Configuration\n\nCentral experiment, model, data, and evaluation settings."),
    ("def ensure_dir", "## Core utilities\n\nReproducibility, geometry conversion, letterboxing, and visualization helpers."),
    ("def load_coco_json", "## Dataset audit\n\nCOCO validation, distribution reports, and ground-truth overlays."),
    ("class CocoDetDataset", "## Data pipeline\n\nCOCO loading, augmentation, tensor conversion, and batching."),
    ("def sigmoid_focal_loss", "## Detection losses\n\nClass-weighted focal loss and IoU regression loss."),
    ("class ConvBNAct", "## Model building blocks\n\nConvolution, GhostConv, attention, feature fusion, backbone, and detection head."),
    ("# Section 11 Points cache", "## Target assignment\n\nMulti-level FCOS points, scale ranges, and positive-sample assignment."),
    ("# Section 12 NMS", "## Post-processing\n\nBox decoding and class-wise non-maximum suppression."),
    ("# Section 13 Training and evaluation", "## Training and evaluation\n\nOptimization, COCO export/evaluation, checkpointing, and latency measurement."),
    ("# Section 14 Inference engine", "## Inference engine\n\nSingle-image prediction with letterbox reversal and visualization."),
    ("# Section 15 Optional ONNX export", "## Optional ONNX export"),
    ("# Section 16 Main pipeline", "## End-to-end experiment\n\nAudit, train, select by validation mAP, evaluate on test, benchmark, and save artifacts."),
)


def markdown_cell(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def prepare(source_path: Path, output_path: Path) -> None:
    with source_path.open("r", encoding="utf-8") as stream:
        notebook = json.load(stream)

    public_cells = [markdown_cell(INTRO)]
    for cell in notebook.get("cells", []):
        source = cell.get("source", "")
        source_text = "".join(source) if isinstance(source, list) else source

        if not source_text.strip():
            continue
        if "os.walk('/kaggle/input')" in source_text:
            continue

        for marker, heading in SECTION_MARKERS:
            if marker in source_text:
                public_cells.append(markdown_cell(heading))
                break

        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        public_cells.append(cell)

    notebook["cells"] = public_cells
    notebook.setdefault("metadata", {}).setdefault(
        "kernelspec",
        {"display_name": "Python 3", "language": "python", "name": "python3"},
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(notebook, stream, ensure_ascii=False, indent=1)
        stream.write("\n")

    print(f"Prepared {output_path} from {source_path}: {len(public_cells)} cells")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    prepare(args.source, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
