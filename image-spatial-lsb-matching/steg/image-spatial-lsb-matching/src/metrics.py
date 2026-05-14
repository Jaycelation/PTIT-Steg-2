import math

import numpy as np


def matching_metrics(original, stego):
    original_i = original.astype(np.int16)
    stego_i = stego.astype(np.int16)
    delta = stego_i - original_i
    changed_pixels = int(np.count_nonzero(delta))
    plus_one_count = int(np.count_nonzero(delta == 1))
    minus_one_count = int(np.count_nonzero(delta == -1))
    mse = float(np.mean(delta.astype(np.float64) ** 2))
    psnr = float("inf") if mse == 0 else float(20 * math.log10(255.0 / math.sqrt(mse)))
    return {
        "changed_pixels": changed_pixels,
        "plus_one_count": plus_one_count,
        "minus_one_count": minus_one_count,
        "mse": mse,
        "psnr": psnr,
        "histogram_delta_simple": {
            "-1": minus_one_count,
            "0": int(delta.size - changed_pixels),
            "+1": plus_one_count,
        },
    }
