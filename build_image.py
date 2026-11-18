#!/usr/bin/env python3
"""Render the Wednesday 18 November 2026 front page as a 1024x1024 PNG.

Everything is fixed: the six stories, the layout, the fonts. Running this
script twice writes byte-identical files. It only runs on my own machine;
the entry itself (main.py) just copies the finished entry.png.
"""

from PIL import Image as PILImage, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
PAPER = (253, 246, 227)
BLACK = (17, 17, 17)
RUST = (178, 34, 34)
MUTE = (90, 90, 90)
GOLD = (255, 210, 0)
WHITE = (255, 255, 255)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

MARGIN = 24

STORIES = [
    {"head": "1  US–IRAN CLASH ESCALATES",
     "body": "The US says it destroyed five Iranian tankers overnight; Iran strikes ships and a US base in Jordan as Gulf shipping braces for more."},
    {"head": "2  KERCH BRIDGE HIT A SECOND NIGHT",
     "body": "Ukraine strikes the Crimea bridge again while Russia hits bridges in Kyiv, days before a summit of Trump, Putin and Xi."},
    {"head": "3  CYCLONE AKVAN BEARS DOWN",
     "body": "The storm strengthens over the Bay of Bengal and is set to cross the Andhra Pradesh coast around noon on Friday 20 November."},
    {"head": "4  NVIDIA DOUBLES REVENUE",
     "body": "The chip giant reports $115.8 billion for the quarter, up 103% on a year earlier, and its board rules out Huang's return."},
    {"head": "5  COP31 ENTERS DECISIVE PHASE",
     "body": "Climate negotiators in Antalya work through a draft deal with 144 disputed items as the summit heads for its Friday close."},
    {"head": "6  PATTINSON IS THE NEW BOND",
     "body": "British actor Robert Pattinson is named the next James Bond, taking over 007."},
]


def load(path, size):
    return ImageFont.truetype(path, size)


def split_lines(canvas, text, face, width):
    out = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if canvas.textlength(trial, font=face) <= width:
            current = trial
        elif current:
            out.append(current)
            current = word
        else:
            current = word
    if current:
        out.append(current)
    return out


def draw_lines(canvas, x, y, lines, face, color, spacing=None):
    step = spacing if spacing is not None else int(face.size * 1.25)
    for line in lines:
        canvas.text((x, y), line, font=face, fill=color)
        y += step
    return y


canvas = PILImage.new("RGB", (PAGE_W, PAGE_H), PAPER)
pen = ImageDraw.Draw(canvas)

pen.rectangle([0, 0, PAGE_W, 44], fill=BLACK)
pen.text((MARGIN, 10), "WEDNESDAY 18 NOVEMBER 2026", font=load(SANS_BOLD, 22), fill=WHITE)
tag = "THE WORLD IN ONE IMAGE"
pen.text((PAGE_W - MARGIN - pen.textlength(tag, font=load(SANS_BOLD, 22)), 10),
         tag, font=load(SANS_BOLD, 22), fill=GOLD)

top = 62
pen.text((MARGIN, top), "THE WORLD", font=load(SERIF_BOLD, 108), fill=BLACK)
top += 118
pen.text((MARGIN, top), "One day, six stories  —  Wednesday 18 November 2026",
         font=load(SANS_BOLD, 26), fill=RUST)
top += 44
pen.line([(MARGIN, top), (PAGE_W - MARGIN, top)], fill=BLACK, width=4)
top += 18

lead = STORIES[0]
lead_lines = split_lines(pen, lead["body"], load(SANS_PLAIN, 24), PAGE_W - 80)
lead_h = 34 + len(lead_lines) * 30 + 28
pen.rectangle([MARGIN, top, PAGE_W - MARGIN, top + lead_h], outline=RUST, width=3)
pen.text((40, top + 14), lead["head"], font=load(SANS_BOLD, 32), fill=RUST)
draw_lines(pen, 40, top + 60, lead_lines, load(SANS_PLAIN, 24), BLACK, 30)
top += lead_h + 16

cell_w = (PAGE_W - 48 - 16) // 2
cell_h = 168
for pos, story in enumerate(STORIES[1:5]):
    gx = MARGIN + (pos % 2) * (cell_w + 16)
    gy = top + (pos // 2) * (cell_h + 16)
    pen.rectangle([gx, gy, gx + cell_w, gy + cell_h], outline=BLACK, width=2)
    head_lines = split_lines(pen, story["head"], load(SANS_BOLD, 19), cell_w - 28)[:2]
    draw_lines(pen, gx + 14, gy + 10, head_lines, load(SANS_BOLD, 19), BLACK, 23)
    body_lines = split_lines(pen, story["body"], load(SANS_PLAIN, 19), cell_w - 28)[:4]
    draw_lines(pen, gx + 14, gy + 10 + len(head_lines) * 23 + 8,
               body_lines, load(SANS_PLAIN, 19), BLACK, 24)
top += 2 * cell_h + 16 + 16

last = STORIES[5]
pen.rectangle([MARGIN, top, PAGE_W - MARGIN, top + 108], fill=BLACK)
pen.text((40, top + 12), last["head"], font=load(SANS_BOLD, 24), fill=GOLD)
tail_lines = split_lines(pen, last["body"], load(SANS_PLAIN, 20), PAGE_W - 80)
draw_lines(pen, 40, top + 48, tail_lines, load(SANS_PLAIN, 20), WHITE, 26)
top += 108 + 14

pen.text((MARGIN, PAGE_H - 34),
         "Sources: AP, Reuters, BBC, Al Jazeera, CNBC  —  18 Nov 2026",
         font=load(SANS_PLAIN, 18), fill=MUTE)

canvas.save("entry.png", format="PNG", optimize=True)
print("saved entry.png")
