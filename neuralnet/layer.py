from weightmatrix import WeightMatrix
import activationfunctions
import numpy as np

class Layer:
    weightmatrix = None
    layer_number = -1
    output_of_layer = None
    input_to_layer = None

    def __init__(self, number_of_neurons, number_of_inputs_from_previous_layer, layer_number):
	self.weightmatrix = WeightMatrix(number_of_inputs_from_previous_layer, number_of_neurons, 0) 
	self.layer_number = layer_number

    def info(self):
	print "Layer #: {}\n".format(self.layer_number)
	self.weightmatrix.info()

    def feedforward(self, input_matrix, activation_function):
        input_matrix = np.append(input_matrix, 1)
	self.input_to_layer = self.weightmatrix.dotproduct(input_matrix, transpose_weight_matrix = False)
	print "Layer: {}".format(self.layer_number)
	print "Input to layer: {}".format(len(input_matrix))
	print "Input to Neurons: {}".format(self.input_to_layer)
	self.output_of_layer = activationfunctions.run_activation_function(self.input_to_layer, activation_function)
	print "Output of Layer: {}".format(self.output_of_layer)
	return self.output_of_layer
    
    def backpropogate(self, error, activation_function):
        delta = error * activation_function(self.output_of_layer, derivative = True)
        if self.layer_number is not 0:
            current_layer_error = np.delete(self.weightmatrix.dotproduct(delta), -1, 0) # Ignore the bias while returning the error for the layer
            
        self.weightmatrix.update_weights(delta, self.input_to_layer)
        
        if self.layer_number is not 0:
            return current_layer_error
                                                                    