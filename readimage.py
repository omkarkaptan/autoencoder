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

raster = read_pgm_image(open("TrainImages/Adrien_Brody_0004.pgm", "r"))

print raster
