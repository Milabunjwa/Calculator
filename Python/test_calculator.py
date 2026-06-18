import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()