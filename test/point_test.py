import unittest

from geometry.point import Point


class TestPoint(unittest.TestCase):

    def get_points(self):
        return [
            Point(0, 0),
            Point(1, 1),
            Point(0, 1),
            Point(-1, 1),
            Point(-1, 0),
            Point(-1, -1),
            Point(1, -1)
        ]

    def test_get_arc(self):
        points = self.get_points()

        self.assertEqual(points[0].get_arc(), 0)
        self.assertEqual(points[1].get_arc(), 45)
        self.assertEqual(points[2].get_arc(), 90)
        self.assertEqual(points[3].get_arc(), 135)
        self.assertEqual(points[4].get_arc(), 180)
        self.assertEqual(points[5].get_arc(), 225)
        self.assertEqual(points[6].get_arc(), 315)


if __name__ == '__main__':
    unittest.main()
