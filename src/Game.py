
from src.Map import Map


class Game(object):
    def __init__(self, setup):
        super(Game, self).__init__()
        self._setup = setup
        self._history = [[]] * self._setup.num_players
        self._map = Map(self._setup)
