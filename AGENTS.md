# GitHub Dashboard

## Project Overview
Multi-dashboard site hosted on GitHub Pages.

Current dashboards:
- Chess champions dashboard with daily auto-updates from the Chess.com API
- Diablo 4 builds dashboard with class and difficulty filtering
- Weather dashboard with zip code lookup
- Dashboard hub page with card navigation

## Tracking
- Keep the `README.md` status table in sync whenever a feature or dashboard changes.
- `README.md` is the source of truth for project progress.

## Structure
- `index.html`: hub page
- `dashboards/`: individual dashboards
- `data/`: JSON backing data
- `.github/workflows/update-chess-data.yml`: daily chess updates plus validation
- `.github/scripts/`: fetch and validation scripts

## Stack
- Static HTML, CSS, and JavaScript
- GitHub Pages on pushes to `main`
- APIs: Chess.com, Open-Meteo, Zippopotam.us
- GitHub Actions for automation

## Adding a Dashboard
1. Create a new HTML file in `dashboards/`.
2. Add a card to `index.html`.
3. If it needs data, add a JSON file in `data/`.
4. Update `README.md` status tracking.

## Diablo 4 Build Updates
- Preferred flow: fetch source content, convert to JSON, then update HTML filters.
- Store data in `data/diablo4-builds.json`.
- Expected fields: `name`, `class`, `difficulty`, `description`, `focus`, `main_skill`, `cost`, `rating`, `tags`.
- Update filters if new classes appear.

## Chess Data
- Chess data is auto-updated daily via GitHub Actions.

## Theme
- Background: `#0a0e27`
- Cards: `#1a1f3a`
- Accent: `#00d084`
- Text: `#e0e0e0`

## Deployment
- Push to `main` to deploy through GitHub Pages.
