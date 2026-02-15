# GitHub Dashboard - Project Guide

## Project Overview
A multi-dashboard site hosted on GitHub Pages. Currently features a chess champions dashboard with daily auto-updates from Chess.com API.

## Tracking & Status
Check the README.md for project status and feature progress. Update the status table as work completes.

## Key Files & Structure
```
├── index.html                          # Main hub page
├── dashboards/
│   └── chess-champions.html           # Chess dashboard
├── data/
│   └── chess-champions.json           # Chess data (auto-updated daily)
├── .github/
│   ├── workflows/
│   │   └── update-chess-data.yml      # Daily chess data fetch
│   └── scripts/
│       └── fetch_chess_data.py        # Chess.com API script
└── README.md                           # Project status & docs
```

## Tech Stack
- Static HTML/CSS/JavaScript
- GitHub Pages (branch deployment from main)
- Chess.com API (free, no auth required)
- GitHub Actions (daily scheduler)

## Adding New Dashboards
1. Create new HTML file in `dashboards/`
2. Add card to `index.html` hub with link
3. If data needed: create JSON file in `data/`, add to README status

## Updating Build Data Quickly

### Diablo 4 Builds
**Best method: WebFetch → JSON → HTML filters** (Tested & fastest)
1. WebFetch maxroll.gg tier list (fast, reliable, clean data)
2. Extract top N builds from fetched content
3. Write to `data/diablo4-builds.json` with fields: name, class, difficulty, description, focus, main_skill, cost, rating, tags
4. Update HTML filters (`<select>`) if new classes appear
5. Commit all changes

Why: WebFetch is ~2x faster than WebSearch, returns exact data, no API limitations

**Frequency:** Update after major patches or seasons

### Chess Champions
Chess data auto-updates daily via GitHub Actions workflow (`update-chess-data.yml`). No manual updates needed.

## Color Theme
- Background: `#0a0e27` (dark navy)
- Cards: `#1a1f3a` (lighter navy)
- Accent: `#00d084` (muted green)
- Text: `#e0e0e0` (soft gray)

## Deployment
- Push to main branch → GitHub Pages auto-deploys in 1-5 minutes
- Workflows run on schedule or manual trigger
