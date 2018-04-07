from enum import Enum
from math import fabs, acos, degrees

from geometry.line import LineBuilder
from geometry.segment import Segment


class PointOrientation(Enum):
    INNER = 'inner'
    OUTER = 'outer'
    ON_POLYGON = 'on_polygon'


class TriangelType(Enum):
    RIGHT = 'right'
    OBTUSE = 'obtuse'
    ACUTE = 'acute'


class Triangel():

    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]
        self.sides = [
            Segment(p1, p2).length(),
            Segment(p2, p3).length(),
            Segment(p3, p1).length()
        ]

    @staticmethod
    def is_triangel(a, b, c):
        a = fabs(a)
        b = fabs(b)
        c = fabs(c)
        return a + b > c and a + c > b and c + b > a

    def get_point_orientation(self, point):
        lines = self.get_lines()

        for i in range(0, len(lines)):
            if not lines[i].is_points_in_plane([self.get_point(i + 2), point]):
                return PointOrientation.OUTER

        for line in lines:
            if line.contain_point(point):
                return PointOrientation.ON_POLYGON

        return PointOrientation.INNER

    def get_lines(self):
        lines = []
        for i in range(0, len(self.points)):
            line = LineBuilder.from_points(
                self.points[i], self.points[(i + 1) % len(self.points)])
            lines.append(line)
        return lines

    def get_point(self, offset):
        return self.points[offset % len(self.points)]

    def get_type(self):

        s = self.sides

        angles = [
            degrees(acos((s[1]**2 + s[2]**2 - s[0]**2) / (2 * s[1] * s[2]))),
            degrees(acos((s[0]**2 + s[2]**2 - s[1]**2) / (2 * s[0] * s[2]))),
            degrees(acos((s[0]**2 + s[1]**2 - s[2]**2) / (2 * s[0] * s[1])))
        ]

        angles = list(map(lambda x: round(x, 2), angles))

        for angle in angles:
            if angle == 90:
                return TriangelType.RIGHT

        for angle in angles:
            if angle > 90:
                return TriangelType.OBTUSE

        return TriangelType.ACUTE
