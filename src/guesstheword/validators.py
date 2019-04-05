import abc
from .exceptions import ValidationError


class InputValidatorBase(abc.ABC):
    """
    Input validator base class.
    Validate input against restrictions.

    """
    DEFAULT_MASSAGE = 'Invalid input.'

    def __init__(self, message=None):
        self._message = message or self.get_message()

    @abc.abstractmethod
    def is_valid(self, value, **kwargs):
        """
        Check whether input value is valid..

        Args:
            value (str): Input value.
            **kwargs (dict): Additional options.

        Returns:
            (bool): True if validation is passed. False otherwise.

        """
        return False

    def get_message(self):
        """
        Get message if it is not provided.

        Returns:
            (str): Message.

        """
        return self.DEFAULT_MASSAGE

    def validate(self, value, **kwargs):
        """
        Validate input.

        Args:
            value (str): Input value.
            **kwargs (dict): Additional options.

        Returns: None.

        Raises: ValidationError if validation failed.

        """
        if not self.is_valid(value, **kwargs):
            raise ValidationError(self._message)
