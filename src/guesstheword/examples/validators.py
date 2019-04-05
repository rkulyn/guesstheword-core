from guesstheword.validators import InputValidatorBase


class InputLengthValidator(InputValidatorBase):
    """
    Validate that input value has correct length.

    """
    MAX_LENGTH = 1

    def __init__(self, message=None, length=None):
        self._length = (
            length if length is not None
            else self.MAX_LENGTH
        )
        super().__init__(message)

    def get_message(self):
        return 'Input length should be {length} characters.'.format(length=self._length)

    def is_valid(self, value, **kwargs):
        return len(value) == self._length
