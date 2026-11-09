#!/usr/bin/env python3
"""Grid extraction: one cell = one pixel (one @1x design pixel, i.e. 1 pt).

Why pt: when designers say "pixel" in Figma they mean an @1x point (an iPhone 15/16
is 393 wide). The phone in a Behance image has been scaled up or down, so the script
first scales the screen back to its design width. Each cell you read is then one
pixel in the Figma file and can go straight into the spec. (Add --unit px to work
in raw image pixels instead.)

Use --crop to frame ONE screen first (original-image pixel coordinates, screen
content only, not the phone case).

Subcommands
  info      Scale factor, and whether the image is sharp enough for 1-cell accuracy
  overview  Whole-screen grid (thin line every 8 cells, labelled thick line every 40), for locating things
  zoom      Enlarge a region with one line per cell and coordinates every 8 cells, for details
  edges     Scan one row or column for colour boundaries; prints margins, sizes and gaps
  colors    Dominant colours with their share
  sample    Colour at given coordinates

Examples
  python grid_extract.py info     shot.png --crop 120,80,520,946
  python grid_extract.py overview shot.png --crop 120,80,520,946 -o shot_overview.png
  python grid_extract.py zoom     shot.png --crop 120,80,520,946 --region 0,180,80,320 -o shot_card_corner.png
  python grid_extract.py edges    shot.png --crop 120,80,520,946 --row 250
  python grid_extract.py edges    shot.png --crop 120,80,520,946 --col 100
  python grid_extract.py colors   shot.png --crop 120,80,520,946 --top 8
  python grid_extract.py sample   shot.png --crop 120,80,520,946 --at 24,120 200,400

Requires Pillow: pip install pillow
"""
import argparse
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install pillow")

# Behance "source" images can be very tall (5600 x 30000+ px). Allow up to ~400 MP
# instead of Pillow's default ~179 MP decompression-bomb guard.
Image.MAX_IMAGE_PIXELS = 400_000_000


# ---------- basics ----------

def load(a):
    img = Image.open(a.image).convert("RGB")
    if a.crop:
        x0, y0, x1, y1 = (int(v) for v in a.crop.split(","))
        img = img.crop((x0, y0, x1, y1))
    return img


def ppu(img, a):
    """Original-image pixels per cell (one unit)."""
    if a.unit == "px":
        return 1.0
    return img.width / a.width_pt


def font(size):
    for name in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "Helvetica.ttc"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def hexc(rgb):
    return "#%02X%02X%02X" % rgb


def unit_name(a):
    return "px" if a.unit == "px" else "pt"


def draw_grid(img, s, step, major, origin=(0.0, 0.0), label_size=11):
    """Draw a grid on an already scaled image. s = screen pixels per unit; origin = unit coords of the top-left corner."""
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    f = font(label_size)
    ox, oy = origin
    w_u, h_u = img.width / s, img.height / s

    def lines(length_u, start, vertical):
        k = int(-(-start // step))  # first whole step at or after start
        v = k * step
        while v <= start + length_u + 1e-6:
            p = round((v - start) * s)
            is_major = abs(v / major - round(v / major)) < 1e-6
            color = (255, 0, 80) if vertical else (0, 110, 255)
            alpha = 170 if is_major else 70
            width = 2 if is_major else 1
            if vertical:
                d.line([(p, 0), (p, img.height)], fill=color + (alpha,), width=width)
                if is_major:
                    d.text((p + 2, 1), f"{v:g}", fill=color + (255,), font=f)
            else:
                d.line([(0, p), (img.width, p)], fill=color + (alpha,), width=width)
                if is_major and p > 0:  # leave the top-left corner to the x label so they do not overlap
                    d.text((2, p + 1), f"{v:g}", fill=color + (255,), font=f)
            v += step

    lines(w_u, ox, True)
    lines(h_u, oy, False)
    return Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")


# ---------- subcommands ----------

def cmd_info(a):
    img = load(a)
    s = ppu(img, a)
    u = unit_name(a)
    print(f"Screen in image: {img.width}x{img.height} px; 1 {u} = {s:.3f} image px; "
          f"screen is about {img.width / s:.0f}x{img.height / s:.0f} {u}")
    if s < 1:
        print(f"WARNING: less than 1 image pixel per cell. 1-cell accuracy is not possible; "
              f"error is about +/-{1 / s:.1f} {u}. Look for a larger image of the same work.")
    elif s < 2:
        print("Note: 1-2 image pixels per cell; edges may be off by 1 cell (compression and anti-aliasing).")
    else:
        print("Sharp enough for 1-cell measurement (still mind compression and anti-aliasing in presentation images).")


def cmd_overview(a):
    img = load(a)
    s = ppu(img, a)
    zoom = max(1.0, 3.0 / s)  # at least 3 screen pixels per unit so thin lines stay visible
    if zoom > 1:
        img = img.resize((round(img.width * zoom), round(img.height * zoom)), Image.LANCZOS)
    out = draw_grid(img, s * zoom, a.step, a.major, label_size=max(11, int(s * zoom * 5)))
    out.save(a.output)
    print(f"Saved {a.output}: thin line every {a.step:g} {unit_name(a)}, labelled thick line every {a.major:g} "
          f"(red = x, blue = y). Use zoom for 1-cell detail and edges for exact values.")


def cmd_zoom(a):
    img = load(a)
    s = ppu(img, a)
    x0, y0, x1, y1 = (float(v) for v in a.region.split(","))
    box = (round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s))
    part = img.crop(box)
    cell = a.cell  # screen pixels per cell after enlarging
    w, h = round((x1 - x0) * cell), round((y1 - y0) * cell)
    if w * h > 40_000_000:
        sys.exit("Region too large: shrink --region or lower --cell")
    part = part.resize((w, h), Image.NEAREST)  # nearest neighbour keeps pixel blocks crisp
    out = draw_grid(part, cell, 1, a.major, origin=(x0, y0), label_size=max(11, cell))
    out.save(a.output)
    print(f"Saved {a.output}: region x {x0:g}-{x1:g}, y {y0:g}-{y1:g} {unit_name(a)}; "
          f"1 cell = 1 {unit_name(a)} (enlarged {cell}x); coordinates every {a.major:g} cells.")
    if s < 1:
        print("WARNING: the image has less than 1 pixel per cell, so blocks are larger than 1 cell and readings are approximate.")


def cmd_edges(a):
    img = load(a)
    s = ppu(img, a)
    u = unit_name(a)
    if (a.row is None) == (a.col is None):
        sys.exit("Use exactly one of --row or --col")
    if a.row is not None:
        y = min(img.height - 1, max(0, round(a.row * s)))
        pixels = [img.getpixel((x, y)) for x in range(img.width)]
        axis, where = "x", f"row y = {a.row:g} {u}"
    else:
        x = min(img.width - 1, max(0, round(a.col * s)))
        pixels = [img.getpixel((x, y)) for y in range(img.height)]
        axis, where = "y", f"column x = {a.col:g} {u}"

    def diff(p, q):
        return max(abs(p[0] - q[0]), abs(p[1] - q[1]), abs(p[2] - q[2]))

    # Start a new segment when the colour differs from the segment's start colour by more than
    # the threshold; merge segments shorter than --min into the previous one (anti-aliasing, noise).
    segs = []
    start, ref = 0, pixels[0]
    for i in range(1, len(pixels)):
        if diff(pixels[i], ref) > a.threshold:
            segs.append([start, i, ref])
            start, ref = i, pixels[i]
    segs.append([start, len(pixels), ref])
    min_px = max(1, round(a.min * s))
    merged = []
    for seg in segs:
        if merged and seg[1] - seg[0] < min_px:
            merged[-1][1] = seg[1]
        else:
            merged.append(seg)

    print(f"{where}: {len(merged)} segments (threshold {a.threshold}, segments shorter than {a.min:g} {u} merged)\n")
    print(f"| {axis} from | {axis} to | length | colour |\n|---|---|---|---|")
    for st, en, _ in merged:
        mid = pixels[(st + en - 1) // 2]  # sample the middle to avoid anti-aliased edges
        print(f"| {st / s:.1f} | {en / s:.1f} | {(en - st) / s:.1f} {u} | {hexc(mid)} |")
    print("\nHow to read: where two segments meet is an element edge; round to the nearest cell for the spec.")


def cmd_colors(a):
    img = load(a)
    small = img.copy()
    small.thumbnail((300, 300))
    q = small.quantize(colors=a.top * 2, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in counts)
    print("| hex | share |\n|---|---|")
    for c, idx in counts[: a.top]:
        print(f"| {hexc(tuple(pal[idx * 3: idx * 3 + 3]))} | {c / total:.1%} |")
    print("\nNote: presentation images are compressed and colour-graded, so these are approximate; "
          "sample text colours at the stroke centre with `sample`.")


def cmd_sample(a):
    img = load(a)
    s = ppu(img, a)
    for pt in a.at:
        xu, yu = (float(v) for v in pt.split(","))
        x, y = min(img.width - 1, round(xu * s)), min(img.height - 1, round(yu * s))
        print(f"({xu:g}, {yu:g}) {unit_name(a)} -> {hexc(img.getpixel((x, y)))}")


# ---------- arguments ----------

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("image")
        sp.add_argument("--crop", help="x0,y0,x1,y1: one screen's pixel box in the original image")
        sp.add_argument("--width-pt", type=float, default=393,
                        help="design width of this screen: 393 for iPhone 15/16, 402 for 16 Pro, 375 older, 430/440 Pro Max")
        sp.add_argument("--unit", choices=["pt", "px"], default="pt",
                        help="pt (default) = @1x design pixels; px = original image pixels")

    sp = sub.add_parser("info"); common(sp); sp.set_defaults(fn=cmd_info)

    sp = sub.add_parser("overview"); common(sp)
    sp.add_argument("--step", type=float, default=8, help="cells between thin lines, default 8; use 1 for a line every cell")
    sp.add_argument("--major", type=float, default=40, help="cells between thick labelled lines, default 40")
    sp.add_argument("-o", "--output", default="overview.png")
    sp.set_defaults(fn=cmd_overview)

    sp = sub.add_parser("zoom"); common(sp)
    sp.add_argument("--region", required=True, help="x0,y0,x1,y1 in cells: the region to enlarge")
    sp.add_argument("--cell", type=int, default=12, help="screen pixels per cell after enlarging, default 12")
    sp.add_argument("--major", type=float, default=8, help="label coordinates every N cells, default 8")
    sp.add_argument("-o", "--output", default="zoom.png")
    sp.set_defaults(fn=cmd_zoom)

    sp = sub.add_parser("edges"); common(sp)
    sp.add_argument("--row", type=float, help="scan this row (y, in cells) left to right")
    sp.add_argument("--col", type=float, help="scan this column (x, in cells) top to bottom")
    sp.add_argument("--threshold", type=int, default=5,
                    help="colour difference (0-255) that counts as an edge, default 5; a white card on #F8F8F8 differs by only 7")
    sp.add_argument("--min", type=float, default=2, help="segments shorter than this many cells are noise, default 2")
    sp.set_defaults(fn=cmd_edges)

    sp = sub.add_parser("colors"); common(sp)
    sp.add_argument("--top", type=int, default=10)
    sp.set_defaults(fn=cmd_colors)

    sp = sub.add_parser("sample"); common(sp)
    sp.add_argument("--at", nargs="+", required=True, help="coordinates in cells, e.g. 24,120")
    sp.set_defaults(fn=cmd_sample)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
