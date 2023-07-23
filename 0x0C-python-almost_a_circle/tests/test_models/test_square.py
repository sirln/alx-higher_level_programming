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
        Set up the Square object for testing.
        """
        self.equad = Square(6, 6, 6, 6)
        self.square = Square(1)

    def test_square_1_exists(self):
        '''
        Test if Square object with size 1 exists.
        '''
        self.assertIsInstance(self.square, Square)

    def test_square_1_2_exists(self):
        '''
        Test if Square object with size 1, x=2 exists.
        '''
        square = Square(1, 2)
        self.assertIsInstance(square, Square)

    def test_square_1_2_3_exists(self):
        '''
        Test if Square object with size 1, x=2, y=3 exists.
        '''
        square = Square(1, 2, 3)
        self.assertIsInstance(square, Square)

    def test_square_invalid_size(self):
        '''
        Test if Square object with invalid size raises TypeError.
        '''
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_invalid_x(self):
        '''
        Test if Square object with invalid x coordinate raises TypeError.
        '''
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_invalid_y(self):
        '''
        Test if Square object with invalid y coordinate raises TypeError.
        '''
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_negative_size(self):
        '''
        Test if Square object with negative size raises ValueError.
        '''
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        '''
        Test if Square object with negative x coordinate raises ValueError.
        '''
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        '''
        Test if Square object with negative y coordinate raises ValueError.
        '''
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        '''
        Test if Square object with zero size raises ValueError.
        '''
        with self.assertRaises(ValueError):
            Square(0)

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

    def test_to_dictionary(self):
        """
        tests the public method to make sure it returns a dictionary
        """
        self.assertTrue(type(self.equad.to_dictionary()) is dict)

    def test_to_dictionary(self):
        '''
        Test if the to_dictionary() method returns the correct dictionary representation.
        '''
        square = Square(2, 3, 4, 5)
        expected_dict = {'id': 5, 'size': 2, 'x': 3, 'y': 4}
        self.assertDictEqual(square.to_dictionary(), expected_dict)

    def test_save_to_file_empty_list(self):
        '''
        Test if save_to_file([]) saves an empty list to file.
        '''
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_load_from_file_exists(self):
        '''
        Test if load_from_file() returns a list of Square objects when the file exists.
        '''
        square = Square(2, 3, 4, 5)
        Square.save_to_file([square])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 2)
        self.assertEqual(squares[0].x, 3)
        self.assertEqual(squares[0].y, 4)
        self.assertEqual(squares[0].id, 5)

    def test_create(self):
        """
        tests the Base class method create
        """
        instance_dict = self.equad.to_dictionary()
        square_dupe = Square.create(**instance_dict)
        self.assertTrue(type(square_dupe) is Square)

if __name__ == '__main__':
    unittest.main()
