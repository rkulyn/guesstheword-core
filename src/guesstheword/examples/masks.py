from guesstheword.masks import WordMaskBase


class NoneWordMask(WordMaskBase):
    """
    Create masked word as list of None(s).

    """
    def create(self, word):
        return [None] * len(word)

    def update(self, letter, word, masked):
        for idx, real_letter in enumerate(word):
            if real_letter == letter:
                masked[idx] = letter

        return masked

    def is_opened(self, masked):
        return None not in masked
