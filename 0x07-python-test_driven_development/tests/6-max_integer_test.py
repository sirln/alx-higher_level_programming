#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_list_with_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_list_with_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.9]), 3.2)

    def test_list_with_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 8, 20]), 20)

    def test_list_with_max_at_the_start(self):
        self.assertEqual(max_integer([32, 2, 13, 8, 20]), 32)

    def test_list_with_max_in_the_middle(self):
        self.assertEqual(max_integer([45, 22, 93, 18, 20]), 93)


if __name__ == '__main__':
    unittest.main()
