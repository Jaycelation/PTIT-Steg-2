#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_io import image_capacity_bits, load_image


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    image_path = ROOT / config["image"]
    image, pixels = load_image(image_path, config["channel_mode"])
    capacity = image_capacity_bits(pixels, config["bits_per_channel"])
    required = int(config["message_length_bytes"]) * 8
    status = "IMAGE_METADATA_OK" if capacity >= required else "IMAGE_METADATA_TOO_SMALL"

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "image_metadata.txt").write_text(
        "\n".join(
            [
                status,
                f"path={config['image']}",
                f"mode={image.mode}",
                f"width={image.width}",
                f"height={image.height}",
                f"capacity_bits={capacity}",
                f"required_bits={required}",
            ]
        )
        + "\n"
    )
    print(status)


if __name__ == "__main__":
    main()
