import os

from guesstheword.score import ScoreSaverBase


class MaxScoreFileSaver(ScoreSaverBase):
    """
    Score saver example.
    Save max score to file.
    If current score less than max in file,
    it won't be saved.

    """
    FILENAME = 'scores.dat'

    def __init__(self, path=None):
        self._path = path or self.get_default_path()

    def get_default_path(self):
        """
        Get default file path if not provided.

        Returns:
            (str): Path.

        """
        return os.path.join(os.getcwd(), self.FILENAME)

    def _get_score(self):
        """
        Get score and player's name from file
        or default values if failed.

        Returns:
            (tuple[int, str]): Player's score, Player's name.

        """
        defaults = 0, 'Incognito'

        # If no score file exist,
        # max score is 0
        if not os.path.exists(self._path):
            return defaults

        # If there are wrong score type in file,
        # max score is 0
        with open(self._path, 'r') as f:
            try:
                score, name = f.readline().split(';')
                return int(score), name
            except (IndexError, ValueError, TypeError):
                return defaults

    def _set_score(self, score, name):
        """
        Save player's score to file.

        Args:
            score (int): Player's score.
            name (str): Player's name.

        Returns: None.

        """
        # Save score to file
        with open(self._path, 'w') as f:
            f.write('{score};{name}'.format(score=score, name=name))

    def get_score_and_name(self):
        return self._get_score()

    def set_score_and_name(self, score, name):
        # Save only if current score
        # greater than saved.
        max_score, _ = self.get_score_and_name()
        if score > max_score:
            self._set_score(score, name)
