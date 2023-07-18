#!/usr/bin/python3
"""
Unittest for models/rectangle.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestClassRectangle(unittest.TestCase):
    """
    test the class Rectangle
    """

    def test_no_args(self):
        """
        test for what happens if did not pass any arguments
        """
        with self.assertRaises(TypeError):
            empty = Rectangle()

    def setUp(self):
        """
        this is for testing
        """
        self.quad = Rectangle(6, 6, 6, 6, 6)

    def test_set_id(self):
        """
        tests if the id was instantiated correctly
        """
        self.assertEqual(self.quad.id, 6)

    def test_width(self):
        """
        tests if width was instantiated correctly
        """
        self.assertEqual(self.quad.width, 6)

    def test_height(self):
        """
        tests if height was instantiated correctly
        """
        self.assertEqual(self.quad.height, 6)

    def test_x(self):
        """
        tests if x was instantiated correctly
        """
        self.assertEqual(self.quad.x, 6)

    def test_y(self):
        """
        tests if y was instantiated correctly
        """
        self.assertEqual(self.quad.y, 6)

    def test_get_set_width(self):
        """
        tests getter/setter for width
        """
        self.quad.width = 9
        self.assertEqual(self.quad.width, 9)

    def test_get_set_height(self):
        """
        tests getter/setter for height
        """
        self.quad.height = 9
        self.assertEqual(self.quad.height, 9)

    def test_get_set_x(self):
        """
        tests getter/setter for x
        """
        self.quad.x = 9
        self.assertEqual(self.quad.x, 9)

    def test_get_set_y(self):
        """
        tests getter/setter for y
        """
        self.quad.y = 9
        self.assertEqual(self.quad.y, 9)

    def test_update_args(self):
        """
        tests the update public method with *args
        """
        self.quad.update(8, 8, 8, 8, 8)
        self.assertEqual(self.quad.id, 8)
        self.assertEqual(self.quad.width, 8)
        self.assertEqual(self.quad.height, 8)
        self.assertEqual(self.quad.x, 8)
        self.assertEqual(self.quad.y, 8)

    def test_update_kwargs_id(self):
        """
        test updating the instance id with **kwargs
        """
        self.quad.update(id=6)
        self.assertEqual(self.quad.id, 6)

    def test_update_kwargs_width(self):
        """
        test updating the instance width with **kwargs
        """
        self.quad.update(width=6)
        self.assertEqual(self.quad.width, 6)

    def test_update_kwargs_height(self):
        """
        test updating the instance height with **kwargs
        """
        self.quad.update(height=6)
        self.assertEqual(self.quad.height, 6)

    def test_update_kwargs_x(self):
        """
        test updating the instance x with **kwargs
        """
        self.quad.update(x=6)
        self.assertEqual(self.quad.x, 6)

    def test_update_kwargs_y(self):
        """
        test updating the instance y with **kwargs
        """
        self.quad.update(y=6)
        self.assertEqual(self.quad.y, 6)

    def test_set_width_not_int(self):
        """
        test setting width with non-int
        """
        with self.assertRaises(TypeError):
            self.quad.width = "width"

    def test_set_width_neg_int(self):
        """
        test setting width with negative integer
        """
        with self.assertRaises(ValueError):
            self.quad.width = -5

    def test_area(self):
        """
        test public method that returns area of instance
        """
        self.assertEqual(self.quad.area(), 36)

    def test_display(self):
        """
        tests public method that prints in stdout the instance using '#' does
        not return anything
        """
        self.assertIsNone(self.quad.display())

    def test_subclass_of_base(self):
        """
        tests that Rectangle is a subclass of Base
        """
        self.assertIsInstance(self.quad, Base)

    def test_override_str(self):
        """
        tests that the overloading __str__ method returns correct string
        """
        self.assertEqual(self.quad.__str__(), "[Rectangle] (6) 6/6 - 6/6")

    def test_to_dictionary(self):
        """
        tests the public method to make sure it returns a dictionary
        """
        self.assertTrue(type(self.quad.to_dictionary()) is dict)

    def test_create(self):
        """
        tests the Base class method create
        """
        instance_dict = self.quad.to_dictionary()
        rectangle_dupe = Rectangle.create(**instance_dict)
        self.assertIsInstance(rectangle_dupe, Rectangle)

if __name__ == '__main__':
    unittest.main()
