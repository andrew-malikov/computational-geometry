from math import sqrt

from geometry.circle import Circle
from geometry.line import Line
from geometry.point import Point


# TODO: Fix
def get_intersect_circle_and_line(c: Circle, l: Line):
    y_list = []

    const_part_1 = l.c**2 + 2 * c.center.x * l.c * l.a
    const_part_2 = (c.center.x**2 + c.center.y**2 - c.radius**2) * l.a**2
    const = const_part_1 + const_part_2

    y1_const = l.b**2 + l.a**2
    y2_const = 2 * l.b * l.c + 2 * c.center.x * l.b * l.a - (
        2 * c.center.y * l.a**2)

    for root in get_quadratic_equation_roots(y1_const, y2_const, const):
        y_list.append(root)

    points = []
    for y in y_list:
        const = (y - c.center.y)**2 + c.center.x**2 - c.radius**2
        for root in get_quadratic_equation_roots(1, c.center.x, const):
            points.append(Point(root, y))

    correct_points = []
    if len(points) > 0:
        correct_points.append(points[0])
        correct_points.append(points[len(points) - 1])

    return correct_points


def get_quadratic_equation_roots(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return []

    if discriminant == 0:
        return [-b / (2 * a)]

    return [
        -b + sqrt(discriminant) / (2 * a), -b - sqrt(discriminant) / (2 * a)
    ]
