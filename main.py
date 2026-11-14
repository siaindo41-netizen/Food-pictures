"""food-picture-01 entry: copy the food picture to the output directory.

The repository holds one picture, entry.png (a steaming cheeseburger,
photographed to make you hungry). This program writes those exact bytes
to <output>/entry.png. No network, no randomness, no other files read:
two runs produce byte-identical output.
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(_HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
