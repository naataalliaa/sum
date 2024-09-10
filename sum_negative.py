import sum
import unittest

class TestNegativeSum(unittest.TestCase):
    def sum_negative(self):
        self.assertEqual(sum.sum(-2,-2),-4)
        
if __name__ == '__main__':
    unittest.main()        
    