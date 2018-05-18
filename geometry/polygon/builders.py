from math import inf
from operator import methodcaller

from geometry.polygon.base import Polygon
from geometry.vector import Vector2Builder


def graham_algorithm(points: list):
    if len(points) < 3:
        raise NotImplementedError()

    down_point = get_down_point(points)
    offset = [down_point.x, down_point.y]

    for point in points:
        point.add_offset(-offset[0], -offset[1])

    sorted_points = sorted(points, key=methodcaller('get_arc'))

    polygon_points = [sorted_points[0], sorted_points[1]]
    length = len(sorted_points)
    for i in range(2, length):
        vector_points = [
            sorted_points[(i - 1) % length], sorted_points[i],
            sorted_points[(i + 1) % length]
        ]

        if get_angle(vector_points) >= 0:
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
