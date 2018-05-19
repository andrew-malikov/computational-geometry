from math import inf

from geometry.polygon.base import Polygon
from geometry.vector import Vector2Builder


def graham_algorithm(points: list):
    if len(points) < 3:
        raise NotImplementedError()

    down_point = get_down_point(points)
    offset = [down_point.x, down_point.y]

    for point in points:
        point.add_offset(-offset[0], -offset[1])

    bubble(points)
    sorted_points = points

    polygon_points = [sorted_points[0], sorted_points[1]]
    length = len(sorted_points)
    for i in range(2, length):
        point = sorted_points[i]

        while get_angle([polygon_points[-2], polygon_points[-1], point]) < 0:
            polygon_points.pop()

        polygon_points.append(sorted_points[i])

    for point in polygon_points:
        point.add_offset(offset[0], offset[1])

    return Polygon(polygon_points)


def get_down_point(points: list):
    down_point = None
    down_distance = inf

    for point in points:

        if point.y <= down_distance:
            down_point = point
            down_distance = point.y

    return down_point


def get_angle(points: list):
    v1 = Vector2Builder().from_points(points[0], points[1])
    v2 = Vector2Builder().from_points(points[1], points[2])
    return v1.skew_product(v2)


def bubble(points: list):
    length = len(points)
    for i in range(0, length):
        swapped = False
        for i in range(0, length - i - 1):
            if points[i].get_arc() > points[i + 1].get_arc():
                hold = points[i + 1]
                points[i + 1] = points[i]
                points[i] = hold
                swapped = True
            elif points[i].get_arc() == points[i + 1].get_arc():
                if points[i].get_distance() > points[i + 1].get_distance():
                    hold = points[i + 1]
                    points[i + 1] = points[i]
                    points[i] = hold
                    swapped = True
        if not swapped:
            break

    return points
