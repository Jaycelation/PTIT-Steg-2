import math

import numpy as np


def image_metrics(original, stego):
    original = original.astype(np.float64)
    stego = stego.astype(np.float64)
    diff = original - stego
    mse = float(np.mean(diff ** 2))
    changed = int(np.count_nonzero(diff))
    if mse == 0:
        psnr = float("inf")
    else:
        psnr = float(20 * math.log10(255.0 / math.sqrt(mse)))
    return {
        "changed_pixel_count": changed,
        "mse": mse,
        "psnr_db": psnr,
    }
