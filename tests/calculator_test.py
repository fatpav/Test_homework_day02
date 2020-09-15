import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_divide(self):
        self.assertEqual(4, divide(16, 4))

    def test_multiply(self):
        self.assertEqual(2, multiply(1, 2))






