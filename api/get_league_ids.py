import requests
from typing import Any

def get_league_ids(user_id: int) -> tuple[list[str], list[str]]:
    url = f"https://fantasy.premierleague.com/api/entry/{user_id}/"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch FPL entry data for user ID {user_id}. Response status: {response.status_code}")
    
    entry_data: dict[str, Any] = response.json()
    leagues_data: dict[str, Any] = entry_data.get('leagues', {})

    classic_leagues: list[dict[str, Any]] = leagues_data.get('classic', [])
    h2h_leagues: list[dict[str, Any]] = leagues_data.get('h2h', [])
    
    classic_league_ids: list[str] = [str(league.get('id')) for league in classic_leagues if league.get('id') is not None]
    h2h_league_ids: list[str] = [str(league.get('id')) for league in h2h_leagues if league.get('id') is not None]
    return classic_league_ids, h2h_league_ids