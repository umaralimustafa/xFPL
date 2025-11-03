class Team:
    def __init__(self, manager_id: int, gameweek_id: int):
        self.manager_id = manager_id
        self.gameweek_id = gameweek_id
        self.players = []  # List to hold Player instances