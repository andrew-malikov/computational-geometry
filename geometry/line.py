from geometry.point import Point
from geometry.multilib import sign, symbolic_sign
from math import sqrt, fabs


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

    def get_orthogonal(self):
        return Line(self.b, self.a, self.c)

    def __str__(self):
        signs = [
            symbolic_sign(self.a),
            symbolic_sign(self.b),
            symbolic_sign(self.c)
        ]
        values = [fabs(self.a), fabs(self.b), fabs(self.c)]
        return f"{signs[0]}{values[0]}x {signs[1]}{values[1]}y {signs[2]}{values[2]} = 0"


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

    @staticmethod
    def orthogonal(line: Line, point: Point):
        '''
        return new Line orthogonal line and intersecting the point
        '''
        c = line.b * point.x + line.a * (-point.y)
        return Line(-line.b, line.a, c)

    @staticmethod
    def parallel(line: Line, distance):
        if line.a:
            point = Point(-line.c / line.a, 0)
        else:
            point = Point(0, -line.c / line.b)
        c = -line.a * point.x - line.b * point.y + distance * sqrt(
            line.a**2 + line.b**2)
        return Line(line.a, line.b, c)

    @staticmethod
    def bisector(a, b):
        a_length = a.length()
        b_length = b.length()
        return LineBuilder.from_points(
            b.a,
            Point(a.b.x / a_length + b.b.x / b_length,
                  a.b.y / a_length + b.b.y / b_length))


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
