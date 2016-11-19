import numpy as np

class WeightMatrix:
    weightmatrix = None
    deltaweightmatrix = None
    learning_rate = 0.7

    def __init__(self, number_of_inputs, number_of_neurons, bias):
    	#print str(number_of_inputs)+";"+str(number_of_neurons)
    	self.weightmatrix = 2*np.random.random((number_of_neurons,number_of_inputs)) - 1 #np.random.randn(number_of_neurons, number_of_inputs)
        self.deltaweightmatrix = np.zeros((number_of_neurons, number_of_inputs))
	
    def info(self):
    	weightmatrix_dimensions = self.weightmatrix.shape
    	print "Number of inputs: {}".format(weightmatrix_dimensions[0])
    	print "Number of neurons in layer: {}".format(weightmatrix_dimensions[1])
    	print "Weight Matrix: {}\n".format(self.weightmatrix)

    def dotproduct(self, input_matrix, transpose_weight_matrix = True):
        if transpose_weight_matrix:
	       return np.dot(input_matrix, self.weightmatrix.T)
        else:
           return np.dot(input_matrix, self.weightmatrix)
    
    def add_to_capital_delta(self, small_delta):
        self.deltaweightmatrix = self.deltaweightmatrix + small_delta
        
    def update_weights(self):
        self.weightmatrix = self.learning_rate * self.weightmatrix + self.deltaweightmatrix
