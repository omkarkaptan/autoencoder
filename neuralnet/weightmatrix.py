import numpy as np

class WeightMatrix:
    weightmatrix = None

    def __init__(self, number_of_inputs, number_of_neurons, bias):
	print str(number_of_inputs)+";"+str(number_of_neurons)
	self.weightmatrix = np.random.randn(number_of_inputs, number_of_neurons) # ADD + 1 for bias
	
    def info(self):
	weightmatrix_dimensions = self.weightmatrix.shape
	print "Number of inputs: {}".format(weightmatrix_dimensions[0])
	print "Number of neurons in layer: {}".format(weightmatrix_dimensions[1])
	print "Weight Matrix: {}\n".format(self.weightmatrix)

    def dotproduct(self, input_matrix):
	return np.dot(input_matrix, self.weightmatrix)
