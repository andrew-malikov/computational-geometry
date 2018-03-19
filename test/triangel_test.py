import unittest

from src.point import Point
from src.triangel import Triangel, PointOrientation


class TestTriangel(unittest.TestCase):

    def get_points(self):
        return [
            Point(0, 0),
            Point(-1, -1),
            Point(-1, 1),
            Point(1, -1),
            Point(1, 1),
            Point(0, 2),
            Point(3, -2),
            Point(15, -1),
            Point(0, 5),
            Point(-4, 1),
            Point(-8, -3),
            Point(7, -8),
            Point(8, 8)
        ]

    def get_triangels(self):
        points = self.get_points()
        return [Triangel(points[1], points[5], points[6])]

    def test_get_point_orientation(self):
        triangels = self.get_triangels()
        points = self.get_points()

        self.assertEqual(triangels[0].get_point_orientation(points[0]),
                         PointOrientation.INNER)

        self.assertEqual(triangels[0].get_point_orientation(points[1]),
                         PointOrientation.ON_POLYGON)

        self.assertEqual(triangels[0].get_point_orientation(points[7]),
                         PointOrientation.OUTER)


if __name__ == '__main__':
    unittest.main()
