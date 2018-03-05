import unittest

from src.point import Point
from src.segment import Segment


class TestSegment(unittest.TestCase):

    def test_contain_point(self):
        segment = Segment(Point(1, 1), Point(4, 4))

        self.assertTrue(segment.contain_point(Point(2, 2)))
        self.assertTrue(segment.contain_point(Point(1, 1)))
        self.assertTrue(segment.contain_point(Point(4, 4)))

        self.assertFalse(segment.contain_point(Point(0, 0)))

        self.assertFalse(segment.contain_point(Point(-5, 88)))
        self.assertFalse(segment.contain_point(Point(-1, 0.5)))


if __name__ == '__main__':
    unittest.main()
