#!/usr/bin/env python3
"""🔬 sc_parser.py — parse Supercell .sc file headers.

Usage:
    python sc_parser.py player.sc
"""
import lzma
import struct
import sys


def parse_sc(path):
    with open(path, "rb") as f:
        data = f.read()

    if data[:2] != b"SC":
        raise ValueError("not a .sc file (bad magic)")

    total_size = struct.unpack(">I", data[2:6])[0]
    header_size = struct.unpack(">I", data[6:10])[0]

    print(f"file:   {path}")
    print(f"magic:  SC")
    print(f"size:   {total_size} bytes (header says {len(data)} on disk)")
    print(f"header: {header_size} bytes")

    # body is LZMA-compressed (starts after magic+sizes)
    try:
        body = lzma.decompress(data[10:])
        print(f"body:   {len(body)} bytes decompressed")
        print(f"head:   {body[:32].hex()}")
    except lzma.LZMAError as e:
        print(f"body:   LZMA decompress failed: {e}")
        print("hint: some .sc use raw zlib or custom packing — check version byte")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python sc_parser.py <file.sc>")
        sys.exit(1)
    parse_sc(sys.argv[1])
