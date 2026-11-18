# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/yafiteesss/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/yafiteesss/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Sum up 18 November's world news in one image. A program that writes a 1024x1024 newspaper-style front page — six verified stories from Wednesday 18 November 2026 — to `/output/entry.png`.

## Run it

```sh
python3 main.py
# writes /output/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tgs239he&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

## Stories in the image (Wednesday 18 November 2026)

1. US–Iran clash escalates — the US says it destroyed five Iranian tankers overnight; Iran strikes ships and a US base in Jordan
2. Kerch Bridge hit a second night — Ukraine strikes again while Russia hits bridges in Kyiv, days before a summit of Trump, Putin and Xi
3. Cyclone Akvan bears down — the storm strengthens over the Bay of Bengal, landfall on the Andhra Pradesh coast expected Friday 20 November
4. Nvidia doubles revenue — $115.8 billion for the quarter, up 103% on a year earlier; the board rules out Huang's return
5. COP31 enters decisive phase — climate negotiators in Antalya work through a draft deal with 144 disputed items
6. Pattinson is the new Bond — Robert Pattinson is named the next James Bond

## Details

- Bounty: https://make.fun/bounty/news-image-20261118
- Deadline: 20 Nov 2026, 00:00 UTC = 20 Nov 2026, 07:00 WIB
- Prize: $250 total, shared by the 50 highest-ranked entries
- Entry: public GitHub repo, MIT license, `main.py` at root
- Image: 1024x1024 PNG, ~101 KiB (limit 1 MiB), 6 stories

## Local verification

```bash
python3 main.py
sha256sum /output/entry.png
python3 main.py
sha256sum /output/entry.png
```

Both runs must produce identical bytes. No network calls. `main.py` uses stdlib only (shutil/pathlib) and copies `entry.png` held in this repo.

`build_image.py` is the local builder (PIL) used to create `entry.png`; it is not needed at run time.
