#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.permutation_codec import extract_message, sha256_text


def main():
    config = json.loads((ROOT / "output" / "public_config.json").read_text())
    work = ROOT / "work"
    stego = ROOT / config["output_stego"]
    if not stego.exists():
        raise SystemExit("Missing work/stego.png. Run tools/run_permutation_embed.py first.")

    message = extract_message(
        ROOT / config["image"],
        stego,
        config["channel_mode"],
        config["seed"],
        config["pair_count"],
        config["message_length_bytes"],
    )
    digest = sha256_text(message)
    work.mkdir(exist_ok=True)
    (work / "answer.txt").write_text(message + "\n")
    (work / "answer.sha256").write_text(digest + "\n")
    (work / "extract.log").write_text(
        "\n".join(["PERMUTATION_EXTRACT_OK", f"message_length_bytes={len(message.encode('utf-8'))}", f"sha256={digest}"])
        + "\n"
    )
    print("PERMUTATION_EXTRACT_OK")


if __name__ == "__main__":
    main()
