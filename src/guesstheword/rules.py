import abc


class GameRuleBase(abc.ABC):
    """
    Game rule base class.
    Get current game state and verify rule.

    """
    @abc.abstractmethod
    def is_passed(self, game):
        """
        Verify rule.

        Args:
            game (instance): Current game.

        Returns:
            (bool): True if rule passed. False otherwise.

        """
        return False
