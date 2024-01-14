#!/usr/bin/python3
"""Defines base class tests
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_constructor_with_id_arg(self):
        """Test the constructor when id is provided."""
        obj_1 = Base(id=45)
        obj_2 = Base(id=55)
        self.assertEqual(obj_1.id, 45)
        self.assertEqual(obj_2.id, 55)

    def test_constructor_with_no_id_arg(self):
        """Test the constructor when id is not provided."""
        obj_1 = Base()
        obj_2 = Base()
        obj_3 = Base()
        self.assertEqual(obj_1.id, 6)
        self.assertEqual(obj_2.id, 7)
        self.assertEqual(obj_3.id, 8)

    def test_incrementing_id(self):
        """Tests if id increments in cumulative manner."""
        obj_1 = Base()
        obj_2 = Base()
        obj_3 = Base(100)
        obj_4 = Base(202)
        obj_5 = Base()
        self.assertEqual(obj_1.id, 10)
        self.assertEqual(obj_2.id, 11)
        self.assertEqual(obj_3.id, 100)
        self.assertEqual(obj_4.id, 202)
        self.assertEqual(obj_5.id, 12)

    def test_mixture_of_id(self):
        """Test a mix of with_id arg and with_no id arg, and increment."""
        obj_1 = Base()
        obj_2 = Base()
        obj_3 = Base(45)
        obj_4 = Base(55)
        obj_5 = Base()
        self.assertEqual(obj_1.id, 13)
        self.assertEqual(obj_2.id, 14)
        self.assertEqual(obj_3.id, 45)
        self.assertEqual(obj_4.id, 55)
        self.assertEqual(obj_5.id, 15)

    def test_id_is_int(self):
        """Test if id is an integer when created with no id arg."""
        obj = Base()
        self.assertIsInstance(obj.id, int)


if __name__ == '__main__':
    unittest.main()
