from math import sqrt

from geometry.point import Point
from geometry.segment import Segment
from geometry.line import LineBuilder


class Circle():

    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def substitute(self, point: Point):
        return (self.center.x - point.x)**2 + (
            self.center.y - point.y)**2 - self.radius**2

    def get_tangent(self, point: Point):
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

    def __str__(self):
        return "(x-{0})^2 + (y-{1})^2 = {2}^2".format(
            self.center.x, self.center.y, self.radius)


class CircleBuilder():

    # TODO: Optimize solution
    @staticmethod
    def from_points(a: Point, b: Point, c: Point):
        y = ((b.x**2 + b.y**2 - a.x**2 - a.y**2) * (2 * c.x - 2 * a.x) -
             (c.x**2 + c.y**2 - a.x**2 - a.y**2) *
             (2 * b.x - 2 * a.x)) / ((2 * b.y - 2 * a.y) *
                                     (2 * c.x - 2 * a.x) -
                                     (2 * c.y - 2 * a.y) * (2 * b.x - 2 * a.x))
        x = (c.x**2 + c.y**2 - a.x**2 - a.y**2 - y *
             (2 * c.y - 2 * a.y)) / (2 * c.x - 2 * a.x)
        radius = (a.x - x) * (a.x - x) + (a.y - y) * (a.y - y)
        return Circle(Point(x, y), radius)
