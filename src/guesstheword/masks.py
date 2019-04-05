import abc


class WordMaskBase(abc.ABC):
    """
    Provide mask behaviour according to word.

    """
    @abc.abstractmethod
    def create(self, word):
        """
        Create masked word for given word.

        Args:
            word (str): Word.

        Returns:
            (any) Masked word.

        """
        return word

    @abc.abstractmethod
    def update(self, letter, word, masked):
        """
        Update current masked word with current letter.

        Args:
            letter (str): Letter.
            word (str): Word.
            masked (any): Current masked word.

        Returns:
            (any) Updated mask.

        """
        return masked

    @abc.abstractmethod
    def is_opened(self, masked):
        """
        Check if all letters are opened in masked word.

        Args:
            masked (any): Current masked word.

        Returns:
            (bool): True if all letters are opened. False. otherwise.

        """
        return False
