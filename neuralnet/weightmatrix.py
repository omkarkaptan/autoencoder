import numpy as np
from math import sqrt

class WeightMatrix:
    weightmatrix = None
    bias = None
    
    deltaweightmatrix = None
    bias_delta = None
    
    learning_rate = 0.001

    def __init__(self, number_of_inputs, number_of_neurons, bias):
    	#print str(number_of_inputs)+";"+str(number_of_neurons)
    	self.weightmatrix = 2*np.random.random((number_of_neurons,number_of_inputs)) - 1 #np.random.randn(number_of_neurons, number_of_inputs)
        self.bias = 2*np.random.random((number_of_neurons,1)) - 1
        
        self.deltaweightmatrix = np.zeros((number_of_neurons, number_of_inputs))
        self.bias_delta = np.zeros((number_of_neurons, 1))
	
    def info(self):
    	weightmatrix_dimensions = self.weightmatrix.shape
    	print "Number of inputs: {}".format(weightmatrix_dimensions[0])
    	print "Number of neurons in layer: {}".format(weightmatrix_dimensions[1])
    	print "Weight Matrix: {}\n".format(self.weightmatrix)

    def dotproduct(self, input_matrix, transpose = False, bias = False):
        if transpose:
	       product = np.dot(self.weightmatrix.T, input_matrix)
        else:
           product = np.dot(self.weightmatrix, input_matrix)
        
        if bias: 
            return product + self.bias
        
        return product
    
    def dotproduct_with_bias(self, input_matrix, transpose = True):
        if transpose:
            return np.dot(self.bias.T, input_matrix)
        else:
            return np.dot(self.bias, input_matrix)
    
    def add_to_capital_delta(self, small_delta):
        self.deltaweightmatrix = self.deltaweightmatrix + small_delta
        
    def add_to_capital_delta_of_bias(self, bias_delta):
        self.bias_delta = self.bias_delta + bias_delta
        
    def update_weights(self, batch_size):
        self.weightmatrix = self.learning_rate * self.weightmatrix + self.deltaweightmatrix/(batch_size*1.0)
        self.bias = self.bias_delta / (batch_size*1.0)
        
    def neuron_net_input(self, neuron_index):
        return sqrt(sum(self.weightmatrix[neuron_index]**2))
        
