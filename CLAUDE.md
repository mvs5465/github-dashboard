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
For dashboards with manual data (like Diablo 4 builds):
1. **Fetch data**: Use WebFetch tool to grab tier lists or data from source (e.g., maxroll.gg)
2. **Identify top entries**: Extract top N builds/entries from the fetched data
3. **Update JSON**: Write new data to `data/[dashboard]-builds.json` with key fields (name, class, difficulty, description, etc.)
4. **Update filters**: Add any new classes/categories to the select dropdowns in the dashboard HTML if needed
5. **Commit**: Stage all changes and commit with a clear message

Example: Updating D4 builds took 3 steps:
- WebFetch maxroll tier list → identified top 5
- Write to `data/diablo4-builds.json`
- Edit dashboard HTML to add Paladin/Spiritborn classes
- Commit with one git push

## Color Theme
- Background: `#0a0e27` (dark navy)
- Cards: `#1a1f3a` (lighter navy)
- Accent: `#00d084` (muted green)
- Text: `#e0e0e0` (soft gray)

## Deployment
- Push to main branch → GitHub Pages auto-deploys in 1-5 minutes
- Workflows run on schedule or manual trigger
