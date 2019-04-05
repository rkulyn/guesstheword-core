import abc
import uuid


class PlayerBase:
    """
    Player base class.

    """
    def __init__(self, name=None):
        self._is_active = True
        self._is_winner = False
        self._failed_attempts = 0
        self._passed_attempts = 0
        self._id = self.generate_id()
        self._name = name or self.generate_name()

    @staticmethod
    def generate_id():
        """
        Generate player ID.

        Returns:
            (UUID): Player ID.

        """
        return uuid.uuid4()

    @staticmethod
    def generate_name():
        """
        Generate name if not provided,

        Returns:
            (str): Name.

        """
        return 'Incognito'

    @property
    def name(self):
        """
        Player's name.

        Returns:
            (str): Name.

        """
        return self._name

    @property
    def id(self):
        """
        Player ID.

        Returns:
            (str): Player ID as string.

        """
        return str(self._id)

    @property
    def is_active(self):
        """
        Activity flag.

        Returns:
            (bool): True if player is active. False otherwise.

        """
        return self._is_active

    @property
    def is_winner(self):
        """
        Player victory flag.

        Returns:
            (bool): True if player won the game. False otherwise.

        """
        return self._is_winner

    @property
    def passed_attempts(self):
        """
        Passed attempts count.

        Returns:
            (int): Passed attempts count.

        """
        return self._passed_attempts

    @property
    def failed_attempts(self):
        """
        Failed attempts count.

        Returns:
            (int): Failed attempts count.

        """
        return self._failed_attempts

    def got_it(self):
        """
        Passed attempt handler.

        Returns: None.

        """
        self._passed_attempts += 1

    def missed(self):
        """
        Failed attempt handler.

        Returns: None.

        """
        self._failed_attempts += 1

    def left_game(self):
        """
        Set user inactive if he left the game.

        Returns: None.

        """
        self._is_active = False

    def win_game(self):
        """
        Set user as winner if he won the game.

        Returns: None.

        """
        self._is_winner = True


class PlayerManagerBase(abc.ABC):
    """
    Player manager base class.

    """
    def __init__(self, max_players=1):
        self._max_players = max_players

    @property
    @abc.abstractmethod
    def current_player(self):
        """
        Current player.

        Returns:
            (instance, None): Player instance or None if not found.

        """
        return None

    @property
    @abc.abstractmethod
    def active_players(self):
        """
        Active players.

        Returns:
            (list): Active players.

        """
        return []

    @abc.abstractmethod
    def add_player(self, player):
        """
        Add player to the game.

        Args:
            player (instance): Player instance.

        Returns: None.

        """
        return None

    @abc.abstractmethod
    def next_player(self):
        """
        Shift order to the next player.
        Set next active player as current (if exists).

        Returns: None.

        """
        return None

    @property
    def active_players_count(self):
        """
        Count of active players.

        Returns:
            (int): Count.

        """
        return len(self.active_players)
