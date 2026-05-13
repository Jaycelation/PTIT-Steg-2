#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_io import load_image
from src.metrics import image_metrics


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    stego = ROOT / config["output_stego"]
    if not stego.exists():
        raise SystemExit("Missing work/stego.png. Run tools/run_permutation_embed.py first.")

    _, original = load_image(ROOT / config["image"], config["channel_mode"])
    _, embedded = load_image(stego, config["channel_mode"])
    metrics = image_metrics(original, embedded)
    metrics["status"] = "METRICS_OK"

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print("METRICS_OK")


if __name__ == "__main__":
    main()
