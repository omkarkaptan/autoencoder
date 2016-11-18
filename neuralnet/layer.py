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

    def __init__(self, number_of_neurons, number_of_inputs_from_previous_layer, layer_number):
	self.weightmatrix = WeightMatrix(number_of_inputs_from_previous_layer, number_of_neurons, 0) 
	self.layer_number = layer_number

    def info(self):
	print "Layer #: {}\n".format(self.layer_number)
	self.weightmatrix.info()

    def feedforward(self, input_matrix, activation_function):
        self.output_of_previous_layer = input_matrix
        input_matrix = np.append(input_matrix, 1)
        input_matrix = input_matrix.reshape(len(input_matrix), 1)
    	self.input_to_layer = np.dot(self.weightmatrix.weightmatrix, input_matrix)
    	print "Layer: {}".format(self.layer_number)
    	print "Input to layer: {}".format(len(input_matrix))
    	print "Input to Neurons: {}".format(self.input_to_layer)
    	self.output_of_layer = activationfunctions.run_activation_function(self.input_to_layer, activation_function)
    	print "Output of Layer: {}".format(self.output_of_layer)
    	return self.output_of_layer
    
    def backpropogate(self, delta, activation_function):
        print self.layer_number
        self.delta = delta
        print delta.shape
        delta_for_previous_layer = np.delete((np.dot(self.weightmatrix.weightmatrix.T, delta)), len(self.weightmatrix.weightmatrix[0])-1, 0) * activation_function(self.output_of_previous_layer, derivative = True)
        
        return delta_for_previous_layer
                                                                    