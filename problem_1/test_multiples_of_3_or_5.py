import unittest

from problem_1.multiples import multiples_of_3_or_5

class TestMultiplesOf3Or5(unittest.TestCase):
    """
    Test case for multiples_of_3_or_5 method.
    """
    def test_multiples_of_3(self):
        """
        Test case for multiples_of_3 method.
        """
        self.assertEqual(multiples_of_3_or_5(3), 3)
        self.assertEqual(multiples_of_3_or_5(6), 6)
        self.assertEqual(multiples_of_3_or_5(9), 9)
        self.assertEqual(multiples_of_3_or_5(12), 12)

    def test_multiples_of_5(self):
        """
        Test case for multiples_of_5 method.
        """
        self.assertEqual(multiples_of_3_or_5(5), 0)
        self.assertEqual(multiples_of_3_or_5(10), 0)
        self.assertEqual(multiples_of_3_or_5(15), 0)
        self.assertEqual(multiples_of_3_or_5(20), 0)

    def test_not_multiples_of_3_or_5(self):
        """
        Test case for not_multiples_of_3_or_5 method.
        """
        self.assertIsNone(multiples_of_3_or_5(1))
        self.assertIsNone(multiples_of_3_or_5(2))
        self.assertIsNone(multiples_of_3_or_5(4))
        self.assertIsNone(multiples_of_3_or_5(7))

if __name__ == '__main__':
    unittest.main()
