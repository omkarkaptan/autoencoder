from weightmatrix import WeightMatrix
import activationfunctions
import numpy as np
from scipy.misc.common import derivative

class Layer:
    weightmatrix = None
    layer_number = -1
    output_of_layer = None
    output_of_previous_layer = None
    input_to_layer = None
    
    delta = None
    bias_delta = None

    def __init__(self, number_of_neurons, number_of_inputs_from_previous_layer, layer_number):
	self.weightmatrix = WeightMatrix(number_of_inputs_from_previous_layer, number_of_neurons, 0) 
	self.layer_number = layer_number

    def info(self):
	print "Layer #: {}\n".format(self.layer_number)
	self.weightmatrix.info()

    def feedforward(self, input_matrix, activation_function):
        self.output_of_previous_layer = input_matrix
    	#self.input_to_layer = np.dot(self.weightmatrix.weightmatrix, input_matrix)
        self.input_to_layer = self.weightmatrix.dotproduct(input_matrix, bias = True)
    	#print "Layer: {}".format(self.layer_number)
    	#print "Input to layer: {}".format(len(input_matrix))
    	#print "Input to Neurons: {}".format(self.input_to_layer)
    	self.output_of_layer = activationfunctions.run_activation_function(self.input_to_layer, activation_function)
    	#print "Output of Layer: {}".format(self.output_of_layer)
    	return self.output_of_layer
    
    def backpropogate(self, delta, activation_function):
        #print self.layer_number
        self.delta = delta * activationfunctions.run_activation_function(self.input_to_layer, activation_function)
        #print delta.shape
        self.bias_delta = self.delta # ?????
        #delta_for_previous_layer = (np.dot(self.weightmatrix.weightmatrix.T, delta)) * activation_function(self.output_of_previous_layer, derivative = True)
        delta_for_previous_layer = self.weightmatrix.dotproduct(self.delta, transpose = True, bias = False)
               
        return delta_for_previous_layer
    
    def calculate_total_delta(self):
        #print "Layer #: {}\n".format(self.layer_number)
        #print "Shape of delta: {}\n".format(self.delta.shape)
        #print "Shape of previous layer output: {}\n".format(self.output_of_previous_layer.shape)
        
        value_to_add_to_capital_delta = np.dot(self.delta, self.output_of_previous_layer.T)
        self.weightmatrix.add_to_capital_delta(value_to_add_to_capital_delta)
        
        self.weightmatrix.add_to_capital_delta_of_bias(self.bias_delta)
        
    def update_weights(self, batch_size):
        self.weightmatrix.update_weights(batch_size)
        
        
