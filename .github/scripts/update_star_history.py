"""Generate a self-hosted Star History chart using the GitHub API."""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = "Neusoft-Intelligent-Laboratory/FridayOS-Lite"
OUTPUT = Path("docs/images/star-history.svg")
WIDTH, HEIGHT = 900, 420
LEFT, TOP, RIGHT, BOTTOM = 70, 35, 25, 55


def fetch_stars():
    token = os.environ["GITHUB_TOKEN"]
    stars = []
    page = 1
    while True:
        request = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}/stargazers?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github.star+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "FridayOS-Lite-star-history",
            },
        )
        with urllib.request.urlopen(request) as response:
            batch = json.load(response)
        stars.extend(batch)
        if len(batch) < 100:
            return stars
        page += 1


def read_stars():
    if "--stdin" not in sys.argv:
        return fetch_stars()
    pages = json.load(sys.stdin)
    return [star for page in pages for star in page]


def render(stars):
    dates = [datetime.fromisoformat(star["starred_at"].replace("Z", "+00:00")) for star in stars]
    now = datetime.now(timezone.utc)
    start = min(dates, default=now)
    span = max((now - start).total_seconds(), 1)
    plot_w = WIDTH - LEFT - RIGHT
    plot_h = HEIGHT - TOP - BOTTOM
    maximum = max(len(dates), 1)

    points = [(LEFT, TOP + plot_h)]
    for count, date in enumerate(dates, 1):
        x = LEFT + ((date - start).total_seconds() / span) * plot_w
        y = TOP + plot_h - (count / maximum) * plot_h
        points.append((x, y))
    points.append((LEFT + plot_w, points[-1][1]))
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area = f"{LEFT},{TOP + plot_h} {line} {LEFT + plot_w},{TOP + plot_h}"

    grid = []
    for step in range(5):
        y = TOP + plot_h - step * plot_h / 4
        value = round(maximum * step / 4)
        grid.append(f'<line x1="{LEFT}" y1="{y:.1f}" x2="{LEFT + plot_w}" y2="{y:.1f}" class="grid"/>')
        grid.append(f'<text x="{LEFT - 12}" y="{y + 5:.1f}" text-anchor="end" class="label">{value}</text>')

    start_label = start.strftime("%Y-%m-%d")
    end_label = now.strftime("%Y-%m-%d")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">FridayOS-Lite Star History</title>
<desc id="desc">{len(dates)} GitHub stars from {start_label} to {end_label}</desc>
<style>
  .bg {{ fill: #ffffff; }} .grid {{ stroke: #e5e7eb; stroke-width: 1; }}
  .label {{ fill: #6b7280; font: 13px system-ui, sans-serif; }}
  .title {{ fill: #111827; font: 600 20px system-ui, sans-serif; }}
  .area {{ fill: #6366f1; opacity: .12; }} .line {{ fill: none; stroke: #4f46e5; stroke-width: 3; }}
  @media (prefers-color-scheme: dark) {{ .bg {{ fill: #0d1117; }} .grid {{ stroke: #30363d; }} .label {{ fill: #8b949e; }} .title {{ fill: #f0f6fc; }} .area {{ fill: #818cf8; }} .line {{ stroke: #818cf8; }} }}
</style>
<rect class="bg" width="100%" height="100%" rx="10"/>
<text x="{LEFT}" y="25" class="title">Star History · {len(dates)} stars</text>
{''.join(grid)}
<polygon points="{area}" class="area"/><polyline points="{line}" class="line"/>
<text x="{LEFT}" y="{HEIGHT - 18}" class="label">{start_label}</text>
<text x="{LEFT + plot_w}" y="{HEIGHT - 18}" text-anchor="end" class="label">{end_label}</text>
</svg>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render(read_stars())
