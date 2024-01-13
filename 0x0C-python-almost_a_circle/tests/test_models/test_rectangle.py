#!/usr/bin/python3
"""Defines Rectangle class unittests
"""
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    r0 = Rectangle(10, 2)
    r1 = Rectangle(2, 10)
    r2 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self) -> None:
        """Reset the values using the cleanup of tearDown."""
        self.r0.update(id=1, width=10, height=2, x=0, y=0)
        self.r1.update(id=2, width=2, height=10, x=0, y=0)
        self.r2.update(id=12, width=10, height=2, x=0, y=0)

    def test_constructor_with_args(self):
        """Test the constructor with width, height, x, y args"""
        # testing width parameter
        self.assertEqual(self.r0.width, 10)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 10)

        # testing height parameter
        self.assertEqual(self.r0.height, 2)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 2)

        # testing id parameter
        self.assertEqual(self.r0.id, 1)
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r2.id, 12)

    def test_update_width_parameter(self):
        """Test the value change for width."""
        # updating the width parameter
        self.r0.width = 15
        self.r1.width = 5
        self.r2.width = 15
        self.assertEqual(self.r0.width, 15)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 15)

    def test_update_height_parameter(self):
        """Test the value change for height."""
        # updating the height parameter
        self.r0.height = 5
        self.r1.height = 15
        self.r2.height = 5
        self.assertEqual(self.r0.height, 5)
        self.assertEqual(self.r1.height, 15)
        self.assertEqual(self.r2.height, 5)

    def test_update_x_parameter(self):
        """Test the value change for x."""
        # updating the x parameter
        self.r0.x = 2
        self.r1.x = 4
        self.r2.x = 6
        self.assertEqual(self.r0.x, 2)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r2.x, 6)

    def test_update_y_parameter(self):
        """Test the value change for y."""
        # updating the y parameter
        self.r0.y = 2
        self.r1.y = 4
        self.r2.y = 6
        self.assertEqual(self.r0.y, 2)
        self.assertEqual(self.r1.y, 4)
        self.assertEqual(self.r2.y, 6)

    def test_id(self):
        """Test the id value."""
        self.r2.id = 15
        self.assertEqual(self.r2.id, 15)

    def test_invalid_type_width(self):
        """Tests the type of the width param and raises an execption."""
        with self.assertRaises(TypeError) as te:
            self.r0.width = True
            self.r1.width = 'Ten'
            self.r2.width = 10.0

        # compare exception raised to string given
        self.assertEqual(
            te.exception.__str__(), 'width must be an integer'
        )

    def test_negative_or_zero_value_width(self):
        """Tests for negative value for width param."""
        with self.assertRaises(ValueError) as ve:
            self.r0.width = 0
            self.r1.width = -5
            self.r2.width = -10

        # compare exception raised to string given
        self.assertEqual(
            ve.exception.__str__(), 'width must be > 0'
        )

    def test_invalid_type_height(self):
        """Tests the type of the height param and raises an execption."""
        with self.assertRaises(TypeError) as te:
            self.r0.height = True
            self.r1.height = 'Two'
            self.r2.height = 2.0

        # compare exception raised to string given
        self.assertEqual(
            te.exception.__str__(), 'height must be an integer'
        )

    def test_negative_or_zero_value_height(self):
        """Tests for negative value for height param."""
        with self.assertRaises(ValueError) as ve:
            self.r0.height = 0
            self.r1.height = -2
            self.r2.height = -4

        # compare exception raised to string given
        self.assertEqual(
            ve.exception.__str__(), 'height must be > 0'
        )

    def test_invalid_type_x(self):
        """Tests the type of the x param and raises an execption."""
        with self.assertRaises(TypeError) as te:
            self.r0.x = True
            self.r1.x = 'Zero'
            self.r2.x = 0.0

        # compare exception raised to string given
        self.assertEqual(
            te.exception.__str__(), 'x must be an integer'
        )

    def test_less_than_zero_value_x(self):
        """Tests for negative value for x param."""
        with self.assertRaises(ValueError) as ve:
            self.r0.x = -2
            self.r1.x = -4
            self.r2.x = -6

        # compare exception raised to string given
        self.assertEqual(
            ve.exception.__str__(), 'x must be >= 0'
        )

    def test_invalid_type_y(self):
        """Tests the type of the y param and raises an execption."""
        with self.assertRaises(TypeError) as te:
            self.r0.y = True
            self.r1.y = 'Zero'
            self.r2.y = 0.0

        # compare exception raised to string given
        self.assertEqual(
            te.exception.__str__(), 'y must be an integer'
        )

    def test_less_than_zero_value_y(self):
        """Tests for negative value for x param."""
        with self.assertRaises(ValueError) as ve:
            self.r0.y = -1
            self.r1.y = -2
            self.r2.y = -3

        # compare exception raised to string given
        self.assertEqual(
            ve.exception.__str__(), 'y must be >= 0'
        )

    def test_area_calc(self):
        """Test the area calculation method"""
        r0 = self.r0.area()
        self.assertEqual(r0, 20)

        # update width and height of r0 and try test again
        self.r0.width = 5
        self.r0.height = 3
        r0 = self.r0.area()
        self.assertEqual(r0, 15)


if __name__ == '__main__':
    unittest.main()
