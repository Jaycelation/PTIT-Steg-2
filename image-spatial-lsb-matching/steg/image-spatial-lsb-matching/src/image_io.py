from pathlib import Path

import numpy as np
from PIL import Image


def load_grayscale(path):
    image = Image.open(path).convert("L")
    pixels = np.array(image, dtype=np.uint8)
    return image, pixels


def save_grayscale(pixels, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    clipped = np.clip(pixels, 0, 255).astype(np.uint8)
    Image.fromarray(clipped, mode="L").save(path)


def capacity_bits(pixels):
    return int(pixels.size)
