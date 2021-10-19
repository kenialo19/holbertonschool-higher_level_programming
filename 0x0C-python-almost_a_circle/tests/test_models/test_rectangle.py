#!/usr/bin/python3
"""write unittests
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class testing_rectangle(unittest.TestCase):
    """unitted test"""
    def test_NegativeHeigh(self):
        """Test negative heigh"""

        self.assertRaises(ValueError, Rectangle, 2, -1)
    
    def test_widthngative(self):
        """test negative width"""

        self.assertRaises(ValueError,  Rectangle, -1, 2)

    def test_heightSetter(self):
        """Height is not a integer"""

        self.assertRaises(TypeError, Rectangle, 1, "Hello")

    def test_widthSetter(self):
        """width is not a integer"""

        self.assertRaises(TypeError, Rectangle, "Hello", 1)
