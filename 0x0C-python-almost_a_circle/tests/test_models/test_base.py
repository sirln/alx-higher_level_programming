#!/usr/bin/python3
"""
Unittest for models/base.py
"""
import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """
    Test cases for the Base Class.
    """
    def test_create_instance_w_int_id(self):
        """
        tests for id of an instance with int id
        """
        b12 = Base(12)
        self.assertEqual(b12.id, 12)

    def test_create_instance_w_nint_id(self):
        """
        tests for id of an instance with non-int id
        """
        pi_base = Base(3.14)
        self.assertEqual(pi_base.id, 3.14)

    def test_create_instance_no_id(self):
        """
        tests for id of an instance that did not receive an id
        """
        first = Base()
        self.assertEqual(first.id, 1)

    def test_to_json_string_none(self):
        """
        Test the Base.to_json_string() method with None input.
        It should return an empty JSON array "[]".
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        """
        Test the Base.to_json_string() method with an empty list input.
        It should return an empty JSON array "[]".
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        """
        Test the Base.to_json_string() method with a list containing a single dictionary.
        It should return the JSON string representation of the dictionary in the list.
        """
        result = Base.to_json_string([{ 'id': 12 }])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_single_dict_returning_string(self):
        """
        Test the Base.to_json_string() method with a list containing a single dictionary.
        It should return a string as the output.
        """
        result = Base.to_json_string([{ 'id': 12 }])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """
        Test the Base.from_json_string() method with None input.
        It should return an empty list.
        """
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty_list(self):
        """
        Test the Base.from_json_string() method with an empty JSON array as input.
        It should return an empty list.
        """
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_single_dict(self):
        """
        Test the Base.from_json_string() method with a JSON string containing a single dictionary.
        It should return a list with the dictionary from the input JSON string.
        """
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{'id': 89}])

    def test_from_json_string_single_dict_returning_list(self):
        """
        Test the Base.from_json_string() method with a JSON string containing a single dictionary.
        It should return a list as the output.
        """
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
