#!/usr/bin/python3
"""Defines square class tests
"""
from models.square import Square
import unittest


class TestSquareClass(unittest.TestCase):
    """Test the square class"""

    s0 = Square(5)
    s1 = Square(2, 2)
    s2 = Square(3, 1, 3)

    def tearDown(self) -> None:
        """Cleanup the values by resetting to default"""
        self.s0.update(size=5)
        self.s1.update(size=2, id=2)
        self.s2.update(size=3, x=1, y=3)

    def test_set_size(self):
        """Test setting size values"""
        self.s0.size = 10
        self.assertEqual(self.s0.size, 10)

        # check similarity between size, height and width
        self.assertEqual(self.s0.size, self.s0.width)
        self.assertEqual(self.s0.size, self.s0.height)

    def test_size(self):
        """Test the size attr"""
        self.assertEqual(self.s0.size, 5)

        self.assertEqual(self.s0.size, self.s0.width)
        self.assertEqual(self.s0.size, self.s0.height)

    def test_invalid_type_size(self):
        """Test invalid type of size attr. Exception must be aligned with
        width
        """
        with self.assertRaises(TypeError) as te:
            self.s0.size = 'Five'

        self.assertEqual(
            te.exception.__str__(), 'width must be an integer'
            )
        
    def test_invalid_value_size(self):
        """Test value error for size attr. Execption must align with width"""
        with self.assertRaises(ValueError) as ve:
            self.s0.size = -5

        self.assertEqual(
            ve.exception.__str__(), 'width must be > 0'
        )
