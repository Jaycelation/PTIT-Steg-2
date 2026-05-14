#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.lsb_matching import SECRET_MESSAGE, embed_message


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    output_stego = ROOT / config["output_stego"]
    result = embed_message(
        ROOT / config["image"],
        output_stego,
        int(config["seed"]),
        SECRET_MESSAGE,
    )

    stego_exists = output_stego.is_file()
    log = ROOT / "work" / "embed.log"
    log.parent.mkdir(exist_ok=True)
    log.write_text(
        "\n".join(
            [
                "LSB_MATCHING_EMBED_OK",
                f"output={config['output_stego']}",
                f"stego_exists={str(stego_exists).lower()}",
                f"embedded_bits={result['embedded_bits']}",
                f"changed_pixels={result['changed_pixels']}",
                f"plus_one_count={result['plus_one_count']}",
                f"minus_one_count={result['minus_one_count']}",
            ]
        )
        + "\n"
    )
    print("LSB_MATCHING_EMBED_OK")


if __name__ == "__main__":
    main()
