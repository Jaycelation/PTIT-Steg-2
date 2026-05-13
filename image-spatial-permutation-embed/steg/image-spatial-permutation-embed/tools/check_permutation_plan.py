#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_io import load_image
from src.permutation_codec import build_pair_plan


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    _, pixels = load_image(ROOT / config["image"], config["channel_mode"])
    pairs = build_pair_plan(pixels, config["seed"], config["pair_count"])
    required = int(config["message_length_bytes"]) * 8
    status = "PERMUTATION_PLAN_OK" if len(pairs) >= required else "PERMUTATION_PLAN_TOO_SMALL"

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "permutation_plan.txt").write_text(
        "\n".join(
            [
                status,
                f"seed={config['seed']}",
                f"requested_pair_count={config['pair_count']}",
                f"valid_pair_count={len(pairs)}",
                f"required_bits={required}",
            ]
        )
        + "\n"
    )
    print(status)


if __name__ == "__main__":
    main()
