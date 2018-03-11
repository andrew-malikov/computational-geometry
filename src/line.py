from src.point import Point
from src.multilib import sign


class Line():

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def substitute(self, point):
        return self.a * point.x + self.b * point.y + self.c

    def contain_point(self, point: Point):
        return self.substitute(point) == 0

    def is_points_in_plane(self, points: list):
        if len(points) == 1:
            return True

        point_index = 0
        original_plane = 0

        for i in range(point_index, len(points)):
            plane = sign(self.substitute(points[i]))
            if plane != 0:
                original_plane = plane
                point_index = i + 1
                break

        if point_index >= len(points):
            return True

        for i in range(point_index, len(points)):
            plane = sign(self.substitute(points[i]))
            if plane != original_plane and plane != 0:
                return False
        return True

    @staticmethod
    def is_parallel(l1, l2):
        return l1.a * l2.b == l2.a * l1.b

    @staticmethod
    def get_intersect(l1, l2):
        """
        If the lines intersect, return point, otherwise false
        """
        if Line.is_parallel(l1, l2):
            return False

        if l1.a:
            y = (l2.a * l1.c - l1.a * l2.c) / (l1.a * l2.b - l2.a * l1.b)
            x = (-l1.b * y - l1.c) / l1.a
        elif l2.a:
            y = (l2.c * l1.a - l1.c * l2.a) / (l1.b * l2.a - l2.b * l1.a)
            x = (-l2.c - l2.b * y) / l2.a

        return Point(x, y)

    def __str__(self):
        return "{0}x + {1}y + {2} = 0".format(self.a, self.b, self.c)


class LineBuilder():

    @staticmethod
    def from_points(p1: Point, p2: Point):
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = -b * p1.y - a * p1.x
        return Line(a, b, c)

    @staticmethod
    def from_function(k: int, m: int):
        a = k
        b = -1
        c = m
        return Line(a, b, c)

    @staticmethod
    def from_segment(segment):
        return LineBuilder.from_points(segment.a, segment.b)


class LineUtils(Line):

    def __init__(self, a, b, c):
        super(a, b, c)

    @staticmethod
    def is_intersect_with_segment(line, segment):
        line_from_segment = LineBuilder.from_segment(segment)

        intersect = Line.get_intersect(line, line_from_segment)

        if segment.contain_point(intersect):
            return True

        return False
