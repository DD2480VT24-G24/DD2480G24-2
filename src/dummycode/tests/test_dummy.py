import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from dummy import Dummy as d


class TestDummy(unittest.TestCase):
    def test_add(self):
        self.assertEqual(d.add(4,5), 9)
    
    def test_sub(self):
        self.assertEqual(d.sub(4,5), -1)

    def test_mult(self):
        self.assertEqual(d.mult(4,5), 20)

    def test_div(self):
        self.assertEqual(d.div(4,2), 2)
    
    def test_pow(self):
        self.assertEqual(d.pow(2,10), 1024)