#!/usr/bin/env python3
"""Score Behance candidates and pick 3. Two rounds on the same CSV.

Round 1: popularity (only the numbers read on Behance)
    python rank_candidates.py candidates.csv --top 8

Round 2: after the AI has reviewed the images and filled visual_* and style,
compute the total and pick 3 works with distinct styles
    python rank_candidates.py candidates.csv --final 3

CSV columns (UTF-8, header row first):
  required  title, url, author, appreciations, views, lists
            lists = which lists it appeared on, separated by ;  e.g. appreciated;viewed;discussed
  optional  comments      comment count from the project page (not shown on the search page)
            year          year published
            excluded      reason if it fails a hard filter (not a phone app, < 6 front screens...); not ranked
            style_guide   yes if the work has a Design Style Guide page (palette, type scale, component specs)
  round 2   visual_polish, visual_hierarchy, visual_hig, visual_nielsen, visual_not_ai
            1-5 each (see the visual review rubric in references/behance-research.md)
            style         5 style tags separated by ;  in this order:
                          background;cards;primary button;radius;imagery   e.g. light;fill;neutral;large;cutout

Popularity (0-1, by percentile within the pool, so results are reproducible):
  appreciations 35% + views 20% + comments 20% + appreciation rate (appreciations/views) 25%,
  plus 0.05 for each extra list it appeared on. Without comment counts, that weight is shared out.
Total = popularity 40% + visual 60%, plus 0.05 with a style guide (author values beat measurements).
Popularity only narrows the field; what looks good is decided by the visual review.
Any two picks must differ in at least 2 of the 5 style tags, so the user has real options later.
"""
import argparse
import csv
import sys

W = {"appreciations": 0.35, "views": 0.20, "comments": 0.20, "rate": 0.25}
VISUAL = ["visual_polish", "visual_hierarchy", "visual_hig", "visual_nielsen", "visual_not_ai"]


def num(v):
    try:
        return float(str(v).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def pct_rank(values):
    """Percentile (0-1) of each value in the list, ties averaged; None stays None."""
    present = sorted(v for v in values if v is not None)
    n = len(present)
    out = []
    for v in values:
        if v is None or n == 0:
            out.append(None)
            continue
        below = sum(1 for x in present if x < v)
        equal = sum(1 for x in present if x == v)
        out.append((below + (equal - 1) / 2) / (n - 1) if n > 1 else 1.0)
    return out


def popularity(rows):
    apps = [num(r.get("appreciations")) for r in rows]
    views = [num(r.get("views")) for r in rows]
    comments = [num(r.get("comments")) for r in rows]
    rates = [a / v if a is not None and v else None for a, v in zip(apps, views)]
    pa, pv, pc, pr = pct_rank(apps), pct_rank(views), pct_rank(comments), pct_rank(rates)
    for i, r in enumerate(rows):
        parts = {"appreciations": pa[i], "views": pv[i], "comments": pc[i], "rate": pr[i]}
        have = {k: v for k, v in parts.items() if v is not None}
        wsum = sum(W[k] for k in have) or 1
        score = sum(W[k] * v for k, v in have.items()) / wsum
        lists = [x for x in (r.get("lists") or "").split(";") if x.strip()]
        score += 0.05 * max(0, len(lists) - 1)
        r["_rate"] = rates[i]
        r["_pop"] = min(score, 1.15)


def visual(r):
    vals = [num(r.get(k)) for k in VISUAL]
    if any(v is None for v in vals):
        return None
    return (sum(vals) / len(vals) - 1) / 4  # 1-5 -> 0-1


def styles_clash(a, b, max_same=3):
    sa = (a.get("style") or "").split(";")
    sb = (b.get("style") or "").split(";")
    same = sum(1 for x, y in zip(sa, sb) if x.strip() and x.strip() == y.strip())
    return same > max_same


def md(s):
    """Escape pipes so titles like "App | UX/UI" do not break Markdown tables."""
    return str(s).replace("|", r"\|")


def fmt(v, pct=False):
    if v is None:
        return "-"
    return f"{v:.1%}" if pct else f"{v:.2f}"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv")
    p.add_argument("--top", type=int, default=8, help="round 1: list the top N by popularity for visual review")
    p.add_argument("--final", type=int, help="round 2: pick N works with distinct styles")
    a = p.parse_args()

    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    pool = [r for r in rows if not (r.get("excluded") or "").strip()]
    if not pool:
        sys.exit("No candidates left to rank (all excluded)")
    popularity(pool)

    if not a.final:
        pool.sort(key=lambda r: r["_pop"], reverse=True)
        print(f"{len(rows)} candidates, {len(rows) - len(pool)} excluded, {len(pool)} ranked.\n")
        print("| # | Work | Author | Appreciations | Views | Comments | Appr. rate | Lists | Popularity |")
        print("|---|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(pool[: a.top], 1):
            print(f"| {i} | [{md(r['title'])}]({r['url']}) | {md(r.get('author', ''))} | {r.get('appreciations', '')} | "
                  f"{r.get('views', '')} | {r.get('comments') or '-'} | {fmt(r['_rate'], True)} | "
                  f"{r.get('lists', '')} | {fmt(r['_pop'])} |")
        return

    scored = []
    for r in pool:
        v = visual(r)
        if v is None:
            continue
        has_guide = (r.get("style_guide") or "").strip().lower() in ("yes", "y", "true", "1")
        r["_vis"] = v
        r["_guide"] = has_guide
        r["_total"] = 0.4 * min(r["_pop"], 1.0) + 0.6 * v + (0.05 if has_guide else 0)
        scored.append(r)
    if not scored:
        sys.exit("No visual_* scores yet: do the visual review first")
    scored.sort(key=lambda r: r["_total"], reverse=True)

    picked, skipped = [], []
    for r in scored:
        clash = next((q for q in picked if styles_clash(r, q)), None)
        if clash:
            skipped.append((r, clash))
            continue
        picked.append(r)
        if len(picked) == a.final:
            break

    print("| # | Work | Popularity | Visual | Style guide | Total | Style |")
    print("|---|---|---|---|---|---|---|")
    for i, r in enumerate(scored, 1):
        mark = " (picked)" if r in picked else ""
        print(f"| {i} | [{md(r['title'])}]({r['url']}){mark} | {fmt(r['_pop'])} | {fmt(r['_vis'])} | "
              f"{'yes' if r['_guide'] else '-'} | {fmt(r['_total'])} | {r.get('style', '')} |")
    for r, q in skipped:
        print(f"\nSkipped \"{r['title']}\": style too close to picked \"{q['title']}\" ({r.get('style')} vs {q.get('style')})")
    if len(picked) < a.final:
        print(f"\nOnly {len(picked)} works with distinct styles: widen the pool in round 1, or check whether the style tags are too coarse.")


if __name__ == "__main__":
    main()
