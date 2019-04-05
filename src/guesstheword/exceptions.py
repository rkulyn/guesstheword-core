class ValidationError(Exception):
    """
    Base validation exception
    to use with validators.

    """
    pass


class MaxPlayersExceededError(Exception):
    """
    Base player count exception
    to raise when players limit is exceeded.

    """
    pass
