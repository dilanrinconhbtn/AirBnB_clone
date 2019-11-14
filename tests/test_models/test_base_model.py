#!/usr/bin/python3
"""
Basemodel Class Tests
"""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):
    """
    Test base_model
    """

    @classmethod
    def setUp(cls):
        """setUp an instance"""
        cls.my_object = BaseModel()
        cls.my_object.name = "Jimbo"
        cls.my_object.number = 19

    def teardown(cls):
        """ Delete at the end of tests"""
        del cls.my_object

    def test_instance_BaseModel(self):
        """Testing my_object is instance of BaseModel"""
        self.assertTrue(isinstance(self.my_object, BaseModel))

    def test_str(self):
        """Testing __str__"""
        string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                              self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

if __name__ == '__main__':
    unittest.main()
