import unittest

from src.multilib import sign


class TestMultilib(unittest.TestCase):

    def test_sign(self):
        self.assertEqual(sign(-2), -1)
        self.assertEqual(sign(43), 1)
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(-0), 0)
        self.assertEqual(sign(0.0000001), 1)
        self.assertEqual(sign(-0.00000001), -1)


if __name__ == '__main__':
    unittest.main()
