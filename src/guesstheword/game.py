import datetime


class GuessTheWordGame:
    """
    Guess The Word game.
    Accept letter and check if it is in hidden word.
    User wins if all letters are guessed.

    Additional restrictions and score count
    are provided by 'judge' instance.

    Hidden word are provided by 'vocabulary' instance.

    """
    def __init__(self, vocabulary, mask):

        word, hint = vocabulary.get_word_and_hint()

        self._mask = mask
        self._word = word
        self._hint = hint
        self._used_letters = set()
        self._masked = mask.create(word)
        self._start_datetime = datetime.datetime.now()

    @property
    def is_victory(self):
        """
        Game over (victory) flag.

        Returns:
            (bool): True if all letters are guessed.

        """
        return self._mask.is_opened(self._masked)

    @property
    def used_letters(self):
        """
        Used letters.

        Returns:
            (set): Used letters.

        """
        return self._used_letters

    @property
    def start_datetime(self):
        """
        Game start datetime.

        Returns:
            (datetime): Game start datetime.

        """
        return self._start_datetime

    @property
    def hint(self):
        """
        Word hint to helping guess.

        Returns:
            (str): Hint.

        """
        return self._hint

    @property
    def word(self):
        """
        Get hidden word as symbols.

        Returns:
            (list): List of letters of hidden word.

        """
        return self._masked

    def _open_letter(self, letter):
        """
        Open given letter if it exists in word.

        Args:
            letter (str): Current letter.

        Returns: None.

        """
        self._masked = self._mask.update(
            letter,
            self._word,
            self._masked
        )

    def _remember_letter(self, letter):
        """
        Update game state. Add current letter to set of used.

        Args:
            letter (str): Current letter.

        Returns: None.

        """

        self._used_letters.add(letter)

    def guess(self, letter):
        """
        Main game method.
        Open guessed letter.
        Update game state.

        Args:
            letter (str): Guessing letter.

        Returns:
            (bool) True if letter in hidden word.

        """
        if letter in self._word:
            self._open_letter(letter)
            success = True
        else:
            success = False

        self._remember_letter(letter)

        return success
