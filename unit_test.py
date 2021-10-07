import unittest

from Math_game import define_difficulty, calculate_answer, define_operation


class Math_gameTest(unittest.TestCase):

    def test_define_difficulty(self):
        self.assertEqual(
            define_difficulty('1'),
            10
        )
        self.assertEqual(
            define_difficulty('2'),
            100
        )
        self.assertEqual(
            define_difficulty('3'),
            1000
        )
        self.assertEqual(
            define_difficulty('4'),
            10000
        )

    def test_calculate_answer(self):
        self.assertEqual(
            calculate_answer([3, 5], '+'),
            8
        )
        self.assertEqual(
            calculate_answer([3, 5], '-'),
            -2
        )
        self.assertEqual(
            calculate_answer([3, 5], '*'),
            15
        )

    def test_define_operation(self):
        self.assertEqual(
            define_operation(1),
            '+'
        )
        self.assertEqual(
            define_operation(2),
            '-'
        )
        self.assertEqual(
            define_operation(3),
            '*'
        )


if __name__ == '__main__':
    unittest.main()
