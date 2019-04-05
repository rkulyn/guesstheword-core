import datetime

from guesstheword.rules import GameRuleBase


class TimeGameRule(GameRuleBase):
    """
    Time rule.
    Check if current game time is less than game time limit.
    Default is 600 seconds (10 minutes).

    """
    MAX_LIFE_SECONDS = 600

    def __init__(self, life_seconds=None):
        self._life_seconds = (
            life_seconds if life_seconds is not None
            else self.MAX_LIFE_SECONDS
        )

    def is_passed(self, game):
        current = datetime.datetime.now()
        start_datetime = game.start_datetime
        return (start_datetime - current).seconds < self._life_seconds
