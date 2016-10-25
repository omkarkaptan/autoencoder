import numpy as np

class Neuron:
    weights = None
    bias = None

    def __init__(self, number_of_inputs, bias):
	self.weights = np.random.random((number_of_inputs,))
	
	self.bias = bias

    def info(self):
	print "Weights: {}\n".format(self.weights)
	print "Bias: {}\n".format(self.bias)
