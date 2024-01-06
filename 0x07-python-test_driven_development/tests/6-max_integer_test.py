#!/usr/bin/python3
"""Unittest for max_integer module
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_empty_list(self):
        """Tests for an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_one_element(self):
        """Tests for case where list has one element."""
        result = max_integer([10])
        self.assertEqual(result, 10)

    def test_max_integer_positive_numbers(self):
        """Tests for positive numbers passed to list."""
        result = max_integer([1, 5, 7, 10, 2])
        self.assertEqual(result, 10)

    def test_max_integer_negative_numbers(self):
        """Tests for negative numbers passed to list."""
        result = max_integer([-2, -10, -5, -7])
        self.assertEqual(result, -2)

    def test_max_integer_duplicate_numbers(self):
        """Tests for duplicate numbers in the list."""
        result = max_integer([3, 11, 10, 11, 3])
        self.assertEqual(result, 11)

    def test_max_integer_mixed_numbers(self):
        """Tests for mixed numbers in the list."""
        result = max_integer([-1, 3, -5, 5, 2])
        self.assertEqual(result, 5)

    def test_max_integer_float_numbers(self):
        """Tests for cases where floats are in list."""
        result = max_integer([2.5, 7.0, 1.8, 4.9])
        self.assertEqual(result, 7.0)

    def test_max_integer_with_strings(self):
        """Test for cases where strings are passed to list."""
        result = max_integer(['test', 'case', 'with', 'strings'])
        self.assertRaises(TypeError)
