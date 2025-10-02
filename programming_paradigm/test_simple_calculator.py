import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        """Test the add method."""
        self.assertEqual(SimpleCalculator().add(2, 3), 5)
        self.assertEqual(SimpleCalculator().add(-2, 3), 1)
        self.assertEqual(SimpleCalculator().add(2, -3), -1)
        self.assertEqual(SimpleCalculator().add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator().subtract(2, 3), -1)
        self.assertEqual(SimpleCalculator().subtract(3, 2), 1)
        self.assertEqual(SimpleCalculator().subtract(3, -2), 5)
        self.assertEqual(SimpleCalculator().subtract(-3, 2), 5)
        self.assertEqual(SimpleCalculator().subtract(-3, -2), -1)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator().multiply(2, 3), 6)
        self.assertEqual(SimpleCalculator().multiply(2, 0), 0)

    def test_divide_normal(self):
        self.assertEqual(SimpleCalculator().divide(6, 3), 2)

    def test_divide_by_zero(self):
        self.assertIsNone(SimpleCalculator().divide(10, 0))