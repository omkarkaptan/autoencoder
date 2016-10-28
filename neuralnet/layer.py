from weightmatrix import WeightMatrix
import activationfunctions

class Layer:
    weightmatrix = None
    layer_number = -1

    def __init__(self, number_of_neurons, number_of_inputs_from_previous_layer, layer_number):
	self.weightmatrix = WeightMatrix(number_of_inputs_from_previous_layer, number_of_neurons, 0) 
	self.layer_number = layer_number

    def info(self):
	print "Layer #: {}\n".format(self.layer_number)
	self.weightmatrix.info()

    def feedforward(self, input_matrix, activation_function):
	input_to_neurons = self.weightmatrix.dotproduct(input_matrix)

	output_of_layer = activationfunctions.run_activation_function(input_to_neurons, activation_function)
	return output_of_layer
