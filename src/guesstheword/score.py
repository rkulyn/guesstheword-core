import abc


class ScoreSaverBase(abc.ABC):
    """
    Score saver base class.
    Provide saving and retrieving
    logic for user scores.

    """
    @abc.abstractmethod
    def get_score_and_name(self):
        """
        Get max score for game.

        Returns:
            (tuple[int, str]): Player's score, Player's name.

        """
        return 0, 'Incognito'

    @abc.abstractmethod
    def set_score_and_name(self, score, name):
        """
        Save player's score.

        Args:
            score (int): Player's score.
            name (str): Player's name.

        Returns: None.

        """
        return None
