from math import degrees, atan2


class Point():
    """
    TODO: Update components count
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_arc(self):
        arc = degrees(atan2(self.y, self.x))
        if arc < 0:
            return 360 + arc
        return arc

    def is_equal(self, point):
        return self.x == point.x and self.y == point.y

    def __str__(self):
        return f"({self.x},{self.y})"

    @staticmethod
    def compare_arc(a, b):
        return a.get_arc() - b.get_arc()
