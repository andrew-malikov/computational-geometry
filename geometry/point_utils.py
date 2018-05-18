from math import inf

from geometry.segment import Segment


def get_optimal_point(points):
    """
    Returns the point the sum of the distances
    from which to other points is minimal
    """
    min_length = inf
    point = None

    for i in range(0, len(points)):
        length = 0

        for j in range(0, len(points)):
            if i == j:
                continue

            length += Segment(points[i], points[j]).length()

        if min_length > length:
            min_length = length
            point = points[i]

    return point


def get_far_point(points):
    far_point = None
    far_distance = 0

    for point in points:
        distance = point.get_distance()

        if distance >= far_distance:
            far_point = point
            far_distance = distance

    return far_point


def get_left_up_far_point(points):
    far_point = None
    far_index = -inf

    for point in points:
        index = -point.x + point.y

        if index >= far_index:
            far_point = point
            far_index = index

    return far_point
