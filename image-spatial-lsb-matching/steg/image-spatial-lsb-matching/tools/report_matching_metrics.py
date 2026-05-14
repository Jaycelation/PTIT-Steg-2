#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_io import load_grayscale
from src.metrics import matching_metrics


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    _, original = load_grayscale(ROOT / config["image"])
    _, stego = load_grayscale(ROOT / config["output_stego"])
    metrics = matching_metrics(original, stego)
    metrics["status"] = "METRICS_OK"

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")
    print("METRICS_OK")


if __name__ == "__main__":
    main()
