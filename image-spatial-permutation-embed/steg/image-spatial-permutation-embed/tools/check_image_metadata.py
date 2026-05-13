#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_io import load_image


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    image, pixels = load_image(ROOT / config["image"], config["channel_mode"])
    capacity_hint = pixels.size // 2

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "image_metadata.txt").write_text(
        "\n".join(
            [
                "IMAGE_METADATA_OK",
                f"path={config['image']}",
                f"mode={image.mode}",
                f"width={image.width}",
                f"height={image.height}",
                f"pixel_count={pixels.size}",
                f"rough_pair_capacity={capacity_hint}",
            ]
        )
        + "\n"
    )
    print("IMAGE_METADATA_OK")


if __name__ == "__main__":
    main()
