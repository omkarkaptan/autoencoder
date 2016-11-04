import unittest
import numpy as np
from utils.matrixutils import *
from utils.imageutils import *

class UtilsTest(unittest.TestCase):
    def test_convert_to_1D_array(self):
        pgm_image = open("testresources/sample.pgm", "r")
        raster = read_pgm_image(pgm_image)
        raster = np.asarray(raster)
        transformed_array = convert_to_1D_array(raster)
	print transformed_array
	print type(transformed_array)
        self.assertEquals(isinstance(transformed_array,np.ndarray), True, "Asserting instance of converted 1-D array")
        self.assertEquals(len(transformed_array), 1024, "Asserting size of converted 1-D array")
    
    def test_convert_to_nD_array(self):
	pgm_image = open("testresources/sample.pgm", "r")
	raster = read_pgm_image(pgm_image)
	raster = np.asarray(raster)
	transformed_array = convert_to_1D_array(raster)
	#print transformed_array
	print type(transformed_array)
	transformed_array2 = convert_1D_to_2D_array(transformed_array, 32)
	print transformed_array2
	print type(transformed_array2)

if __name__ == '__main__':
    unittest.main()

