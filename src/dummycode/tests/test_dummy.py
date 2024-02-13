import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from dummy import add, sub, mult, div, pow


class TestDummy(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,5), 9)
    
    def test_sub(self):
        self.assertEqual(sub(4,5), -1)

    def test_mult(self):
        self.assertEqual(mult(4,5), 20)

    def test_div(self):
        self.assertEqual(div(4,2), 2)
    
    def test_pow(self):
        self.assertEqual(pow(2,10), 1024)