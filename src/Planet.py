
from random import uniform

from src.Geometry import ColoredCircle


class Planet(ColoredCircle):
    def __init__(self):
        x = uniform(-0.5, 0.5)
        y = uniform(-0.5, 0.5)
        r = uniform(0.02, 0.1)
        c = (uniform(0.3, 0.7), uniform(0.3, 0.7), uniform(0.3, 0.7))
        super(Planet, self).__init__(x, y, r, c)
        self._m = uniform(0.1, 1.0)

    def mass(self):
        return self._m

    def gravity(self, x=None, y=None):
        r = self.distance(x, y)
        return self._m / (r * r)
