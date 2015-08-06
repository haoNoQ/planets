
from math import sin, cos
from threading import Thread

from src.Geometry import Point, Vector, Segment
from src.Constants import PlayerColors


class Trajectory(object):
    def __init__(self, m, p, a, v):
        super(Trajectory, self).__init__()
        self._player = p
        self._color = PlayerColors[p]
        self._map = m
        b = m.base(p)
        self._pos = Point(b)
        self._vel = Vector(v * cos(a), v * sin(a))
        self._segments = []
        self._last_draw_idx = 0

        self._thread = Trajectory._WorkerThread(self)
        self._thread.start()

    def _advance(self):
        old_pos = self._pos
        self._vel += self._map.gravity(self._pos)
        self._pos += self._vel
        self._segments.append(Segment(old_pos, self._pos))
        return self._map.passThrough(self._player, self._pos)

    class _WorkerThread(Thread):
        def __init__(self, t):
            super(Trajectory.WorkerThread, self).__init__(daemon=True)
            self._t = t

        def run(self):
            while True:
                if self._t._advance():
                    return
