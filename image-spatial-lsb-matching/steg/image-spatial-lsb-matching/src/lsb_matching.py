import hashlib
import random

from .image_io import load_grayscale, save_grayscale


SECRET_MESSAGE = "PTIT spatial LSB Matching lab: +/-1 embedding changes pixels gently."


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


def positions_for_bits(pixel_count, bit_count, seed):
    if bit_count > pixel_count:
        raise ValueError("Message is larger than image capacity.")
    rng = random.Random(int(seed))
    return rng.sample(range(pixel_count), bit_count)


def matching_delta(value, rng):
    if value == 0:
        return 1
    if value == 255:
        return -1
    return 1 if rng.randrange(2) == 1 else -1


def embed_message(input_path, output_path, seed, message):
    _, pixels = load_grayscale(input_path)
    flat = pixels.reshape(-1).copy()
    bits = bytes_to_bits(message.encode("utf-8"))
    positions = positions_for_bits(flat.size, len(bits), seed)
    rng = random.Random(int(seed) ^ 0x5A17)

    changed = 0
    plus_one = 0
    minus_one = 0
    for position, bit in zip(positions, bits):
        original = int(flat[position])
        current_lsb = original & 1
        if current_lsb == int(bit):
            continue
        delta = matching_delta(original, rng)
        updated = original + delta
        flat[position] = updated
        changed += 1
        if delta > 0:
            plus_one += 1
        else:
            minus_one += 1

    save_grayscale(flat.reshape(pixels.shape), output_path)
    return {
        "embedded_bits": len(bits),
        "changed_pixels": changed,
        "plus_one_count": plus_one,
        "minus_one_count": minus_one,
        "positions_used": len(positions),
    }


def extract_message(stego_path, seed, message_length_bytes):
    _, pixels = load_grayscale(stego_path)
    bit_count = int(message_length_bytes) * 8
    flat = pixels.reshape(-1)
    positions = positions_for_bits(flat.size, bit_count, seed)
    bits = [int(flat[position]) & 1 for position in positions]
    return bits_to_bytes(bits).decode("utf-8")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
