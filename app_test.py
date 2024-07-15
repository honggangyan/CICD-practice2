import unittest
from app import sum

class TestSumFunction(unittest.TestCase):


    def test_positive_numbers(self):
        self.assertEqual(sum(1, 1), 2)

    def test_negative_numbers(self):
        self.assertEqual(sum(-1, -2), -3)
    
    def test_float_number(self):
        self.assertEqual(sum(1.3, 2.3), 3.6)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum("1",2)

if __name__ == "__main__":
    unittest.main()