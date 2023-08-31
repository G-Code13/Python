import unittest
from LocalMath import *

class TestLocalMath(unittest.TestCase):
    
    def test_Add_Integers(self):
        self.assertEqual(Add(2, 3), 5)
    
    def test_Add_Doubles(self):
        self.assertEqual(Add(2.0, 3.5), 5.5)
    
    def test_Add_Strings(self):
        self.assertEqual(Add("2", "3"), "23")
    
    def test_Temperature_Conversion(self):
        self.assertAlmostEqual(Fahrenheit_To_Centigrade(0), 32)
        self.assertAlmostEqual(Fahrenheit_To_Centigrade(100), 212)
        self.assertAlmostEqual(Fahrenheit_To_Centigrade(20), 68)
    
    def test_Factors(self):
        expected_factors = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        self.assertEqual(Factors(36), expected_factors)
    
    def test_Divide_Integers(self):
        self.assertEqual(Divide(10, 2), 5)
    
    def test_Divide_doubles(self):
        self.assertAlmostEqual(Divide(10.0, 3.0), 3.3333333)
    
    def test_Divide_By_Zero(self):
        with self.assertRaises(ZeroDivisionError):
            Divide(10, 0)
    
    def test_Divide_Strings(self):
        with self.assertRaises(TypeError):
            Divide("10", "2")
    
    def test_Even_With_Even_Number(self):
        self.assertTrue(Even(6))
    
    def test_Even_With_Odd_Number(self):
        self.assertTrue(Even(7))

if __name__ == '__main__':
    unittest.main()