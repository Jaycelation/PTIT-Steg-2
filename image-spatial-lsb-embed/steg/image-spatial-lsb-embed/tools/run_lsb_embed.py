#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.lsb_codec import SECRET_MESSAGE, embed_message


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    output_stego = ROOT / config["output_stego"]
    result = embed_message(
        ROOT / config["image"],
        output_stego,
        config["channel_mode"],
        int(config["bits_per_channel"]),
        SECRET_MESSAGE,
    )

    log = ROOT / "work" / "embed.log"
    log.parent.mkdir(exist_ok=True)
    log.write_text(
        "\n".join(
            [
                "LSB_EMBED_OK",
                f"output={config['output_stego']}",
                f"embedded_bits={result['embedded_bits']}",
                f"changed_channels={result['changed_channels']}",
            ]
        )
        + "\n"
    )
    print("LSB_EMBED_OK")


if __name__ == "__main__":
    main()
