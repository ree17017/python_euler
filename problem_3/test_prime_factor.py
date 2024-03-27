import unittest
from prime_factor import prime_factor

class TestPrimeFactor(unittest.TestCase):
    """
    Test case for prime_factor method.
    """
    def test_prime_factor(self):
        """
        Test case for prime_factor method.
        """
        self.assertEqual(prime_factor(17), 17)
        self.assertEqual(prime_factor(13195), 29)
        self.assertEqual(prime_factor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()