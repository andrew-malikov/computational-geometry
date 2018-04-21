from math import sqrt

from geometry.circle import Circle
from geometry.line import Line
from geometry.point import Point


# TODO: Fix
def get_intersect_circle_and_line(c: Circle, l: Line):
    x_list = []
    y_list = []

    const_part_1 = l.c**2 + l.a * c.center.x * l.c + l.a**2 * c.center.x**2
    const_part_2 = c.center.y**2 * l.a**2 - c.radius**2 * l.a**2
    const = const_part_1 + const_part_2

    y1_const = l.b + l.a**2
    y2_const = 2 * l.b * l.c + l.a * c.center.x * l.b - 2 * c.center.y * l.a**2

    discriminant = y2_const**2 - 4 * const * y1_const

    if discriminant < 0:
        return []

    if discriminant == 0:
        y_list.append((y2_const + sqrt(discriminant)) / 2 * y1_const)

    if discriminant > 0:
        y_list.append((y2_const + sqrt(discriminant)) / 2 * y1_const)
        y_list.append((y2_const - sqrt(discriminant)) / 2 * y1_const)

    for y in y_list:
        x_list.append((-l.b * y - l.c) / l.a)

    points = []
    for i in range(0, len(x_list)):
        points.append(Point(x_list[i], y_list[i]))

    return points
