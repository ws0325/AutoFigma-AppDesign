#!/usr/bin/env python3
"""WCAG 2.x contrast ratio checker.

Usage:
    python contrast.py "#808080" "#FFFFFF"          # one pair
    python contrast.py "#808080" "#FFFFFF" --size 15 --bold
    python contrast.py --pairs pairs.txt            # one "fg bg [size] [bold]" per line

Thresholds follow Apple HIG / WCAG AA:
    text <= 17 pt (not bold): 4.5:1
    text >= 18 pt, or bold:   3:1
"""
import argparse
import sys


def parse_hex(value: str):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) == 8:  # ignore alpha
        v = v[:6]
    if len(v) != 6:
        raise ValueError(f"not a hex colour: {value}")
    return tuple(int(v[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    def channel(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    l1, l2 = luminance(parse_hex(fg)), luminance(parse_hex(bg))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def check(fg, bg, size=None, bold=False):
    r = ratio(fg, bg)
    large = bold or (size is not None and size >= 18)
    need = 3.0 if large else 4.5
    verdict = "PASS" if r >= need else "FAIL"
    label = "large/bold text" if large else "text <=17pt"
    if size is None and not bold:
        label = "small text (assumed)"
    return f"{fg} on {bg}: {r:.2f}:1  need {need}:1 for {label}  -> {verdict}"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("fg", nargs="?")
    p.add_argument("bg", nargs="?")
    p.add_argument("--size", type=float, help="font size in pt")
    p.add_argument("--bold", action="store_true")
    p.add_argument("--pairs", help="file with lines: fg bg [size] [bold]")
    a = p.parse_args()

    if a.pairs:
        with open(a.pairs, encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                # skip blank lines and comments ("# note", "// note"); hex colours like "#111" are kept
                if len(parts) < 2 or parts[0] in ("#", "//") or parts[0].startswith("//"):
                    continue
                size = float(parts[2]) if len(parts) > 2 else None
                bold = len(parts) > 3 and parts[3].lower() in ("bold", "b", "1", "true")
                print(check(parts[0], parts[1], size, bold))
    elif a.fg and a.bg:
        print(check(a.fg, a.bg, a.size, a.bold))
    else:
        p.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
