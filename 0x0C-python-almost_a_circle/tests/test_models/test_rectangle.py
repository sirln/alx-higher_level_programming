#!/usr/bin/python3
'''
Rectagle Class Test Module
'''
import sys
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        rect = Rectangle(10, 20, 5, 7, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 1)

    def test_width(self):
        """Test the getter and setter for width."""
        rect = Rectangle(10, 20)
        rect.width = 30
        self.assertEqual(rect.width, 30)

    def test_height(self):
        """Test the getter and setter for height."""
        rect = Rectangle(10, 20)
        rect.height = 25
        self.assertEqual(rect.height, 25)

    def test_x(self):
        """Test the getter and setter for x-coordinate."""
        rect = Rectangle(10, 20)
        rect.x = 15
        self.assertEqual(rect.x, 15)

    def test_y(self):
        """Test the getter and setter for y-coordinate."""
        rect = Rectangle(10, 20)
        rect.y = 12
        self.assertEqual(rect.y, 12)

    def test_valid_instantiation(self):
        """ Test valid instantiation with positive values """
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_invalid_width(self):
        """ Test width with non-integer value """
        with self.assertRaises(TypeError) as context:
            Rectangle("not_an_integer", 5, 2, 3)
        self.assertEqual(str(context.exception), "width must be an integer.")

        """ Test width with zero value """
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 5, 2, 3)
        self.assertEqual(str(context.exception), "width must be > 0.")

        """ Test width with negative value """
        with self.assertRaises(ValueError) as context:
            Rectangle(-5, 5, 2, 3)
        self.assertEqual(str(context.exception), "width must be > 0.")

    def test_invalid_height(self):
        """ Test height with non-integer value """
        with self.assertRaises(TypeError) as context:
            Rectangle(5, "not_an_integer", 2, 3)
        self.assertEqual(str(context.exception), "height must be an integer.")

        """ Test height with zero value """
        with self.assertRaises(ValueError) as context:
            Rectangle(5, 0, 2, 3)
        self.assertEqual(str(context.exception), "height must be > 0.")

        """ Test height with negative value """
        with self.assertRaises(ValueError) as context:
            Rectangle(5, -5, 2, 3)
        self.assertEqual(str(context.exception), "height must be > 0.")

    def test_invalid_x(self):
        """ Test x with non-integer value """
        with self.assertRaises(TypeError) as context:
            Rectangle(5, 10, "not_an_integer", 3)
        self.assertEqual(str(context.exception), "x must be an integer.")

        """ Test x with negative value """
        with self.assertRaises(ValueError) as context:
            Rectangle(5, 10, -2, 3)
        self.assertEqual(str(context.exception), "x must be >= 0.")

    def test_invalid_y(self):
        """ Test y with non-integer value """
        with self.assertRaises(TypeError) as context:
            Rectangle(5, 10, 2, "not_an_integer")
        self.assertEqual(str(context.exception), "y must be an integer.")

        """ Test y with negative value """
        with self.assertRaises(ValueError) as context:
            Rectangle(5, 10, 2, -3)
        self.assertEqual(str(context.exception), "y must be >= 0.")

    def setUp(self):
        self.rectangle_1 = Rectangle(5, 10)
        self.rectangle_2 = Rectangle(3, 6)
        self.rectangle_3 = Rectangle(0, 0)

    def test_area_with_positive_values(self):
        """
        Test the area method with positive length and width values.
        """
        self.assertEqual(self.rectangle_1.area(), 50, "Area calculation for rectangle_1 is incorrect")
        self.assertEqual(self.rectangle_2.area(), 18, "Area calculation for rectangle_2 is incorrect")

    def test_area_with_zero_values(self):
        """
        Test the area method with zero length and width values.
        """
        self.assertEqual(self.rectangle_3.area(), 0, "Area calculation for rectangle_3 is incorrect")

    def test_area_with_negative_values(self):
        """
        Test the area method with negative length and width values.
        """
        rectangle = Rectangle(-5, -10)
        self.assertEqual(rectangle.area(), 50, "Area calculation for rectangle with negative values is incorrect")

    def test_area_with_mixed_values(self):
        """
        Test the area method with a mix of positive and negative length and width values.
        """
        rectangle = Rectangle(4, -3)
        self.assertEqual(rectangle.area(), -12, "Area calculation for rectangle with mixed values is incorrect")

    def test_str_method(self):
        """
        Test case to check if the __str__ method returns the expected string format.
        """
        rect1 = Rectangle(1, 2, 5, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 1/2 - 5/10")

        rect2 = Rectangle(0, 0, 3, 4)
        self.assertEqual(str(rect2), "[Rectangle] (2) 0/0 - 3/4")

    def test_multiple_instances(self):
        """
        Test case to verify that multiple instances have different IDs.
        """
        rect1 = Rectangle(1, 2, 5, 10)
        rect2 = Rectangle(0, 0, 3, 4)
        rect3 = Rectangle(3, 1, 7, 8)

        self.assertNotEqual(rect1.id, rect2.id)
        self.assertNotEqual(rect1.id, rect3.id)
        self.assertNotEqual(rect2.id, rect3.id)

    def test_next_id_counter(self):
        """
        Test case to check if the next_id counter increments correctly.
        """
        current_next_id = Rectangle.next_id
        rect1 = Rectangle(1, 2, 5, 10)
        self.assertEqual(Rectangle.next_id, current_next_id + 1)

    def test_negative_dimensions(self):
        """
        Test case to check if the Rectangle can handle negative dimensions.
        """
        rect = Rectangle(-1, -2, -5, -10)
        self.assertEqual(str(rect), "[Rectangle] (3) -1/-2 - -5/-10")

    def test_zero_dimensions(self):
        """
        Test case to check if the Rectangle can handle zero dimensions.
        """
        rect = Rectangle(0, 0, 0, 0)
        self.assertEqual(str(rect), "[Rectangle] (4) 0/0 - 0/0")

    def test_update_with_no_args(self):
        """Test update method with no arguments."""
        rect = Rectangle(5, 7)
        rect.update()
        self.assertEqual(rect.length, 5)
        self.assertEqual(rect.width, 7)

    def test_update_with_one_arg(self):
        """Test update method with one argument."""
        rect = Rectangle(5, 7)
        rect.update(10)
        self.assertEqual(rect.length, 10)
        self.assertEqual(rect.width, 7)

    def test_update_with_two_args(self):
        """Test update method with two arguments."""
        rect = Rectangle(5, 7)
        rect.update(10, 3)
        self.assertEqual(rect.length, 10)
        self.assertEqual(rect.width, 3)

    def test_update_with_more_than_two_args(self):
        """Test update method with more than two arguments (should only consider the first two)."""
        rect = Rectangle(5, 7)
        rect.update(10, 3, 15)
        self.assertEqual(rect.length, 10)
        self.assertEqual(rect.width, 3)

    def test_update_with_positional_arguments(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(7, 15)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 15)

    def test_update_with_keyword_arguments(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(width=20, height=30)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 30)

    def test_update_with_mixed_arguments(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(25, height=35)
        self.assertEqual(rectangle.width, 25)
        self.assertEqual(rectangle.height, 35)

    def test_update_with_no_arguments(self):
        rectangle = Rectangle(5, 10)
        rectangle.update()
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)


class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        """ Create a rectangle object for testing """
        self.rectangle = Rectangle(5, 3)

    def test_area(self):
        """Test the area() method of Rectangle."""
        expected_area = 5 * 3
        self.assertEqual(self.rectangle.area(), expected_area)

    def test_display(self):
        """Test the display() method of Rectangle."""
        expected_output = "#####\n#####\n#####\n"
        ''' Capture stdout to check the output of display() '''
        captured_output = StringIO()
        sys.stdout = captured_output

        self.rectangle.display()

        ''' Reset stdout '''
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Rectangle."""
        rect = Rectangle(5, 10, 2, 3)
        expected_dict = {'id': id(rect), 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(rect.to_dictionary(), expected_dict)

        rect1 = Rectangle(1, 10, 20, 5, 8)
        dict1 = rect1.to_dictionary()
        self.assertEqual(dict1, {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 8})

        rect2 = Rectangle(2, 5, 5, 0, 0)
        dict2 = rect2.to_dictionary()
        self.assertEqual(dict2, {'id': 2, 'width': 5, 'height': 5, 'x': 0, 'y': 0})

        rect3 = Rectangle(3, 15, 25, -2, -2)
        dict3 = rect3.to_dictionary()
        self.assertEqual(dict3, {'id': 3, 'width': 15, 'height': 25, 'x': -2, 'y': -2})


class TestRectangleDisplay(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 3)

    def tearDown(self):
        self.rectangle = None

    def capture_stdout(self, func, *args):
        """Capture stdout output from the given function.

        Args:
            func (function): The function to be tested.
            *args: Variable length argument list.

        Returns:
            str: Captured stdout output.
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_display_default_position(self):
        """Test display method with default position (x=0, y=0)."""
        expected_output = "#####\n#####\n#####\n"
        captured_output = self.capture_stdout(self.rectangle.display)
        self.assertEqual(captured_output, expected_output)

    def test_display_custom_position(self):
        """ Test display method with custom position (x=2, y=1)."""
        self.rectangle.x = 2
        self.rectangle.y = 1
        expected_output = "  #####\n  #####\n  #####\n"
        captured_output = self.capture_stdout(self.rectangle.display)
        self.assertEqual(captured_output, expected_output)

    def test_display_zero_width(self):
        """Test display method with zero width."""
        self.rectangle.width = 0
        expected_output = ""
        captured_output = self.capture_stdout(self.rectangle.display)
        self.assertEqual(captured_output, expected_output)

    def test_display_zero_height(self):
        """Test display method with zero height."""
        self.rectangle.height = 0
        expected_output = ""
        captured_output = self.capture_stdout(self.rectangle.display)
        self.assertEqual(captured_output, expected_output)

    def test_display_negative_position(self):
        """Test display method with negative position (x=-2, y=-1)."""
        self.rectangle.x = -2
        self.rectangle.y = -1
        expected_output = "#####\n#####\n#####\n"
        captured_output = self.capture_stdout(self.rectangle.display)
        self.assertEqual(captured_output, expected_output)


if __name__ == '__main__':
    unittest.main()
