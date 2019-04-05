from guesstheword.restrictions import PlayerRestrictionBase


class MaxFailsPlayerRestriction(PlayerRestrictionBase):
    """
    Max fails count restriction.
    Check if current fails count is less than threshold.
    Default is 5 fails.

    """
    MAX_FAILS = 5

    def __init__(self, max_fails=None):
        self._max_fails = (
            max_fails if max_fails is not None
            else self.MAX_FAILS
        )

    def is_passed(self, player):
        return player.failed_attempts < self._max_fails
