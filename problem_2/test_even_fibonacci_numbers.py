import unittest
from even_fibonacci_numbers import even_fibonacci_numbers

class TestEvenFibonacciNumbers(unittest.TestCase):
    def test_even_fibonacci_numbers(self):
        self.assertEqual(even_fibonacci_numbers(10), 2)
        self.assertEqual(even_fibonacci_numbers(20), 10)
        self.assertEqual(even_fibonacci_numbers(30), 10)
        self.assertEqual(even_fibonacci_numbers(50), 44)
        self.assertEqual(even_fibonacci_numbers(100), 44)
        self.assertEqual(even_fibonacci_numbers(1000), 798)
        self.assertEqual(even_fibonacci_numbers(10000), 3382)
        self.assertEqual(even_fibonacci_numbers(100000), 60696)
        self.assertEqual(even_fibonacci_numbers(1000000), 1089154)
        self.assertEqual(even_fibonacci_numbers(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()