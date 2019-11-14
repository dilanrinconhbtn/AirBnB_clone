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
