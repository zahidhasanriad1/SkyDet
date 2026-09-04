# Contributing to SkyDet

Thank you for helping improve SkyDet and the SkySeaLand research artifacts.

## Before opening a change

1. Search existing issues to avoid duplicates.
2. Keep benchmark claims tied to a named dataset split, checkpoint, input size, score threshold, NMS threshold, device, precision mode, warm-up policy, and sample count.
3. Do not replace recorded results without preserving their provenance.
4. Never commit dataset images, credentials, private links, or large checkpoints directly to Git.

## Development setup

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/validate_notebook.py notebooks/skydet-skysealand.ipynb
```

## Pull requests

- Keep each pull request focused on one concern.
- Explain the motivation, implementation, and verification performed.
- For metric changes, provide the complete run configuration and raw evaluation output.
- For notebook changes, clear incidental outputs and make sure the notebook validation script passes.
- Update the dataset card, model card, or reproducibility notes when behavior or claims change.

By contributing, you agree that your code contributions are licensed under the repository's MIT License. Dataset and manuscript artifacts retain their separately stated terms.
