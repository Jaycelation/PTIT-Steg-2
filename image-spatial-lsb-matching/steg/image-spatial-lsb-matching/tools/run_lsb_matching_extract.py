#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.lsb_matching import extract_message, sha256_text


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    message = extract_message(
        ROOT / config["output_stego"],
        int(config["seed"]),
        int(config["message_length_bytes"]),
    )
    digest = sha256_text(message)

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    (work / "answer.txt").write_text(message + "\n")
    (work / "answer.sha256").write_text(digest + "\n")
    (work / "extract.log").write_text(
        "\n".join(
            [
                "LSB_MATCHING_EXTRACT_OK",
                f"message_length_bytes={len(message.encode('utf-8'))}",
                f"sha256={digest}",
            ]
        )
        + "\n"
    )
    print("LSB_MATCHING_EXTRACT_OK")


if __name__ == "__main__":
    main()
