from pathlib import Path

import numpy as np
from PIL import Image


def load_image(path, mode):
    image = Image.open(path).convert(mode)
    return image, np.array(image)


def save_image(array, path, mode):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(array.astype(np.uint8), mode=mode).save(path)
