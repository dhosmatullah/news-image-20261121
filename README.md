# The World Today — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/dhosmatullah/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/dhosmatullah/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world's news of **Saturday 21 November 2026**, drawn as a newspaper front page: a masthead and date band, one lead story with a night-sky illustration, four story panels with icons, a health strip and an "Also today" ticker.

The program (`main.py`, Python 3, standard library only) copies the finished image (`entry.png`, 1024×1024 PNG, drawn at build time by `make_image.py`) to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). It needs no network and writes identical bytes on every run.

## The day's stories shown

All events were reported on 21 November 2026:

1. **War in Europe (lead)** — Russia fired more than 400 drones and about 110 missiles at Ukraine overnight; Kyiv's bridges and railway stations were hit and at least 8 people killed. Two Russian missiles and a suspected drone came down in Poland; Prime Minister Tusk called it a deliberate provocation and NATO scrambled jets. *(France 24, CBS News, El País via One Turn News, 21 Nov 2026)*
2. **Justice** — The International Court of Justice in The Hague found Myanmar responsible for genocide against the Rohingya; Britain expelled Myanmar's envoy. *(One Turn News and wire reports, 21 Nov 2026)*
3. **Markets** — An AI-sector sell-off pushed the S&P 500 down 3.7% into correction territory and wiped out the Nasdaq's 2026 gains; the Nikkei fell about 5%. *(One Turn News market report, 21 Nov 2026)*
4. **Politics** — The UK and the EU signed their biggest post-Brexit agreements in Brussels, covering food exports, carbon markets and youth mobility. *(One Turn News, 21 Nov 2026)*
5. **Climate** — The COP31 climate summit in Antalya, Turkey ran past its deadline into overtime as nearly 200 nations deadlocked over fossil fuels. *(One Turn News, 21 Nov 2026)*
6. **Health** — In a trial of the pill daraxonrasib, pancreatic-cancer tumours became undetectable in one in 12 patients. *(One Turn News, 21 Nov 2026)*
7. **Ticker** — Gen Z protests across 25 European countries; a magnitude 6.7 earthquake in Peru; the EU's €1 billion for Ukrainian drones and air defence; the US losing its measles-elimination status. *(One Turn News, 21 Nov 2026)*

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, under 1 MiB)
```

To redraw the image from scratch (build machine only, needs Pillow and DejaVu fonts):

```sh
python3 make_image.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=0trcj9y5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
