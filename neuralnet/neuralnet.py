from layer import Layer 

class NeuralNet:
    
    layers = None
    activation_function = None
    error_function = None
    delta = None

    def __init__(self, number_of_inputs, neurons_per_hidden_layer, activation_function, error_function):
    	self.layers = []
    #	input_layer = Layer(number_of_inputs, number_of_inputs, 0) # NUMBER OF NEURONS SAME AS NUMBER OF INPUTS
    	
    #	self.layers.append(input_layer)
    	layer_number = 1
    	number_of_inputs_from_previous_layer = number_of_inputs + 1
    	for number_of_neurons in neurons_per_hidden_layer:
    	    hidden_layer = Layer(number_of_neurons, number_of_inputs_from_previous_layer, layer_number)
    	    
    	    self.layers.append(hidden_layer)
    	    number_of_inputs_from_previous_layer = number_of_neurons + 1
    	    layer_number = layer_number + 1
    
    	output_layer = Layer(number_of_inputs, number_of_inputs_from_previous_layer, layer_number)
    	self.layers.append(output_layer)
    
    	self.activation_function = activation_function
        self.error_function = error_function

    def info(self):
	print "Number of layers: {}\n".format(len(self.layers))

	print "Layers Info: \n"

	for layer in self.layers:
	    layer.info()

    def feedforward(self, external_input):
        input_to_layer = external_input
	 
	for layer in self.layers:
	    input_to_layer = layer.feedforward(input_to_layer, self.activation_function)

	return input_to_layer # which is the result from the output layer
    
    def backpropogate(self, expected_output, observed_output):
        delta = expected_output - observed_output
        number_of_hidden_layers = len(self.layers)
        for layer_number in reversed(range(0, number_of_hidden_layers)):
            delta = self.layers[layer_number].backpropogate(delta, self.activation_function)
        
