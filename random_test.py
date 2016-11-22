import array as ar
import random
import sys
import numpy as np

# define the width  (columns) and height (rows) of your image
width = 32
height = 32

# declare 1-d array of unsigned char and assign it random values
buff=ar.array('f')
buff2 = np.random.randn(10, 1)
print buff2
buff3 = buff2.tolist()
print buff3
for i in range(0, width*height):
  buff.append(random.randint(0,255))


# open file for writing 
filename = 'x.pgm'

try:
  fout=open(filename, 'wb')
except IOError, er:
  print "Cannot open file ", filename, "Exiting \n", er
  sys.exit()


# define PGM Header
pgmHeader = 'P5' + '\n' + str(width) + '  ' + str(height) + '  ' + str(255) + '\n'

# write the header to the file
fout.write(pgmHeader)

# write the data to the file 
buff.tofile(fout)

# close the file
fout.close()