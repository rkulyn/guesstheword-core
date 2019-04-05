import abc


class VocabularyBase(abc.ABC):
    """
    Vocabulary base class.
    Provide word with hint
    to use in game.

    """
    @abc.abstractmethod
    def get_word_and_hint(self):
        """
        Get word and hint to guess it.

        Returns:
            (tuple): Word, hint.

        """
        return 'word', 'hint for word'
