"""food-picture-01 entry: write the food picture to the output directory.

The repository holds the picture as base64 text in image.b64 (one line).
This program decodes it and writes the exact JPEG bytes to
<output>/entry.png. No network, no randomness, no other files read:
two runs produce byte-identical output.
"""

import base64
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(_HERE, "image.b64")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "r", encoding="ascii") as f:
        text = f.read()
    data = base64.b64decode("".join(text.split()))
    # The payload must be the JPEG picture: a JPEG starts with FF D8.
    if data[:2] != b"\xff\xd8":
        raise ValueError("decoded image is not a JPEG")
    with open(dst, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
