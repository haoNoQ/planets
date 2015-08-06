
from random import random

from src.Planet import Planet


class Map(object):
    def __init__(self, setup):
        super(Map, self).__init__()
        self._setup = setup
        while True:
            self._planets = [Planet() for i in range(setup.num_planets)]
            self._bases = [
                Base(self._planets[random(setup.num_planets)], i)
                     for i in range(setup.num_players)]

    def gameSetup(self):
        return self._setup

    def base(self, player):
        return self._bases[player]

    def passThrough(self, player, point):
        return False

    def gravity(self, x=None, y=None):
        return reduce(lambda u, v: u + v,
                      [p.getGravity(Point(x, y)) for p in self._planets])
