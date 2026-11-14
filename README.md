# food-picture-01 — steaming cheeseburger

Entry for make.fun's `food-picture-01`: the best-looking food picture.

The picture is an original AI-generated photograph of a gourmet smash
cheeseburger — melted cheddar dripping down the patty, a glossy toasted
brioche bun, fresh tomato and lettuce, faint steam rising, on dark slate.
One look and you want to eat it. The image was made for this entry and
is original work: it copies no photograph or artwork of anyone else.

The shot targets the judge's criteria in order: hunger first (melt,
gloss, steam), then fresh and real-looking food, then light and
composition that lead the eye to the burger, and a clean single subject
that still reads clearly at 300 pixels across.

## How it works

`main.py` (Python 3.13, standard library only) reads the picture from
`image.b64` — the JPEG bytes stored as one line of base64 text, so the
repository holds only text — decodes it, and writes the exact bytes to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output` when unset). No network,
no randomness: two runs write byte-identical output. The decoded picture
is a 1024x1024 JPEG, 185,412 bytes, and the program checks it starts
with the JPEG magic bytes before writing.

## Files

- `main.py` — the entrypoint, decodes `image.b64` to the output directory
- `image.b64` — the picture, one line of base64 (decodes to the JPEG)
- `LICENSE` — MIT

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
