# SkyDet model card

## Model summary

SkyDet is an ultra-lightweight, anchor-free satellite object detector reported as the low-footprint baseline for SkySeaLand. The manuscript describes a MobileNetV3-Small backbone, a 64-channel feature pyramid, and a depthwise-separable FCOS-style prediction head.

| Property | Reported value |
|---|---|
| Task | Four-class horizontal object detection |
| Classes | airplane, boat, car, ship |
| Input | 640 x 640, aspect-ratio-preserving letterbox |
| Parameters | 1.22 M |
| Checkpoint size | 4.90 MB |
| Training | 150 epochs; best validation checkpoint at epoch 124 |
| Test mAP50 | 60.50% |
| Test mAP50-95 | 24.32% |
| T4 latency | 13.74 ms/image |
| T4 throughput | 72.8 FPS |

## Design intent

SkyDet quantifies how much detection capability can be retained near a one-million-parameter budget. It is not presented as a state-of-the-art accuracy model. Parameter count, checkpoint size, and latency are reported separately because a smaller network does not automatically execute faster on every device or framework.

## Training and evaluation

- ImageNet-pretrained MobileNetV3-Small backbone.
- Class-weighted focal loss with inverse-frequency class weights.
- Cosine learning-rate decay initialized at 3e-4.
- COCO test metrics over IoU 0.50-0.95 and at IoU 0.50.
- Final score threshold 0.05, NMS IoU 0.45, and at most 300 detections per image.
- Checkpoint selection used the validation split only; the selected checkpoint was then evaluated on the held-out test split.

## Intended use

- Research baselines for resource-constrained satellite object detection.
- Storage-footprint and accuracy trade-off analysis.
- Starting point for tiling, higher-resolution, or scale-aware experiments.

## Out-of-scope use

- Safety-critical surveillance or autonomous decision-making without independent validation.
- Claims of geographic generalization beyond the evaluated data.
- Oriented bounding-box tasks without architectural and annotation changes.
- Direct latency comparisons across different hardware, device counts, precision modes, or timing protocols.

## Limitations

- The 36.18-point gap between mAP50 and mAP50-95 indicates weaker localization at stricter IoU thresholds.
- No final-checkpoint per-class or per-scale AP is available.
- No component ablation isolates the contribution of individual architecture choices.
- Reported detector baselines use unequal, model-specific training budgets and single runs.
- The dataset split is not geographically separated.

## Artifact boundary

The repository's notebook records a development experiment and should not be treated as a byte-for-byte reproduction of the final manuscript checkpoint. Consult [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the exact distinction.
