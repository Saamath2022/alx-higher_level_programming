#!/usr/python3
import unittest
from your_module import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_integer_duplicate_elements(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_max_integer_float_elements(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_max_integer_string_elements(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]),
                         "cherry")

    def test_max_integer_mixed_elements(self):
        self.assertIsNone(max_integer([1, "apple", 3.3]))


if __name__ == '__main__':
    unittest.main()
