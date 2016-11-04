import unittest
from utils.imageutils import *
from utils.matrixutils import *

class UtilsTest(unittest.TestCase):
    def test_read_single_pgm(self):
    	pgm_image = open("testresources/sample.pgm", "r")
    	raster = read_pgm_image(pgm_image)
    	self.assertEquals(len(raster), 32)
    
    	total_element_count = 0
    
    	for single_list in raster:	
    	    total_element_count = total_element_count +len(single_list)
    
    	self.assertEquals(total_element_count, 1024)

    def test_read_pgm_from_directory(self):
    	directory = "testresources/images"
    	image_count = 0
    	for image in read_pgm_from_directory_generator(directory):
    	    image_count = image_count + 1
    	
    	self.assertEquals(image_count, 6)

    def test_write_pgm(self):
	pgm_image = open("testresources/sample.pgm", "r")
	raster = read_pgm_image(pgm_image)
	print raster
	print type(raster)
	raster_1d = convert_to_1D_array(raster)
	twodlist = convert_1D_to_2D_array(raster_1d, 32)
	print twodlist
	print type(twodlist)

if __name__ == '__main__':
    unittest.main()
