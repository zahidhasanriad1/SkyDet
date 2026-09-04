# Reproducibility and provenance

## Artifact map

This repository intentionally distinguishes the finalized manuscript record from the preserved development notebook.

| Artifact | Role | Recorded run |
|---|---|---|
| `paper/SkySeaLand_SkyDet_arXiv_2608.07382v1.pdf` | Final manuscript record | 150 epochs; best checkpoint at epoch 124; 60.50 mAP50; 24.32 mAP50-95 |
| `notebooks/skydet-skysealand.ipynb` | Reference implementation and development record | 100 epochs; best validation mAP 0.20534 at epoch 86; test AP 0.212 and AP50 0.533 in the saved source output |

The two rows are distinct experiments. Do not use the notebook's development metrics as evidence for the manuscript's Table IV values.

## Notebook pipeline

The notebook includes:

1. COCO split auditing and annotated-image overlays.
2. COCO-to-contiguous category mapping for airplane, boat, car, and ship.
3. Aspect-ratio-preserving resize and padding.
4. Albumentations-based training augmentation.
5. MobileNetV3-Small feature extraction.
6. Multi-scale feature fusion and an FCOS-style prediction head.
7. Point assignment, class-weighted focal loss, IoU loss, and centerness loss.
8. COCO JSON export, COCOeval, checkpointing, latency measurement, and optional ONNX export.

## Environment

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

CUDA users should install the PyTorch build matching their CUDA runtime by following the official PyTorch installation selector before installing the remaining packages.

## Data configuration

The notebook defaults to the Kaggle mount:

```python
data_root = "/kaggle/input/datasets/mdzahidhasanriad/skysealand-coco"
```

For local or Colab execution, change `CFG.data_root`. Each split directory must contain its images and `_annotations.coco.json` file.

## Hardware-qualified timing

Latency values are meaningful only when the GPU/CPU, device count, framework and CUDA versions, precision, batch size, input resolution, warm-up, sample count, and preprocessing policy are recorded.

The manuscript reports SkyDet at 13.74 ms per image (72.8 FPS) on one Tesla T4. Cross-dataset timings involving different device counts are provenance only and must not be compared directly.

## Determinism

The notebook seeds Python, NumPy, and PyTorch, but also enables cuDNN benchmarking. GPU kernels, data-loader workers, augmentation libraries, and dependency revisions may therefore produce small run-to-run differences. Exact replication requires a frozen environment, the original checkpoint, and the original hardware/runtime record.

## Validation

The repository CI validates notebook JSON structure and Python syntax without executing the training workload:

```bash
python scripts/validate_notebook.py notebooks/skydet-skysealand.ipynb
```

Execution-level reproduction requires the dataset, a CUDA-capable environment, and the full training budget.
