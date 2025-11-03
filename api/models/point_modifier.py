from abc import ABC, abstractmethod
from typing import Any

class PointModifier(ABC):
    _identifier: str
    _points: int | float
    _value: int | float

    @abstractmethod
    def __init__(self, identifier: str, points: int | float, value: int | float) -> None:
        self._identifier = identifier
        self._points = points
        self._value = value

    @property
    def identifier(self) -> str:
        return self._identifier

    @property
    def points(self) -> int | float:
        return self._points

    @property
    def value(self) -> int | float:
        return self._value

class ActualPointModifier(PointModifier):
    def __init__(self, stat_explain: dict[str, Any]):
        identifier: str = stat_explain.get('identifier', '')
        points: int = stat_explain.get('points', 0)
        value: int = stat_explain.get('value', 0)
        points_modification: int = stat_explain.get('points_modification', 0)
        super().__init__(identifier, points + points_modification, value)

class ExpectedPointModifier(PointModifier, ABC):
    def __init__(self, identifier: str, expected_value: float, element_type: int):
        points = self.compute_expected_points(expected_value, element_type)
        super().__init__(identifier, points, expected_value)

    @abstractmethod
    def compute_expected_points(self, expected_value: float, element_type: int) -> float:
        pass

class ExpectedGoalsPointModifier(ExpectedPointModifier):
    POINTS_PER_GOAL_MAP = {1: 10, 2: 6, 3: 5, 4: 4}

    def __init__(self, expected_goals: float, element_type: int):
        identifier: str = 'expected_goals'
        super().__init__(identifier, expected_goals, element_type)

    def compute_expected_points(self, expected_value: float, element_type: int) -> float:
        points_per_goal = self.POINTS_PER_GOAL_MAP.get(element_type, 0)
        return expected_value * points_per_goal