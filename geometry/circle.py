from math import sqrt, fabs
from functools import reduce
from enum import Enum

from geometry.point import Point
from geometry.segment import Segment
from geometry.line import LineBuilder
from geometry.multilib import symbolic_sign


class CircleOrientation(Enum):
    EQUAL = 'equal'
    INTERSECT = 'intersect'
    NOT_INTERSECT = 'not_intersect'


class Circle():

    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def substitute(self, point: Point):
        return (self.center.x - point.x)**2 + (
            self.center.y - point.y)**2 - self.radius**2

    # TODO: Update realization
    def get_tangents(self, point: Point):
        point_position = self.substitute(point)

        if point_position < 0:
            return None
        if point_position == 0:
            return LineBuilder.from_points(self.center, point).get_orthogonal()

        catheter = Segment(point, self.center).length()
        hypotenuse = sqrt(self.radius**2 + catheter**2)

        c = self.center.x - point.x
        d = self.center.y - point.y

        b = [
            hypotenuse * (c * self.radius - d) / (c**2 - d**2),
            hypotenuse * (-c * self.radius - d) / (c**2 - d**2)
        ]

        a = [hypotenuse**2 - d * b[0] / c, hypotenuse**2 - d * b[1] / c]

        tangent_points = [
            Point(point.x - a[0], point.y - b[0]),
            Point(point.x - a[1], point.y - b[1])
        ]

        return [
            LineBuilder.from_points(point, tangent_points[0]),
            LineBuilder.from_points(point, tangent_points[1])
        ]

    @staticmethod
    def get_intersect(c1, c2):
        length = Segment(c1.center, c2.center).length()
        points = []

        if length == 0 and c1.radius == c2.radius:
            return {"orientation": CircleOrientation.EQUAL, "points": points}

        if c1.radius + c2.radius < length:
            return {
                "orientation": CircleOrientation.NOT_INTERSECT,
                "points": points
            }

        if fabs(c1.radius - c2.radius) > length:
            return {
                "orientation": CircleOrientation.NOT_INTERSECT,
                "points": points
            }

        b = (c2.radius**2 - c1.radius**2 + length**2) / (2 * length)
        a = length - b
        h = sqrt(c1.radius**2 - a**2)

        p0 = Point(c1.center.x + a / length * (c2.center.x - c1.center.x),
                   c1.center.y + a / length * (c2.center.y - c1.center.y))

        points.append(
            Point(p0.x + h / length * (c2.center.y - c1.center.y),
                  p0.y - h / length * (c2.center.x - c1.center.x)))

        points.append(
            Point(p0.x - h / length * (c2.center.y - c1.center.y),
                  p0.y + h / length * (c2.center.x - c1.center.x)))

        return {"orientation": CircleOrientation.INTERSECT, "points": points}

    def __str__(self):
        signs = [symbolic_sign(-self.center.x), symbolic_sign(-self.center.y)]
        values = [fabs(self.center.x), fabs(self.center.y)]
        parts = [
            f"(x{signs[0]}{values[0]})^2",
            "\t+\t" + f"(y{signs[1]}{values[1]})^2" + f"\t=\t{self.radius}^2"
        ]
        return reduce(lambda output, x: output + x, parts)


class CircleBuilder():

    @staticmethod
    def from_points(a: Point, b: Point, c: Point):
        bx_by = b.x**2 + b.y**2
        ax_ay = a.x**2 + a.y**2
        cx_cy = c.x**2 + c.y**2
        cx_ax = 2 * c.x - 2 * a.x
        bx_ax = 2 * b.x - 2 * a.x
        by_ay = 2 * b.y - 2 * a.y
        cy_ay = 2 * c.y - 2 * a.y

        y = ((bx_by - ax_ay) * cx_ax - (cx_cy - ax_ay) * bx_ax) / (
            by_ay * cx_ax - cy_ay * bx_ax)
        x = (cx_cy - ax_ay - y * cy_ay) / cx_ax
        radius = (a.x - x)**2 + (a.y - y)**2
        return Circle(Point(x, y), radius)
