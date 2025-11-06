from typing import Any

class Pick:
    def __init__(self, player_id: int, gameweek_id: int):
        self.player_id = player_id
        self.gameweek_id = gameweek_id
        self.element_type = 0
        self.team = 0

        self.fixture = 0
        self.minutes = 0
        self.goals_scored = 0
        self.assists = 0
        self.clean_sheets = 0
        self.goals_conceded = 0
        self.own_goals = 0
        self.penalties_saved = 0
        self.penalties_missed = 0
        self.yellow_cards = 0
        self.red_cards = 0
        self.saves = 0
        self.bonus = 0
        self.bps = 0
        self.influence = 0.0
        self.creativity = 0.0
        self.threat = 0.0
        self.ict_index = 0.0
        self.clearances_blocks_interceptions = 0
        self.recoveries = 0
        self.tackles = 0
        self.defensive_contribution = 0
        self.starts = 0
        self.expected_goals = 0.0
        self.expected_assists = 0.0
        self.expected_goal_involvements = 0.0
        self.expected_goals_conceded = 0.0
        self.total_points = 0
        self.in_dreamteam = False
    
    def populate_stats(self, gameweek_data: list[dict[str, Any]], players_data: list[dict[str, Any]]) -> None:
        # Find player in gameweek data by player_id
        pick_stats = next((stat_dict for stat_dict in gameweek_data if stat_dict.get('id') == self.player_id), None)
        if not pick_stats:
            raise ValueError(f"No statistics found for player ID {self.player_id} in the provided gameweek data.")
        
        self.minutes: int = pick_stats.get('minutes', 0)
        self.goals_scored: int = pick_stats.get('goals_scored', 0)
        self.assists: int = pick_stats.get('assists', 0)
        self.clean_sheets: int = pick_stats.get('clean_sheets', 0)
        self.goals_conceded: int = pick_stats.get('goals_conceded', 0)
        self.own_goals: int = pick_stats.get('own_goals', 0)
        self.penalties_saved: int = pick_stats.get('penalties_saved', 0)
        self.penalties_missed: int = pick_stats.get('penalties_missed', 0)
        self.yellow_cards: int = pick_stats.get('yellow_cards', 0)
        self.red_cards: int = pick_stats.get('red_cards', 0)
        self.saves: int = pick_stats.get('saves', 0)
        self.bonus: int = pick_stats.get('bonus', 0)
        self.bps: int = pick_stats.get('bps', 0)
        self.influence: float = float(pick_stats.get('influence', 0.0))
        self.creativity: float = float(pick_stats.get('creativity', 0.0))
        self.threat: float = float(pick_stats.get('threat', 0.0))
        self.ict_index: float = float(pick_stats.get('ict_index', 0.0))
        self.clearances_blocks_interceptions: int = pick_stats.get('clearances_blocks_interceptions', 0)
        self.recoveries: int = pick_stats.get('recoveries', 0)
        self.tackles: int = pick_stats.get('tackles', 0)
        self.defensive_contribution: int = pick_stats.get('defensive_contribution', 0)
        self.starts: int = pick_stats.get('starts', 0)
        self.expected_goals: float = float(pick_stats.get('expected_goals', 0.0))
        self.expected_assists: float = float(pick_stats.get('expected_assists', 0.0))
        self.expected_goal_involvements: float = float(pick_stats.get('expected_goal_involvements', 0.0))
        self.expected_goals_conceded: float = float(pick_stats.get('expected_goals_conceded', 0.0))
        self.total_points: int = pick_stats.get('total_points', 0)
        self.in_dreamteam: bool = pick_stats.get('in_dreamteam', False)

        player_stats = next((player_dict for player_dict in players_data if player_dict.get('id') == self.player_id), None)
        if not player_stats:
            raise ValueError(f"No player data found for player ID {self.player_id} in the provided players data.")
        
        self.element_type: int = player_stats.get('element_type', 0)
        self.team: int = player_stats.get('team', 0)

        # TODO
        # Add point modifiers processing here