#!/usr/bin/python3
'''
Square Class Test Module
'''
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_inherits_from_rectangle(self):
        """
        Test if Square class properly inherits from Rectangle.
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_constructor_assigns_size_as_width_and_height(self):
        """
        Test if the Square constructor correctly assigns size as width and height.
        """
        size = 5
        square = Square(size)
        self.assertEqual(square.width, size)
        self.assertEqual(square.height, size)

    def test_square_constructor_inherits_from_rectangle(self):
        """
        Test if Square constructor properly calls the constructor of the Rectangle class.
        """
        size = 5
        x = 10
        y = 15
        square = Square(size, x, y, id=1)
        self.assertEqual(square.x, x)
        self.assertEqual(square.y, y)
        self.assertEqual(square.width, size)
        self.assertEqual(square.height, size)
        self.assertEqual(square.id, 1)

    def test_square_constructor_with_negative_size(self):
        """
        Test if Square constructor raises ValueError when a negative size is provided.
        """
        with self.assertRaises(ValueError):
            size = -5
            square = Square(size)

    def test_square_constructor_with_invalid_coordinates(self):
        """
        Test if Square constructor raises ValueError when invalid coordinates are provided.
        """
        with self.assertRaises(ValueError):
            size = 5
            x = -10
            y = "invalid"
            square = Square(size, x, y)

    def test_square_str_representation(self):
        """
        Test if the __str__ method of Square returns the correct string representation.
        """
        size = 5
        x = 10
        y = 15
        square = Square(size, x, y, id=1)
        expected_str = f"[Square] (1) {x}/{y} - {size}"
        self.assertEqual(str(square), expected_str)

    def test_square_size(self):
        '''
        Test if the size getter works correctly
        '''
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_set_square_size(self):
        '''
        Test if the size setter assigns the width and height correctly
        '''
        square = Square(7)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_invalid_square_size(self):
        '''
        Test if the size setter raises a ValueError for invalid input
        '''
        square = Square(3)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_non_integer_square_size(self):
        '''
        Test if the size setter raises a ValueError for non-integer input
        '''
        square = Square(4)
        with self.assertRaises(ValueError):
            square.size = "abc"

    def test_zero_square_size(self):
        '''
        Test if the size setter raises a ValueError for zero size
        '''
        square = Square(2)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_update_with_args(self):
        """
        Test updating attributes using *args.
        """
        square = Square(1, 5, 10, 15)
        square.update(2, 8, 20, 25)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)

    def test_update_with_kwargs(self):
        """
        Test updating attributes using **kwargs.
        """
        square = Square(1, 5, 10, 15)
        square.update(size=6, y=30)

        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 30)

    def test_update_with_args_and_kwargs(self):
        """
        Test updating attributes using both *args and **kwargs. *args should take precedence.
        """
        square = Square(1, 5, 10, 15)
        square.update(2, 8, 20, 25, size=6, y=30)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)


class TestSquareToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the to_dictionary method for a Square instance."""
        square = Square(1, 5, 2, 3)
        result_dict = square.to_dictionary()
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3,
        }
        self.assertDictEqual(result_dict, expected_dict)

    def test_to_dictionary_empty(self):
        """Test the to_dictionary method for an empty Square instance."""
        square = Square(None, None, None, None)
        result_dict = square.to_dictionary()
        expected_dict = {
            'id': None,
            'size': None,
            'x': None,
            'y': None,
        }
        self.assertDictEqual(result_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
