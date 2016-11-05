import unittest
import numpy as np
from utils.matrixutils import *
from utils.imageutils import *
from neuralnet.activationfunctions import *

class NNTest(unittest.TestCase):
    def test_sigmoid_function(self):
	print sigmoid(0.5) 
        
if __name__ == '__main__':
    unittest.main()

