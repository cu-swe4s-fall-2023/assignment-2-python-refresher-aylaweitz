import unittest 
import sys

sys.path.insert(0, '../src')
import my_utils # import my functions

class TestCalc(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(my_utils.calc_mean([1, 1, 2, 3, 4]), 2.2)  
        self.assertEqual(my_utils.calc_mean([-1, -1, 0, 3, 4]), 1.0) 

    def test_median(self):
        self.assertEqual(my_utils.calc_median([1, 1, 2, 3, 4]), 2.0) 
        self.assertEqual(my_utils.calc_median([-1, -1, 0, 3, 4]), 0.0) 

    def test_std(self):
        self.assertEqual(my_utils.calc_std([1, 1, 2, 1, 1]), 0.4)  
        self.assertEqual(my_utils.calc_std([-1, -1, 1, 1]), 1.0)  

    def test_convert_to_int(self):
        self.assertEqual(my_utils.convert_to_int(0.9), 1) # rounding up


if __name__ == '__main__':
    unittest.main()      