import abc
from operator import methodcaller


class JudgeBase(abc.ABC):
    """
    Judge base class.
    Provide judge logic, score calculating
    and additional game and player restrictions.

    """
    def __init__(self, rules=None, restrictions=None):
        self._rules = rules or ()
        self._restrictions = restrictions or ()

    @abc.abstractmethod
    def get_score(self, player):
        """
        Get player score.

        Args:
            player (instance): Current player.

        Returns:
            (int): Player score.

        """
        return 0

    def is_player_allowed_to_play(self, player):
        """
        Check if there are no any restriction violations for current player.

        Args:
            player (instance): Current player.

        Returns:
            (bool): True if player is allowed to play. False otherwise.

        """
        return all(map(methodcaller('is_passed', player), self._restrictions))

    def is_game_over(self, game):
        """
        Game over flag.

        Args:
            game (instance): Current game.

        Returns:
            (bool): True if game is over. False otherwise.

        """
        return not all(map(methodcaller('is_passed', game), self._rules))
