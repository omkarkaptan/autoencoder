import os

##
# Read PGM image files and asserts the first line for height width and maximum value
#
def read_pgm_image(pgmf):
    """Return a raster of integers from a PGM as a list of lists."""
    image_header = pgmf.readline().split()
    assert image_header[0] == 'P5'

    (width, height, depth) = [int(i) for i in image_header[1:]]
    assert depth <= 255

    raster = []
    for y in range(height):
	row = []
	for y in range(width):
		row.append(ord(pgmf.read(1)))
	raster.append(row)
    return raster

##
# A generator function that calls read_pgm_image and 
# returns of the result stack after next() is called from the calling function.
#
def read_pgm_from_directory_generator(imgDirectory):
    for img in os.listdir(imgDirectory):
        yield read_pgm_image(open(imgDirectory + "/" + img, 'r'))

##
# Test Main Application
#
if __name__ == '__main__':
    pgm_reader = read_pgm_from_directory_generator("TrainImages")
    print next(pgm_reader)
