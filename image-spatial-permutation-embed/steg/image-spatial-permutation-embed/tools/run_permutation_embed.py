#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.permutation_codec import SECRET_MESSAGE, embed_message


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    result = embed_message(
        ROOT / config["image"],
        ROOT / config["output_stego"],
        config["channel_mode"],
        config["seed"],
        config["pair_count"],
        SECRET_MESSAGE,
    )

    log = ROOT / "work" / "embed.log"
    log.parent.mkdir(exist_ok=True)
    log.write_text(
        "\n".join(
            [
                "PERMUTATION_EMBED_OK",
                f"output={config['output_stego']}",
                f"embedded_bits={result['embedded_bits']}",
                f"available_pairs={result['available_pairs']}",
                f"swaps={result['swaps']}",
            ]
        )
        + "\n"
    )
    print("PERMUTATION_EMBED_OK")


if __name__ == "__main__":
    main()
