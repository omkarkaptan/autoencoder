import unittest
import numpy as np
from utils.errorcalculator import *

class UtilsTest(unittest.TestCase):
    def test_element_error(self):
        mean_square_error_result = element_error(np.array([3, -0.5, 2, 7]), np.array([2.5, 0.0, 2, 8]), mean_square_error)
        mean_square_error_result = round(mean_square_error_result, 3)
        self.assertEquals(mean_square_error_result, 0.612)
        
    def test_batch_error(self):
        mean_square_error_result = batch_error(np.array([[3, -0.5, 2, 7], [3, -0.5, 2, 7]]), np.array([[2.5, 0.0, 2, 8], [2.5, 0.0, 2, 8]]), mean_square_error)
        mean_square_error_result = round(mean_square_error_result, 3)
        print mean_square_error_result
        self.assertEquals(mean_square_error_result, 0.612)
        
if __name__ == '__main__':
    unittest.main()

