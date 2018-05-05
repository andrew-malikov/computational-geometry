from geometry.vector import Vector2Builder
from geometry.segment import Segment
from geometry.line import LineBuilder
from geometry.multilib import sign

from math import fabs


class Polygon():

    def __init__(self, points):
        self.points = points

    def get_segments(self):
        segments = []
        points = self.points

        length = len(points)
        for i in range(0, length):
            j = (i + 1) % length
            segments.append(Segment(points[i], points[j]))

        return segments

    def is_simple(self):
        segments = self.get_segments()

        length = len(segments)
        for i in range(0, length):
            for j in range(i + 2, i + length - 1):

                if Segment.is_intersects(segments[i], segments[j % length]):
                    return False

        return True

    def get_area(self):
        if not self.is_simple():
            return None

        area = 0
        points = self.points
        length = len(points)
        for i in range(0, length):
            j = (i + 1) % length

            area += points[i].x * points[j].y - points[i].y * points[j].x

        return fabs(area) / 2

    def is_convex(self):
        segments = self.get_segments()
        skew_sign = None

        length = len(segments)
        for i in range(0, length):

            v_1 = Vector2Builder.from_segment(segments[i])
            v_2 = Vector2Builder.from_segment(segments[(i + 1) % length])

            current_sign = sign(v_1.skew_product(v_2))

            if current_sign == 0:
                continue
            elif skew_sign is None:
                skew_sign = current_sign
            elif skew_sign != current_sign:
                return False

        return True
