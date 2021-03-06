import os
import array

def read_pgm_image(pgmf):
    """Return a raster of integers from a PGM as a list of lists.
       Number of lists within the raster = height of the image.
       Number of elements within each list in the raster = width of the image """
    image_header = pgmf.readline().split()
    assert image_header[0] == 'P5'

    (width, height, depth) = [int(i) for i in image_header[1:]]
    assert depth <= 255

    raster = []
    for y in range(height):
	row = []
	for y in range(width):
		row.append(ord(pgmf.read(1)) / (1.0*depth))
	raster.append(row)
    return raster

def read_pgm_from_directory_generator(imgDirectory):
    """ Generator function which returns a raster for each pgm image in the specified directory"""
    for img in os.listdir(imgDirectory):
        yield read_pgm_image(open(imgDirectory + "/" + img, 'r'))

def write_pgm_image(pgm_image_array, width, height, depth, filename, directory=""):
    image_buffer = array.array('c')
    
    for i in range(0, len(pgm_image_array)):
        image_buffer.append(chr(int(round(pgm_image_array[i][0]))))
    
    #print "PGM IMAGE TO BE WRITTEN KA Type: {}".format(type(pgm_image_array))
    if len(pgm_image_array) != 1024:
        return
    
    try: 
        image_file = open(directory + filename, "wb")
    except IOError, er:
      print "Cannot open file ", filename, "Exiting\n", er
      sys.exit()

    pgmfileheader = "P5 {} {} {}\n".format(width, height, depth)

    image_file.write(pgmfileheader)
    image_buffer.tofile(image_file)

    image_file.close()
    
