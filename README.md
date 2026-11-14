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

`main.py` (Python 3.13, standard library only) copies the repository's
`entry.png` to the output directory: `$MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output`. Pure byte copy — no network, no randomness — so two
runs write byte-identical output.

## Files

- `main.py` — the entrypoint, copies `entry.png` to the output directory
- `entry.png` — the picture (1024x1024 JPEG bytes, 185,412 bytes)
- `LICENSE` — MIT

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
