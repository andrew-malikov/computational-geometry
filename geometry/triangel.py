from enum import Enum

from geometry.line import LineBuilder


class PointOrientation(Enum):
    INNER = 'inner'
    OUTER = 'outer'
    ON_POLYGON = 'on_polygon'


class Triangel():

    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def get_point_orientation(self, point):
        lines = self.get_lines()

        for i in range(0, len(lines)):
            if not lines[i].is_points_in_plane([self.get_point(i + 2), point]):
                return PointOrientation.OUTER

        for line in lines:
            if line.contain_point(point):
                return PointOrientation.ON_POLYGON

        return PointOrientation.INNER

    def get_lines(self):
        lines = []
        for i in range(0, len(self.points)):
            line = LineBuilder.from_points(
                self.points[i], self.points[(i + 1) % len(self.points)])
            lines.append(line)
        return lines

    def get_point(self, offset):
        return self.points[offset % len(self.points)]
