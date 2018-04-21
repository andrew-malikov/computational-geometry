from geometry.segment import Segment

from math import fabs


class Polygon():

    def __init__(self, points):
        self.points = points

    def is_simple(self):

        length = len(self.points)

        for i in range(0, length):
            j = (i + 2) % length

            segment_1 = Segment(self.points[i], self.points[(i + 1) % length])
            segment_2 = Segment(self.points[j], self.points[(j + 1) % length])

            if Segment.is_intersects(segment_1, segment_2):
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
        pass
