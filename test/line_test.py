import unittest

from src.point import Point
from src.line import Line, LineBuilder


class TestLine(unittest.TestCase):

    def get_line_list_from_points(self):
        return [
            LineBuilder.from_points(Point(1, 1), Point(2, 2)),
            LineBuilder.from_points(Point(0, 0), Point(2, 4))
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


if __name__ == '__main__':
    unittest.main()
