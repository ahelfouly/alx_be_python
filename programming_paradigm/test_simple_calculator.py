import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
        self.assertEqual(self.calc.add(-4, 1), -3)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-4, -1), -3)
        self.assertEqual(self.calc.subtract(1, 1), 0)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-4, -1), 4)
        self.assertEqual(self.calc.multiply(1, 0), 0)
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-4, -1), 4.0)
        self.assertEqual(self.calc.divide(1, 0), None)
        self.assertEqual(self.calc.divide(4, -1), -4.0)
        self.assertEqual(self.calc.divide(-6, 1), 6.0)
