from abc import ABC, abstractmethod

class League:
    def __init__(self, id: int):
        self.id = id
        self.players = []