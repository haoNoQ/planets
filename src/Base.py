
from random import uniform
from math import sin, cos, pi

from src.Geometry import ColoredCircle
from src.Constants import PlayerColors


class Base(ColoredCircle):
    def __init__(self, planet, player):
        a = uniform(0, 2 * pi)
        x = planet.x() + planet.radius() * cos(a)
        y = planet.y() + planet.radius() * sin(a)
        super(Base, self).__init__(x, y, 0.01, PlayerColors[player])
