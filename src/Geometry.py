
from math import sqrt
from src.Overrides import overrides


class Point(object):
    def __init__(self, x=None, y=None):
        super(Point, self).__init__()
        if x is None:
            self._x = 0.0
            self._y = 0.0
        elif isinstance(x, Point):
            p = x
            self._x = p.x
            self._y = p.y
        else:
            self._x = x
            self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance(self, x=None, y=None):
        if x is None:
            return self.distance(0.0, 0.0)
        if y is None:
            p = x
            return self.distance(p.x(), p.y())
        return sqrt((self._x - x) * (self._x - x) +
                    (self._y - y) * (self._y - y))

    def __add__(self, v):
        assert isinstance(v, Vector)
        return Point(self._x + v._x, self._y + v._y)

    def __sub__(self, p):
        assert isinstance(p, Point)
        return Vector(self._x - p._x, self._y - p._y)


class Vector(Point):
    def __init__(self, x, y):
        if isinstance(y, Point) and isinstance(x, Point):
            super(Vector, self).__init__(Vector(y) - Vector(x))
        else:
            super(Vector, self).__init__(x, y)

    def length(self):
        return self.distance()

    def __add__(self, v):
        assert(isinstance(v, Vector))
        return Vector(self._x + v._x, self._y + v._y)

    def __sub__(self, v):
        assert(isinstance(v, Vector))
        return Vector(self._x - v._x, self._y - v._y)

    def __neg__(self):
        return Vector(-self._x, -self._y)

    def __mul__(self, a):
        if isinstance(a, Vector):
            return self._x * a._x + self._y * a._y
        else:
            return Vector(self._x * a, self._y * a)

    def __div__(self, a):
        return Vector(self._x / a, self._y / a)


class Circle(Point):
    def __init__(self, r, x, y=None):
        super(Circle, self).__init__(x, y)
        self._r = r

    def radius(self):
        return self._r

    def contains(self, x=None, y=None):
        return self.distance(x, y) < self._r

    def overlaps(self, c):
        return self.distance(c) < self._r + c.radius()


class Line(object):
    def __init__(self, p1, p2, p3=None, p4=None):
        super(Line, self).__init__()
        if isinstance(p1, Point):
            self._p1 = p1
            if isinstance(p2, Point):
                self._p2 = p2
            else:
                self._p2 = Point(p2, p3)
        else:
            self._p1 = Point(p1, p2)
            if isinstance(p3, Point):
                self._p2 = p3
            else:
                self._p2 = Point(p3, p4)
        self._x1 = self._p1.x()
        self._y1 = self._p1.y()
        self._x2 = self._p2.x()
        self._y2 = self._p2.y()
        self._a = self._y1 - self._y2
        self._b = self._x1 - self._y2
        self._c = self._x1 * self._y2 - self._x2 * self._y1
        n = sqrt(self._a * self._a + self._b * self._b)
        self._a /= n
        self._b /= n
        self._c /= n

    def direction(self):
        return Vector(self._x2 - self._x1, self._y2 - self._y1)

    def distance(self, x=None, y=None):
        pp = Point(x, y)
        return self._a * pp._x + self._b * pp._y + self._c

    def intersects_circle(self, c):
        return self.distance(c) < c.radius()


class Segment(Line):
    def __init__(self, p1, p2, p3=None, p4=None):
        super(Segment, self).__init__(p1, p2, p3, p4)

    def _projects_inside(self, x=None, y=None):
        pp = Point(x, y)
        v1 = self.direction()
        v2 = Vector(self._p1, pp)
        v3 = Vector(pp, self._p2)
        return (v1 * v2 >= 0) and (v1 * v3 >= 0)

    @overrides
    def distance(self, x=None, y=None):
        if self._projects_inside(x, y):
            return super(Segment, self).distance(x, y)
        return min(self._p1.distance(x, y), self._p2.distance(x, y))
