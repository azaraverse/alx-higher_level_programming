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

        # update width and height of r0 and try testing again
        self.r0.width = 5
        self.r0.height = 3
        r0 = self.r0.area()
        self.assertEqual(r0, 15)

    def test_str(self):
        """Test the __str__ method"""
        # expected output
        r0 = '[Rectangle] (1) 0/0 - 10/2'
        r1 = '[Rectangle] (2) 0/0 - 2/10'
        r2 = '[Rectangle] (12) 0/0 - 10/2'

        # check output against expected output
        self.assertEqual(self.r0.__str__(), r0)
        self.assertEqual(self.r1.__str__(), r1)
        self.assertEqual(self.r2.__str__(), r2)

        # update values of parameters
        self.r0.update(id=5, width=20, height=5, x=2, y=4)
        self.r1.update(id=10, width=4, height=8, x=1, y=3)
        self.r2.update(id=15, width=7, height=6, y=8)

        # new expected output
        r0 = '[Rectangle] (5) 2/4 - 20/5'
        r1 = '[Rectangle] (10) 1/3 - 4/8'
        r2 = '[Rectangle] (15) 0/8 - 7/6'

        # test again
        self.assertEqual(self.r0.__str__(), r0)
        self.assertEqual(self.r1.__str__(), r1)
        self.assertEqual(self.r2.__str__(), r2)

    def test_update_method_args(self):
        """Test the update method"""
        # began testing above, so continue
        self.r0.update(10, 20, 10, 5, 0)
        self.r1.update(12, 10, 20, 0, 5)
        self.r2.update(14, 5, 5, 5, 5)

        # test some values of r0
        self.assertEqual(self.r0.width, 20)
        self.assertEqual(self.r0.y, 0)

        # test some values of r1
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.height, 20)

        # test some values of r2
        self.assertEqual(self.r2.id, 14)
        self.assertEqual(self.r2.width, 5)

    def test_update_method_one_positional_arg(self):
        """Test the update method passing one positional arg to function.

        Returns:
            ID update because that is the default when one argument is passed
        """
        self.r0.update(10)
        self.r1.update(20)
        self.r2.update(30)

        # test
        self.assertEqual(self.r0.id, 10)
        self.assertEqual(self.r1.id, 20)
        self.assertEqual(self.r2.id, 30)

    def test_update_kwargs(self):
        """Test the update method by using key-worded arguments"""
        self.r0.update(x=4)
        self.r1.update(id=100)
        self.r2.update(width=44)

        # test
        self.assertEqual(self.r0.x, 4)
        self.assertEqual(self.r1.id, 100)
        self.assertEqual(self.r2.width, 44)

    def test_update_args_kwargs(self):
        """Test the update method by passing both variable arguments
        and keyworded arguments of the ID argument to the method

        Returns:
            set variable or positional argument of ID rather than kwargs
        """
        self.r0.update(50, id=45)

        # test (should return 50 and not 45)
        self.assertEqual(self.r0.id, 50)

    def no_positional_arg_width(self):
        """Test Rectangle class with no width argument."""
        # x, y, and ID are set so there is no need to test for them
        with self.assertRaisesRegex(
            TypeError, "__init__() missing 1 required positional argument:"
            " 'width'"
        ):
            Rectangle(height=7)

    def no_positional_arg_height(self):
        """Test Rectangle class with no height argument."""
        # x, y, and ID are set so there is no need to test for them
        with self.assertRaisesRegex(
            TypeError, "__init__() missing 1 required positional argument:"
            " 'height'"
        ):
            Rectangle(width=17)

    def no_positional_args(self):
        """Test Rectangle class with no height argument."""
        # x, y, and ID are set so there is no need to test for them
        with self.assertRaisesRegex(
            TypeError, "__init__() missing 2 required positional arguments:"
            " 'width' and 'height'"
        ):
            Rectangle()


if __name__ == '__main__':
    unittest.main()
