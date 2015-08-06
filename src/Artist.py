
from enum import Enum
from collections import namedtuple


class Figure(object):

    Shape = Enum('Shape', 'Segment Circle')
    Item = namedtuple('Item', 'Object Shape')

    def __init__(self, color):
        super(Figure, self).__init__()
        self._color = color

    def addSegment(self, s):
        self._shapes.append(Figure.Item(s, Figure.Shape.Segment))

    def addCircle(self, c):
        self._shapes.append(Figure.Item(s, Figure.Shape.Circle))


class Artist(object):
    def __init__(self):
        super(Artist, self).__init__()

    def makeObject(self):
        pass

    def addSegment(self, o, s):
        pass

    def addCircle(self, o, c):
        pass
