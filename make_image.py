#!/usr/bin/env python3
"""Draw entry.png: a front-page collage summing up the world news of
Saturday 21 November 2026.

Build-time tool only (uses PIL, which is available on the build machine).
The graded program is main.py, which copies the finished entry.png to the
output directory using only the standard library.

Every headline below was reported on 21 November 2026; see README.md for
the story list and sources.
"""
import math
import random

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (24, 24, 28)
RED = (178, 24, 32)
NAVY = (16, 28, 54)
GOLD = (255, 183, 3)
WHITE = (250, 248, 240)
GREY = (92, 92, 96)
PANEL = (255, 253, 247)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading=1.12):
    x, y = xy
    step = int(fnt.size * leading)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def centered(draw, y, text, fnt, fill, cx=W / 2):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def starburst(draw, cx, cy, r, fill):
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rad = r if i % 2 == 0 else r * 0.38
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=fill)


def lead_art(draw, box):
    """Night sky over a skyline: missile arcs, bursts, a drone."""
    x0, y0, x1, y1 = box
    rng = random.Random(20261121)
    for _ in range(40):  # stars
        draw.point((rng.uniform(x0 + 6, x1 - 6), rng.uniform(y0 + 6, y1 - 130)),
                   fill=(210, 220, 245))
    for (sx, sy, ex, ey) in [
        (x1 - 14, y0 + 30, x0 + 96, y1 - 92),
        (x1 - 66, y0 + 10, x0 + 168, y1 - 92),
        (x1 - 128, y0 + 44, x0 + 40, y1 - 92),
    ]:
        pts = []
        for t in range(41):
            u = t / 40
            pts.append(((1 - u) * sx + u * ex,
                        (1 - u) * sy + u * ey - 80 * u * (1 - u)))
        draw.line(pts, fill=(255, 120, 90), width=3)
        starburst(draw, ex, ey, 16, GOLD)
        starburst(draw, ex, ey, 7, (255, 240, 200))
    dx, dy = x0 + 66, y0 + 58  # drone silhouette
    draw.line((dx - 24, dy - 13, dx + 24, dy + 13), fill=WHITE, width=3)
    draw.line((dx - 24, dy + 13, dx + 24, dy - 13), fill=WHITE, width=3)
    draw.ellipse((dx - 8, dy - 8, dx + 8, dy + 8), outline=WHITE, width=3)
    heights = [42, 64, 34, 78, 52, 88, 40, 60, 48, 70, 36]
    bx = x0 + 6
    for hgt in heights:  # skyline silhouette with lit windows
        bw = rng.randint(24, 36)
        draw.rectangle((bx, y1 - hgt, bx + bw, y1), fill=(6, 10, 22))
        for wy in range(y1 - hgt + 7, y1 - 9, 12):
            for wx in range(bx + 4, bx + bw - 5, 9):
                if rng.random() < 0.4:
                    draw.rectangle((wx, wy, wx + 4, wy + 5), fill=(255, 205, 90))
        bx += bw + 4
        if bx > x1 - 28:
            break


def scales_icon(draw, cx, cy, color):
    draw.line((cx, cy - 32, cx, cy + 28), fill=color, width=5)
    draw.line((cx - 36, cy - 20, cx + 36, cy - 20), fill=color, width=5)
    for sgn in (-1, 1):
        px = cx + sgn * 36
        draw.line((px, cy - 20, px - 12, cy + 5), fill=color, width=3)
        draw.line((px, cy - 20, px + 12, cy + 5), fill=color, width=3)
        draw.arc((px - 14, cy - 2, px + 14, cy + 15), 0, 180, fill=color, width=4)
    draw.line((cx - 19, cy + 32, cx + 19, cy + 32), fill=color, width=5)


def chart_icon(draw, box, color):
    x0, y0, x1, y1 = box
    draw.line((x0, y0, x0, y1), fill=color, width=3)
    draw.line((x0, y1, x1, y1), fill=color, width=3)
    pts = [(x0 + 7, y0 + 12), (x0 + 28, y0 + 9), (x0 + 48, y0 + 26),
           (x0 + 66, y0 + 22), (x0 + 84, y1 - 13)]
    draw.line(pts, fill=color, width=5)
    ex, ey = pts[-1]
    draw.polygon([(ex, ey), (ex - 15, ey - 2), (ex - 3, ey - 13)], fill=color)


def stars_icon(draw, cx, cy):
    for i in range(12):
        ang = 2 * math.pi * i / 12
        starburst(draw, cx + 27 * math.cos(ang), cy + 27 * math.sin(ang), 6, GOLD)
    draw.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), outline=(30, 70, 160), width=3)


def thermo_icon(draw, cx, cy, color):
    draw.rounded_rectangle((cx - 8, cy - 38, cx + 8, cy + 16), 8, outline=color, width=5)
    draw.ellipse((cx - 16, cy + 6, cx + 16, cy + 38), outline=color, width=5)
    draw.line((cx, cy - 24, cx, cy + 18), fill=RED, width=6)
    draw.ellipse((cx - 8, cy + 14, cx + 8, cy + 30), fill=RED)
    for yy in range(cy - 28, cy + 10, 13):
        draw.line((cx + 14, yy, cx + 23, yy), fill=color, width=3)


def pill_icon(draw, cx, cy):
    draw.rounded_rectangle((cx - 32, cy - 12, cx + 32, cy + 12), 12, fill=(46, 140, 90))
    draw.rounded_rectangle((cx, cy - 12, cx + 32, cy + 12), 12, fill=(235, 235, 225))
    draw.line((cx, cy - 12, cx, cy + 12), fill=(30, 100, 62), width=3)
    draw.ellipse((cx + 46, cy - 11, cx + 68, cy + 11), outline=(46, 140, 90), width=4)
    draw.line((cx + 52, cy, cx + 62, cy), fill=(46, 140, 90), width=4)
    draw.line((cx + 57, cy - 5, cx + 57, cy + 5), fill=(46, 140, 90), width=4)


def panel(draw, box, accent, kicker, headline, sub):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL, outline=(200, 192, 172), width=2)
    draw.rectangle((x0, y0, x1, y0 + 8), fill=accent)
    tx = x0 + 118
    draw.text((tx, y0 + 15), kicker, font=font(SANS_B, 16), fill=accent)
    y = text_block(draw, (tx, y0 + 38), headline, font(SANS_B, 24), INK, x1 - tx - 12)
    draw.text((tx, y + 3), sub, font=font(SANS, 17), fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.line((36, 24, W - 36, 24), fill=INK, width=4)
    centered(d, 34, "THE WORLD TODAY", font(SERIF_B, 76), INK)
    d.line((36, 128, W - 36, 128), fill=INK, width=2)
    d.rectangle((0, 136, W, 180), fill=RED)
    centered(d, 143, "SATURDAY  ·  21 NOVEMBER 2026", font(SANS_B, 31), WHITE)

    # ---- lead story ----
    lead = (36, 196, W - 36, 470)
    d.rectangle(lead, fill=NAVY)
    lead_art(d, (676, 210, 972, 456))
    d.text((60, 214), "WAR IN EUROPE  ·  KYIV / WARSAW", font=font(SANS_B, 19), fill=GOLD)
    y = text_block(d, (60, 242),
                   "RUSSIA FIRES 400 DRONES AND 110 MISSILES AT UKRAINE",
                   font(SANS_B, 39), WHITE, 596)
    d.text((60, y + 6), "TWO MISSILES FALL IN POLAND", font=font(SANS_B, 29), fill=GOLD)
    text_block(d, (60, y + 48),
               "Kyiv's bridges and stations hit, at least 8 killed. PM Tusk calls "
               "it a deliberate provocation; NATO jets scramble.",
               font(SANS, 19), (205, 214, 235), 596)

    # ---- four panels, 2 x 2 ----
    pw, ph, gap, gy = 468, 148, 16, 486
    panel(d, (36, gy, 36 + pw, gy + ph), (120, 84, 20),
          "THE HAGUE · JUSTICE",
          "WORLD COURT FINDS MYANMAR GUILTY OF ROHINGYA GENOCIDE",
          "ICJ ruling at The Hague")
    scales_icon(d, 94, gy + 78, (120, 84, 20))
    panel(d, (36 + pw + gap, gy, W - 36, gy + ph), RED,
          "NEW YORK · MARKETS",
          "AI ROUT: S&P 500 FALLS 3.7% INTO CORRECTION",
          "Nasdaq erases its 2026 gains")
    chart_icon(d, (548, gy + 46, 632, gy + 118), RED)
    gy2 = gy + ph + gap
    panel(d, (36, gy2, 36 + pw, gy2 + ph), (30, 70, 160),
          "BRUSSELS · POLITICS",
          "UK AND EU SIGN BIGGEST POST-BREXIT DEAL",
          "Food trade, carbon, youth mobility")
    stars_icon(d, 94, gy2 + 78)
    panel(d, (36 + pw + gap, gy2, W - 36, gy2 + ph), (196, 96, 16),
          "ANTALYA · CLIMATE",
          "COP31 TALKS RUN INTO OVERTIME OVER FOSSIL FUELS",
          "Nearly 200 nations deadlocked")
    thermo_icon(d, 594, gy2 + 74, (196, 96, 16))

    # ---- health strip ----
    hy = gy2 + ph + 14
    d.rectangle((36, hy, W - 36, hy + 66), fill=(232, 244, 234),
                outline=(46, 140, 90), width=2)
    pill_icon(d, 104, hy + 33)
    d.text((192, hy + 8), "LONDON · HEALTH", font=font(SANS_B, 15), fill=(30, 100, 62))
    d.text((192, hy + 29),
           "CANCER PILL: PANCREATIC TUMOURS VANISH IN 1 IN 12 PATIENTS",
           font=font(SANS_B, 20), fill=INK)

    # ---- ticker + footer ----
    ty = hy + 80
    d.rectangle((0, ty, W, ty + 58), fill=INK)
    centered(d, ty + 7,
             "ALSO TODAY:  GEN Z PROTESTS ACROSS 25 EUROPEAN COUNTRIES  ·  6.7 QUAKE SHAKES PERU",
             font(SANS_B, 16), WHITE)
    centered(d, ty + 31,
             "EU GIVES €1BN FOR UKRAINE AIR DEFENCE  ·  US LOSES MEASLES-FREE STATUS",
             font(SANS_B, 16), WHITE)
    centered(d, ty + 68,
             "Reported 21 November 2026 · Sources: France 24, CBS News, El País and wire reports",
             font(SANS, 15), GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
