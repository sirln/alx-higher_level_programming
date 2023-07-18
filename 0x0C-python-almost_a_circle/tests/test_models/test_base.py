#!/usr/bin/python3
"""
Unittest for models/base.py
"""
import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """
    test the class Base
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

if __name__ == '__main__':
    unittest.main()
