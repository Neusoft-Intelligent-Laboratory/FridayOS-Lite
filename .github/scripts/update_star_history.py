"""Generate a self-hosted Star History chart from GitHub stargazer data."""

import json
import os
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime
from pathlib import Path

REPO = "Neusoft-Intelligent-Laboratory/FridayOS-Lite"
OUTPUT = Path("docs/images/star-history.svg")
WIDTH, HEIGHT = 900, 420
LEFT, TOP, RIGHT, BOTTOM = 70, 35, 25, 55


def fetch_stars():
    token = os.environ.get("STAR_HISTORY_TOKEN")
    if not token:
        raise SystemExit("STAR_HISTORY_TOKEN is required to read stargazer history")

    stars = []
    page = 1
    while True:
        request = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}/stargazers?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github.star+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2026-03-10",
                "User-Agent": "FridayOS-Lite-star-history",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                batch = json.load(response)
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")[:500]
            raise SystemExit(
                f"GitHub stargazers API returned HTTP {error.code}: {detail}"
            ) from error

        stars.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    count_request = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "FridayOS-Lite-star-history",
        },
    )
    try:
        with urllib.request.urlopen(count_request, timeout=30) as response:
            expected = json.load(response)["stargazers_count"]
    except (urllib.error.HTTPError, KeyError) as error:
        raise SystemExit("Unable to verify the repository's current star count") from error

    if len(stars) != expected:
        raise SystemExit(
            f"Refusing to replace the chart: fetched {len(stars)} of {expected} stars"
        )
    return stars


def read_stars():
    if "--stdin" not in sys.argv:
        return fetch_stars()

    payload = json.load(sys.stdin)
    if payload and isinstance(payload[0], list):
        return [star for page in payload for star in page]
    return payload


def parse_dates(stars):
    if not stars:
        raise SystemExit("No stargazers returned; refusing to replace the existing chart")
    try:
        return sorted(
            datetime.fromisoformat(star["starred_at"].replace("Z", "+00:00"))
            for star in stars
        )
    except (KeyError, TypeError) as error:
        raise SystemExit(
            "GitHub response did not include starred_at timestamps; check API access"
        ) from error


def render(stars):
    timestamps = parse_dates(stars)
    days = [timestamp.date() for timestamp in timestamps]
    daily_counts = Counter(days)

    fallback = date(1970, 1, 1)
    start = min(days, default=fallback)
    end = max(days, default=fallback)
    span = max((end - start).days, 1)
    plot_w = WIDTH - LEFT - RIGHT
    plot_h = HEIGHT - TOP - BOTTOM
    maximum = max(len(days), 1)

    points = [(LEFT, TOP + plot_h)]
    cumulative = 0
    for day, count in sorted(daily_counts.items()):
        cumulative += count
        x = LEFT + ((day - start).days / span) * plot_w
        y = TOP + plot_h - (cumulative / maximum) * plot_h
        points.append((x, y))
    if not days:
        points.append((LEFT + plot_w, TOP + plot_h))

    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area = f"{LEFT},{TOP + plot_h} {line} {LEFT + plot_w},{TOP + plot_h}"

    grid = []
    for step in range(5):
        y = TOP + plot_h - step * plot_h / 4
        value = round(maximum * step / 4)
        grid.append(
            f'<line x1="{LEFT}" y1="{y:.1f}" x2="{LEFT + plot_w}" '
            f'y2="{y:.1f}" class="grid"/>'
        )
        grid.append(
            f'<text x="{LEFT - 12}" y="{y + 5:.1f}" text-anchor="end" '
            f'class="label">{value}</text>'
        )

    start_label = start.isoformat()
    end_label = end.isoformat()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">FridayOS-Lite Star History</title>
<desc id="desc">{len(days)} GitHub stars from {start_label} to {end_label}</desc>
<style>
  .bg {{ fill: #ffffff; }} .grid {{ stroke: #e5e7eb; stroke-width: 1; }}
  .label {{ fill: #6b7280; font: 13px system-ui, sans-serif; }}
  .title {{ fill: #111827; font: 600 20px system-ui, sans-serif; }}
  .area {{ fill: #6366f1; opacity: .12; }} .line {{ fill: none; stroke: #4f46e5; stroke-width: 3; }}
  @media (prefers-color-scheme: dark) {{ .bg {{ fill: #0d1117; }} .grid {{ stroke: #30363d; }} .label {{ fill: #8b949e; }} .title {{ fill: #f0f6fc; }} .area {{ fill: #818cf8; }} .line {{ stroke: #818cf8; }} }}
</style>
<rect class="bg" width="100%" height="100%" rx="10"/>
<text x="{LEFT}" y="25" class="title">Star History · {len(days)} stars</text>
{''.join(grid)}
<polygon points="{area}" class="area"/><polyline points="{line}" class="line"/>
<text x="{LEFT}" y="{HEIGHT - 18}" class="label">{start_label}</text>
<text x="{LEFT + plot_w}" y="{HEIGHT - 18}" text-anchor="end" class="label">{end_label}</text>
</svg>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as output:
        output.write(svg)


if __name__ == "__main__":
    render(read_stars())
