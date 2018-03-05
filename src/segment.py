from src.point import Point


class Segment():

    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def _get_start_point(self):
        return [min(self.a[0], self.b[0]), min(self.a[1], self.b[1])]

    def _get_end_point(self):
        return [max(self.a[0], self.b[0]), max(self.a[1], self.b[1])]

    def contain_point(self, point: Point):
        left_part = (point.x - self.a.x) * (self.b.y - self.a.y)
        right_part = (self.b.x - self.a.x) * (point.y - self.a.y)

        if not left_part == right_part:
            return False

        if not min(self.a.x, self.b.x) <= point.x <= max(self.a.x, self.b.x):
            return False

        if not min(self.a.y, self.b.y) <= point.y <= max(self.a.y, self.b.y):
            return False

        return True
