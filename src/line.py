from src.point import Point


class Line():

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def new_from_points(p1: Point, p2: Point):
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = -b * p1.y - a * p1.x
        return Line(a, b, c)

    @staticmethod
    def new_from_function(k: int, m: int):
        a = k
        b = -1
        c = m
        return Line(a, b, c)

    @staticmethod
    def is_parallel(l1, l2):
        return l1.a * l2.b == l2.a * l1.b
