import unittest
from imageutils import *

class UtilsTest(unittest.TestCase):
    def read_single_pgm(self):
	pgm_image = open("testresources/sample.pgm", "r")
	raster = read_pgm_image(pgm_image)
	self.assertEquals(len(raster), 32)

	total_element_count = 0

	for single_list in raster:	
	    total_element_count = total_element_count +len(single_list)

	self.assertEquals(total_element_count, 1024)

    def read_pgm_from_directory(self):
	directory = "testresources/images"
	image_count = 0
	for image in read_pgm_from_directory_generator(directory):
	    image_count = image_count + 1
	
	self.assertEquals(image_count, 6)

if __name__ == '__main__':
    unittest.main()

