from math import sqrt

from geometry.segment import Segment


class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def skew_product(self, vector):
        return self.x * vector.y - self.y * vector.x

    def scalar_product(self, vector):
        return self.x * vector.x + self.y * vector.y


class Vector2Builder():

    @staticmethod
    def from_points(p_1, p_2):
        return Vector2(p_2.x - p_1.x, p_2.y - p_1.y)

    @staticmethod
    def from_segment(segment: Segment):
        return Vector2Builder.from_points(segment.a, segment.b)


class Vector2Utils():

    @staticmethod
    def get_cos(v_1: Vector2, v_2: Vector2):
        return v_1.scalar_product(v_2) / (v_1.length() * v_2.length())

    @staticmethod
    def get_sin(v_1: Vector2, v_2: Vector2):
        return sqrt(1 - Vector2Utils.get_cos(v_1, v_2)**2)
