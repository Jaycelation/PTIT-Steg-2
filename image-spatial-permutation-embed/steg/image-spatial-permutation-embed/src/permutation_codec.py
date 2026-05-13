import hashlib
import random

import numpy as np

from .image_io import load_image, save_image


SECRET_MESSAGE = "ATTT permutation pair-order lab: recover this message from swapped pixel pairs."


def bytes_to_bits(data):
    bits = []
    for byte in data:
        for shift in range(7, -1, -1):
            bits.append((byte >> shift) & 1)
    return bits


def bits_to_bytes(bits):
    out = bytearray()
    for offset in range(0, len(bits), 8):
        value = 0
        for bit in bits[offset : offset + 8]:
            value = (value << 1) | int(bit)
        out.append(value)
    return bytes(out)


def build_pair_plan(reference_pixels, seed, pair_count):
    flat = reference_pixels.reshape(-1)
    rng = random.Random(int(seed))
    pairs = []
    seen = set()
    attempts = 0
    max_attempts = int(pair_count) * 200
    while len(pairs) < int(pair_count) and attempts < max_attempts:
        i = rng.randrange(flat.size)
        j = rng.randrange(flat.size)
        attempts += 1
        if i == j:
            continue
        a, b = (i, j) if i < j else (j, i)
        if (a, b) in seen:
            continue
        seen.add((a, b))
        if int(flat[i]) == int(flat[j]):
            continue
        pairs.append((i, j))
    return pairs


def embed_message(input_path, output_path, mode, seed, pair_count, message):
    image, pixels = load_image(input_path, mode)
    flat = pixels.reshape(-1).copy()
    pairs = build_pair_plan(pixels, seed, pair_count)
    bits = bytes_to_bits(message.encode("utf-8"))
    if len(bits) > len(pairs):
        raise ValueError("Not enough non-equal pixel pairs for the message.")

    swaps = 0
    for bit, (i, j) in zip(bits, pairs):
        left = int(flat[i])
        right = int(flat[j])
        relation_is_one = left > right
        if int(bit) != int(relation_is_one):
            flat[i], flat[j] = flat[j], flat[i]
            swaps += 1

    stego = flat.reshape(pixels.shape)
    save_image(stego, output_path, image.mode)
    return {"embedded_bits": len(bits), "available_pairs": len(pairs), "swaps": swaps}


def extract_message(reference_path, stego_path, mode, seed, pair_count, message_length_bytes):
    _, reference = load_image(reference_path, mode)
    _, stego = load_image(stego_path, mode)
    pairs = build_pair_plan(reference, seed, pair_count)
    bit_count = int(message_length_bytes) * 8
    if bit_count > len(pairs):
        raise ValueError("The configured message length exceeds the pair plan capacity.")

    flat = stego.reshape(-1)
    bits = []
    for i, j in pairs[:bit_count]:
        bits.append(1 if int(flat[i]) > int(flat[j]) else 0)
    return bits_to_bytes(bits).decode("utf-8")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def changed_pixel_count(original, stego):
    return int(np.count_nonzero(original != stego))
