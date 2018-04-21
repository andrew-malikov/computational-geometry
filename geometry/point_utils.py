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

    return [point, min_length]
