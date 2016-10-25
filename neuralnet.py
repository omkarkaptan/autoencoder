from layer import Layer 

class NeuralNet:
    
    layers = None

    def __init__(self, number_of_inputs, neurons_per_hidden_layer):
	self.layers = []
	input_layer = Layer(number_of_inputs, number_of_inputs, 0) # NUMBER OF NEURONS SAME AS NUMBER OF INPUTS
	
	self.layers.append(input_layer)
	layer_number = 1
	number_of_inputs_from_previous_layer = number_of_inputs
	for number_of_neurons in neurons_per_hidden_layer:
	    hidden_layer = Layer(number_of_neurons, number_of_inputs_from_previous_layer, layer_number)
	    
	    self.layers.append(hidden_layer)
	    number_of_inputs_from_previous_layer = number_of_neurons
	    layer_number = layer_number + 1

	output_layer = Layer(number_of_inputs, number_of_inputs_from_previous_layer, layer_number)
	self.layers.append(output_layer)

    def info(self):
	print "Number of layers: {}\n".format(len(self.layers))

	print "Layers Info: \n"

	for layer in self.layers:
	    layer.info()

