import hashlib

from .image_io import load_image, save_image


SECRET_MESSAGE = "ATTT spatial LSB lab: recover this message from the stego image."


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


def embed_message(input_path, output_path, mode, bits_per_channel, message):
    if bits_per_channel != 1:
        raise ValueError("This lab supports exactly 1 LSB per channel.")

    image, pixels = load_image(input_path, mode)
    flat = pixels.reshape(-1).copy()
    message_bytes = message.encode("utf-8")
    bits = bytes_to_bits(message_bytes)
    if len(bits) > flat.size:
        raise ValueError("Message is larger than image LSB capacity.")

    changes = 0
    for idx, bit in enumerate(bits):
        original = int(flat[idx])
        updated = (original & 0xFE) | bit
        if updated != original:
            changes += 1
        flat[idx] = updated

    stego = flat.reshape(pixels.shape)
    save_image(stego, output_path, image.mode)
    return {"embedded_bits": len(bits), "changed_channels": changes}


def extract_message(stego_path, mode, message_length_bytes):
    _, pixels = load_image(stego_path, mode)
    bit_count = int(message_length_bytes) * 8
    bits = [int(value) & 1 for value in pixels.reshape(-1)[:bit_count]]
    return bits_to_bytes(bits).decode("utf-8")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
