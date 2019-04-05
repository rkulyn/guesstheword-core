from guesstheword.judges import JudgeBase


class Judge(JudgeBase):
    """
    Judge example.

    """
    def get_score(self, player):

        try:
            return int(player.passed_attempts / player.failed_attempts * 100)
        except ZeroDivisionError:
            # If no fails at all. Super score!
            return player.passed_attempts * 200
