import abc


class PlayerRestrictionBase(abc.ABC):
    """
    Player restriction base class.
    Get current player state and verify restrictions.

    """
    @abc.abstractmethod
    def is_passed(self, player):
        """
        Verify restriction.

        Args:
            player (instance): Current player.

        Returns:
            (bool): True if restriction is not violated. False otherwise.

        """
        return False
