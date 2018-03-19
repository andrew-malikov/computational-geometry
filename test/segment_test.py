import unittest

from src.point import Point
from src.segment import Segment


class TestSegment(unittest.TestCase):

    def get_segments(self):
        return [
            Segment(Point(5, 5), Point(1, 1)),
            Segment(Point(1, 1), Point(1, 6)),
            Segment(Point(0, -1), Point(7, -1)),
            Segment(Point(-2, 6), Point(-2, -4)),
            Segment(Point(-4, 4), Point(4, -4)),
            Segment(Point(-8, -1), Point(5, 1)),
            Segment(Point(1, 2), Point(6, 0)),
            Segment(Point(-5, 0), Point(5, 0)),
            Segment(Point(0, 5), Point(0, -5)),
            Segment(Point(-5, 5), Point(-1, 1))
        ]

    def test_contain_point(self):
        segment = Segment(Point(1, 1), Point(4, 4))

        self.assertTrue(segment.contain_point(Point(2, 2)))
        self.assertTrue(segment.contain_point(Point(1, 1)))
        self.assertTrue(segment.contain_point(Point(4, 4)))

        self.assertFalse(segment.contain_point(Point(0, 0)))

        self.assertFalse(segment.contain_point(Point(-5, 88)))
        self.assertFalse(segment.contain_point(Point(-1, 0.5)))

    def test_is_intersect(self):
        segments = self.get_segments()

        self.assertTrue(Segment.is_intersects(segments[0], segments[1]))
        self.assertFalse(Segment.is_intersects(segments[0], segments[2]))
        self.assertTrue(Segment.is_intersects(segments[5], segments[3]))
        self.assertFalse(Segment.is_intersects(segments[4], segments[6]))


if __name__ == '__main__':
    unittest.main()
