from itertools import cycle, islice

from guesstheword.exceptions import MaxPlayersExceededError
from guesstheword.players import PlayerBase, PlayerManagerBase


class Player(PlayerBase):
    """
    Player example.

    """
    @property
    def status(self):
        """
        Get player's status.

        Returns:
            (str): Status.

        """
        return 'Active' if self.is_active else 'Inactive'

    def __str__(self):
        return self.name


class PlayerManager(PlayerManagerBase):
    """
    Player manager example.

    """
    def __init__(self, max_players=1):
        super().__init__(max_players)
        self._players = []
        self._current_idx = None

    @property
    def current_player(self):
        try:
            return self._players[self._current_idx]
        except (TypeError, IndexError):
            return None

    @property
    def active_players(self):
        return [p for p in self._players if p.is_active]

    def add_player(self, player):
        # Raise exception
        # if we try to add more players than allowed.
        if self.players_count == self._max_players:
            raise MaxPlayersExceededError(
                'Max players count exceeded: "{0}"'.format(self._max_players)
            )

        self._players.append(player)
        # If it is first player or first active,
        # mark it as current.
        if self.is_current_player_missed and player.is_active:
            self.set_current_player(player)

    def next_player(self):

        current_player_idx = self._current_idx or 0

        # Drop current player index if not active
        current_player = self.current_player
        if current_player is not None and not current_player.is_active:
            self.drop_current_player()

        # Get cycle iterator over other players
        # except current and starting from current idx
        other_players = islice(
            cycle(enumerate(self._players)),
            current_player_idx + 1,
            self.players_count + current_player_idx
        )

        # If new active player found,
        # set him as current
        for pos, player in other_players:
            if player.is_active:
                self._current_idx = pos
                break

        return self.current_player

    @property
    def players_count(self):
        """
        Count of all players.

        Returns:
            (int): Count.

        """
        return len(self._players)

    @property
    def is_current_player_missed(self):
        """
        Check if current player is not set.

        Returns:
            (bool): True if current player is not set. False otherwise.

        """
        return self._current_idx is None

    def set_current_player(self, player):
        """
        Set player as current.

        Args:
            player (instance): Player instance.

        Returns: None.

        """
        try:
            idx = self._players.index(player)
        except ValueError:
            return

        self._current_idx = idx

    def drop_current_player(self):
        """
        Drop current player index.

        Returns: None.

        """
        self._current_idx = None

    def __str__(self):
        return (
            'Player Manager. Total players: "{obj.players_count}". '
            'Active players: "{obj.active_players_count}".'
        ).format(obj=self)
