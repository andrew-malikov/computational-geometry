import unittest

from geometry.point import Point
from geometry.line import Line, LineBuilder


class TestLine(unittest.TestCase):

    def get_line_list_from_points(self):
        return [
            LineBuilder.from_points(Point(1, 1), Point(2, 2)),
            LineBuilder.from_points(Point(0, 0), Point(2, 4)),
            LineBuilder.from_points(Point(-1, 1), Point(0, 0)),
            LineBuilder.from_points(Point(1, 0), Point(0, 1))
        ]

    def get_line_list_from_functions(self):
        return [
            LineBuilder.from_function(1, 0),
            LineBuilder.from_function(2, 0)
        ]

    def test_is_parallel(self):
        line_list_from_points = self.get_line_list_from_points()
        line_list_from_functions = self.get_line_list_from_functions()

        self.assertTrue(
            Line.is_parallel(line_list_from_points[0],
                             line_list_from_functions[0]))

        self.assertTrue(
            Line.is_parallel(line_list_from_points[1],
                             line_list_from_functions[1]))

        self.assertFalse(
            Line.is_parallel(line_list_from_points[0],
                             line_list_from_functions[1]))

        self.assertFalse(
            Line.is_parallel(line_list_from_points[1],
                             line_list_from_functions[0]))

    def test_is_intersect(self):
        lines = self.get_line_list_from_points()

        self.assertTrue(Line.get_intersect(lines[0], lines[1]))
        self.assertTrue(Line.get_intersect(lines[2], lines[1]))
        self.assertFalse(Line.get_intersect(lines[2], lines[3]))


if __name__ == '__main__':
    unittest.main()
