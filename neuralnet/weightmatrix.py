import numpy as np

class WeightMatrix:
    weightmatrix = None
    deltaweightmatrix = None
    deltaweightmatrix = None
    bias_delta = None

    learning_rate = 0.01

    def initdeltamatrices(self):
        self.deltaweightmatrix = np.zeros((self.weightmatrix.shape[0], self.weightmatrix.shape[1]))
        self.bias_delta = np.zeros((self.weightmatrix.shape[0], 1))

    def __init__(self, number_of_inputs, number_of_neurons, bias, learning_rate):
    	#print str(number_of_inputs)+";"+str(number_of_neurons)
    	self.weightmatrix = np.random.randn(number_of_neurons, number_of_inputs) * np.sqrt(2.0/number_of_neurons)
 #2*np.random.random((number_of_neurons,number_of_inputs)) - 1 #np.random.randn(number_of_neurons, number_of_inputs)
        self.bias = 2*np.random.random((number_of_neurons,1)) - 1

        self.initdeltamatrices()
        self.learning_rate = learning_rate

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
            return product #+ self.bias

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
        self.weightmatrix = self.weightmatrix + self.learning_rate * self.deltaweightmatrix/(batch_size*1.0)
 #       self.bias = self.bias + self.learning_rate * self.bias_delta / (batch_size*1.0)
        self.initdeltamatrices()
