from math import sqrt

from geometry.point import Point
from geometry.polar_point.base import PolarPoint


def from_point(point: Point):
    radius = sqrt(point.x**2 + point.y**2)
    angle = point.get_arc()
    return PolarPoint(radius, angle)
