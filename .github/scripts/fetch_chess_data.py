#!/usr/bin/env python3
import json
import requests
from datetime import datetime

# List of players to track (world champion + top players)
PLAYERS = [
    'gukesh',           # World Champion
    'magnuscarlsen',
    'ding',
    'fabiano-caruana',
    'alireza-firouzja',
    'shakhriyar-mamedyarov',
    'wesley-so',
    'teimour-radjabov',
    'daniil-dubov',
    'leinier-dominguez'
]

BASE_URL = 'https://api.chess.com/pub/player'

def fetch_player_data(username):
    """Fetch player data from Chess.com API"""
    try:
        response = requests.get(f'{BASE_URL}/{username}', timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            'username': username,
            'name': data.get('name', username),
            'title': data.get('title', ''),
            'country': data.get('country', ''),
            'url': data.get('url', ''),
            'is_world_champion': 'gukesh' in username.lower()
        }
    except Exception as e:
        print(f"Error fetching {username}: {e}")
        return None

def fetch_player_ratings(username):
    """Fetch player's current ratings"""
    try:
        response = requests.get(f'{BASE_URL}/{username}/stats', timeout=10)
        response.raise_for_status()
        data = response.json()

        ratings = {}

        # Extract ratings from different time controls
        if 'chess_blitz' in data:
            ratings['blitz'] = data['chess_blitz'].get('last', {}).get('rating', 0)
        if 'chess_rapid' in data:
            ratings['rapid'] = data['chess_rapid'].get('last', {}).get('rating', 0)
        if 'chess_bullet' in data:
            ratings['bullet'] = data['chess_bullet'].get('last', {}).get('rating', 0)

        return ratings
    except Exception as e:
        print(f"Error fetching ratings for {username}: {e}")
        return {}

def main():
    """Main function to fetch all player data"""
    champions_data = []

    print("Fetching chess champions data...")

    for username in PLAYERS:
        print(f"Fetching data for {username}...")

        # Get player info
        player_info = fetch_player_data(username)
        if not player_info:
            continue

        # Get player ratings
        ratings = fetch_player_ratings(username)
        player_info['ratings'] = ratings

        # Calculate highest rating across formats
        if ratings:
            player_info['max_rating'] = max(ratings.values()) if ratings.values() else 0
        else:
            player_info['max_rating'] = 0

        champions_data.append(player_info)

    # Sort by max rating
    champions_data.sort(key=lambda x: x['max_rating'], reverse=True)

    # Add timestamp
    output = {
        'last_updated': datetime.utcnow().isoformat() + 'Z',
        'champions': champions_data
    }

    # Ensure data directory exists
    import os
    os.makedirs('data', exist_ok=True)

    # Write to JSON file
    with open('data/chess-champions.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Updated {len(champions_data)} players")
    print("Data written to data/chess-champions.json")

if __name__ == '__main__':
    main()
