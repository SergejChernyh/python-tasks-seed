"""
Base85 encoder and decoder
"""

from __future__ import annotations
from beartype import beartype

ENCODE_MAP = \
    b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
DECODE_MAP = {char: idx for idx, char in enumerate(ENCODE_MAP)}

powers85 = (52200625, 614125, 7225, 85, 1)


@beartype
def encode(b: bytes):
    """
    Base85 encoder
    """
    res = bytearray()
    for i in range(0, len(b) - 3, 4):
        val = int.from_bytes(b[i : i + 4])
        res.extend([ENCODE_MAP[val // m % 85] for m in powers85])

    if len(b) % 4:
        val = int.from_bytes(b[len(b) - len(b) % 4 :] + b"\x00" * (4 - len(b) % 4))
        res.extend([ENCODE_MAP[val // m % 85] for m in powers85][: len(b) % 4 + 1])

    return bytes(res)


@beartype
def decode(b: bytes):
    """
    Base85 decoder
    """
    res = bytearray()
    if len(b) % 5 == 1:
        raise ValueError("Incorrect length of the last chunk")

    for i in range(0, len(b) - 4, 5):
        val = sum(DECODE_MAP[b[i + j]] * powers85[j] for j in range(5))
        if val >= 4294967296:
            raise ValueError(f"base85 overflow in hunk starting at byte {i}")
        res.extend(val.to_bytes(4))

    if len(b) % 5:
        last_chunk = b[len(b) - len(b) % 5 :] + b"~" * (5 - len(b) % 5)
        val = sum(DECODE_MAP[last_chunk[j]] * powers85[j] for j in range(5))
        if val >= 4294967296:
            raise ValueError(f"base85 overflow in hunk starting at byte {len(b) - len(b) % 4}")
        res.extend(val.to_bytes(4)[: len(b) % 5 - 1])

    return bytes(res)
