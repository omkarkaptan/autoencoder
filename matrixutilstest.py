import unittest
import numpy as np
from matrixutils import *
from imageutils import *

class UtilsTest(unittest.TestCase):
    def test_convert_to_1D_array(self):
        pgm_image = open("testresources/sample.pgm", "r")
        raster = read_pgm_image(pgm_image)
        raster = np.asarray(raster)
        transformed_array = convert_to_1D_array(raster)
        
        self.assertEquals(isinstance(transformed_array,np.ndarray), True, "Asserting instance of converted 1-D array")
        self.assertEquals(len(transformed_array), 1024, "Asserting size of converted 1-D array")

if __name__ == '__main__':
    unittest.main()

