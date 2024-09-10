import sum
import unittest

class TestPositiveSum(unittest.TestCase):
    def sum_positive(self):
        self.assertEqual(sum.sum(3,3),4)
        
if __name__ == '__main__':
    unittest.main()        
    