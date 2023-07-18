#!/usr/bin/python3
'''
Base Class Test Module
'''
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        '''
        Test whether the ID is correctly assigned
        when 'id' is provided
        '''
        obj1 = Base(10)
        self.assertEqual(obj1.id, 10)

        obj2 = Base(100)
        self.assertEqual(obj2.id, 100)

    def test_auto_increment(self):
        '''
        Test whether the ID is auto-incremented
        when 'id' is not provided
        '''
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_id_type(self):
        '''
        Assuming 'id' is always an integer,
        let's test that it's the case.
        '''
        obj = Base(123)
        self.assertIsInstance(obj.id, int)

    def test_id_uniqueness(self):
        '''
        Test whether the IDs are unique
        when 'id' is not provided
        '''
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_to_json_string_empty(self):
        """
        Test to check if to_json_string returns "[]" for an empty list.
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """
        Test to check if to_json_string returns "[]" when given None as input.
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_valid_list(self):
        """
        Test to check if to_json_string returns the correct JSON string representation for a valid list of dictionaries.
        """
        input_list = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        expected_output = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_output)

    def test_to_json_string_invalid_input(self):
        """
        Test to check if to_json_string raises a TypeError for invalid input.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string({"name": "Alice", "age": 30})

    def setUp(self):
        self.rectangle_instances = [Rectangle(10, 5), Rectangle(7, 3)]
        self.square_instances = [Square(5), Square(3)]

    def tearDown(self):
        ''' Remove the created JSON files after each test '''
        for cls_name in ["Rectangle", "Square"]:
            filename = f"{cls_name}.json"
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_with_rectangles(self):
        """Test save_to_file method with a list of Rectangle instances."""
        Base.save_to_file(self.rectangle_instances)
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[{"width": 10, "height": 5}, {"width": 7, "height": 3}]')

    def test_save_to_file_with_squares(self):
        """Test save_to_file method with a list of Square instances."""
        Base.save_to_file(self.square_instances)
        with open("Square.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[{"size": 5}, {"size": 3}]')

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file method with an empty list."""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[]')

    def test_save_to_file_with_none_list(self):
        """Test save_to_file method with None as list_objs."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[]')

    def test_from_json_string_valid(self):
        ''' Test a valid JSON string with a list of dictionaries '''
        json_string = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
        expected_result = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        self.assertEqual(Base.from_json_string(json_string), expected_result)

    def test_from_json_string_empty(self):
        ''' Test an empty JSON string, should return an empty list '''
        json_string = ''
        expected_result = []
        self.assertEqual(Base.from_json_string(json_string), expected_result)

    def test_from_json_string_none(self):
        ''' Test when the input is None, should return an empty list '''
        json_string = None
        expected_result = []
        self.assertEqual(Base.from_json_string(json_string), expected_result)

    def test_from_json_string_invalid(self):
        ''' Test an invalid JSON string, should raise an error '''
        json_string = 'This is not a valid JSON string'
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(json_string)

    def test_create_with_args(self):
        ''' Test the create method with positional arguments '''
        instance = Base.create(1, 2, 3, 4, 5)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)

    def test_create_with_kwargs(self):
        ''' Test the create method with keyword arguments '''
        instance = Base.create(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)

    def test_update_with_args(self):
        ''' Test the update method with positional arguments '''
        instance = Rectangle(1, 1)
        instance.update(2, 3, 4, 5, 6)
        self.assertEqual(instance.id, 2)
        self.assertEqual(instance.width, 3)
        self.assertEqual(instance.height, 4)
        self.assertEqual(instance.x, 5)
        self.assertEqual(instance.y, 6)

    def test_update_with_kwargs(self):
        ''' Test the update method with keyword arguments '''
        instance = Rectangle(1, 1)
        instance.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(instance.id, 2)
        self.assertEqual(instance.width, 3)
        self.assertEqual(instance.height, 4)
        self.assertEqual(instance.x, 5)
        self.assertEqual(instance.y, 6)


    def test_load_from_nonexistent_file(self):
        """Test loading from a nonexistent file should return an empty list."""
        filename = "NonExistentFile.json"
        if os.path.exists(filename):
            os.remove(filename)

        instances = Base.load_from_file()

        self.assertEqual(instances, [])

    def test_load_from_empty_file(self):
        """Test loading from an empty file should return an empty list."""
        filename = "EmptyFile.json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("")

        instances = Base.load_from_file()

        self.assertEqual(instances, [])

    def test_load_from_file_rectangle(self):
        """Test loading from a file with rectangle data should return a list of Rectangle instances."""
        filename = "Rectangle.json"
        data = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 7, "height": 3}]'
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(data)

        instances = Rectangle.load_from_file()

        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 5)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].width, 7)
        self.assertEqual(instances[1].height, 3)

    def test_load_from_file_square(self):
        """Test loading from a file with square data should return a list of Square instances."""
        filename = "Square.json"
        data = '[{"id": 1, "size": 5}, {"id": 2, "size": 7}]'
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(data)

        instances = Square.load_from_file()

        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Square)
        self.assertIsInstance(instances[1], Square)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].size, 5)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].size, 7)

    def tearDown(self):
        """Remove created JSON files after each test."""
        filenames = ["NonExistentFile.json", "EmptyFile.json", "Rectangle.json", "Square.json"]
        for filename in filenames:
            if os.path.exists(filename):
                os.remove(filename)

class TestBaseCSVSerialization(unittest.TestCase):
    def test_save_to_file_csv(self):
        ''' Test case for saving objects to CSV file '''

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        s1 = Square(11, 12, 13, 14)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1])

        with open("Rectangle.csv", "r") as file:
            content = file.read()
            self.assertIn("1,2,3,4,5", content)
            self.assertIn("6,7,8,9,10", content)

        with open("Square.csv", "r") as file:
            content = file.read()
            self.assertIn("11,12,13,14", content)

    def test_load_from_file_csv(self):
        ''' Test case for loading objects from CSV file '''

        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertTrue(all(isinstance(obj, Rectangle) for obj in rectangles))
        self.assertTrue(all(isinstance(obj, Square) for obj in squares))

        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 2)
        self.assertEqual(rectangles[0].height, 3)
        self.assertEqual(rectangles[0].x, 4)
        self.assertEqual(rectangles[0].y, 5)

        self.assertEqual(rectangles[1].id, 6)
        self.assertEqual(rectangles[1].width, 7)
        self.assertEqual(rectangles[1].height, 8)
        self.assertEqual(rectangles[1].x, 9)
        self.assertEqual(rectangles[1].y, 10)

        self.assertEqual(squares[0].id, 11)
        self.assertEqual(squares[0].size, 12)
        self.assertEqual(squares[0].x, 13)
        self.assertEqual(squares[0].y, 14)


if __name__ == '__main__':
    unittest.main()
