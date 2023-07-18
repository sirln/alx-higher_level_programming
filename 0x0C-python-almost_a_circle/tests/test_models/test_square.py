#!/usr/bin/python3
"""
Unittest for models/square.py
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestClassSquare(unittest.TestCase):
    """
    test the class Square
    """

    def test_no_args(self):
        """
        test for what happens if did not pass any arguments
        """
        with self.assertRaises(TypeError):
            empty = Square()

    def setUp(self):
        """
        this is for testing
        """
        self.equad = Square(6, 6, 6, 6)

    def test_set_id(self):
        """
        tests if the id was instantiated correctly
        """
        self.assertEqual(self.equad.id, 6)

    def test_size(self):
        """
        tests if width was instantiated correctly
        """
        self.assertEqual(self.equad.size, 6)

    def test_x(self):
        """
        tests if x was instantiated correctly
        """
        self.assertEqual(self.equad.x, 6)

    def test_y(self):
        """
        tests if y was instantiated correctly
        """
        self.assertEqual(self.equad.y, 6)

    def test_get_set_size(self):
        """
        tests getter/setter for size
        """
        self.equad.size = 9
        self.assertEqual(self.equad.size, 9)

    def test_get_set_x(self):
        """
        tests getter/setter for x
        """
        self.equad.x = 9
        self.assertEqual(self.equad.x, 9)

    def test_get_set_y(self):
        """
        tests getter/setter for y
        """
        self.equad.y = 9
        self.assertEqual(self.equad.y, 9)

    def test_update_args(self):
        """
        tests the update public method with *args
        """
        self.equad.update(8, 8, 8, 8)
        self.assertEqual(self.equad.id, 8)
        self.assertEqual(self.equad.size, 8)
        self.assertEqual(self.equad.x, 8)
        self.assertEqual(self.equad.y, 8)

    def test_update_kwargs_id(self):
        """
        test updating the instance id with **kwargs
        """
        self.equad.update(id=6)
        self.assertEqual(self.equad.id, 6)

    def test_update_kwargs_size(self):
        """
        test updating the instance width with **kwargs
        """
        self.equad.update(size=6)
        self.assertEqual(self.equad.size, 6)

    def test_update_kwargs_x(self):
        """
        test updating the instance x with **kwargs
        """
        self.equad.update(x=6)
        self.assertEqual(self.equad.x, 6)

    def test_update_kwargs_y(self):
        """
        test updating the instance y with **kwargs
        """
        self.equad.update(y=6)
        self.assertEqual(self.equad.y, 6)

    def test_set_size_not_int(self):
        """
        test setting width with non-int
        """
        with self.assertRaises(TypeError):
            self.equad.size = "size"

    def test_set_size_neg_int(self):
        """
        test setting width with negative integer
        """
        with self.assertRaises(ValueError):
            self.equad.size = -5

    def test_area(self):
        """
        test public method that returns area of instance
        """
        self.assertEqual(self.equad.area(), 36)

    def test_display(self):
        """
        tests public method that prints in stdout the instance using '#' does
        not return anything
        """
        self.assertIsNone(self.equad.display())

    def test_subclass_of_base(self):
        """
        tests that Square is a subclass of Rectangle
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_override_str(self):
        """
        tests that the overloading __str__ method returns correct string
        """
        self.assertEqual(self.equad.__str__(), "[Square] (6) 6/6 - 6")

    def test_to_dictionary(self):
        """
        tests the public method to make sure it returns a dictionary
        """
        self.assertTrue(type(self.equad.to_dictionary()) is dict)

    def test_create(self):
        """
        tests the Base class method create
        """
        instance_dict = self.equad.to_dictionary()
        square_dupe = Square.create(**instance_dict)
        self.assertTrue(type(square_dupe) is Square)

if __name__ == '__main__':
    unittest.main()
