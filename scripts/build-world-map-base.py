"""Strip the baked-in route overlay from world-map.png so the map silhouette can
be reused as a plain base layer (nodes and arcs are drawn in SVG instead)."""

import numpy as np
from PIL import Image, ImageFilter

SRC = "scripts/world-map-source.png"
DST = "public/images/world-map-base.png"

# Node centres of the baked overlay, measured on the 1536x1024 source.
DOTS = [(206.9, 456.8), (717.4, 366.7), (780.7, 393.9), (1241.8, 534.0), (1340.3, 451.9), (1163.6, 642.7)]
DOT_RADIUS = 42


def box_pass(arr, radius, axis):
    if radius < 1:
        return arr
    arr = np.moveaxis(arr, axis, 0)
    pad = np.concatenate([np.repeat(arr[:1], radius, 0), arr, np.repeat(arr[-1:], radius, 0)])
    cum = np.concatenate([np.zeros((1,) + arr.shape[1:], np.float32), np.cumsum(pad, 0, dtype=np.float32)])
    out = (cum[2 * radius + 1 :] - cum[: -2 * radius - 1]) / (2 * radius + 1)
    return np.moveaxis(out, 0, axis)


def blur(arr, radius):
    """Three box passes approximate a Gaussian closely enough for this purpose."""
    out = arr.astype(np.float32)
    for _ in range(3):
        out = box_pass(box_pass(out, radius, 0), radius, 1)
    return out


def main():
    rgb = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32)
    h, w, _ = rgb.shape

    # The map itself is a desaturated pale blue; only the route overlay is strongly blue.
    mask = rgb[..., 2] - rgb[..., 0] > 28
    mask = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(15))) > 0

    yy, xx = np.mgrid[0:h, 0:w]
    for cx, cy in DOTS:
        mask |= (xx - cx) ** 2 + (yy - cy) ** 2 <= DOT_RADIUS**2

    keep = (~mask).astype(np.float32)
    filled = rgb * keep[..., None]

    # Coarse-to-fine normalised convolution gives a rough fill...
    for radius in (64, 32, 16, 8, 4, 2, 1):
        den = blur(keep, radius)
        valid = mask & (den > 1e-4)
        for c in range(3):
            est = blur(filled[..., c] * keep, radius) / np.maximum(den, 1e-6)
            filled[..., c] = np.where(valid, est, filled[..., c])

    # ...which is then relaxed towards a harmonic fill so no seam shows at the mask edge.
    for radius, steps in ((2, 120), (1, 60)):
        for _ in range(steps):
            smoothed = blur(filled, radius)
            filled[mask] = smoothed[mask]

    Image.fromarray(np.clip(filled, 0, 255).astype(np.uint8)).save(DST)
    print(f"{DST} written, {mask.sum()} px repainted")


if __name__ == "__main__":
    main()
