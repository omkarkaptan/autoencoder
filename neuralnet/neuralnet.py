from layer import Layer

class NeuralNet:

    layers = None
    activation_function = None
    error_function = None
    delta = None
    batch_error = None
    def __init__(self, number_of_inputs, neurons_per_hidden_layer, activation_function, error_function):
    	self.layers = []
    #	input_layer = Layer(number_of_inputs, number_of_inputs, 0) # NUMBER OF NEURONS SAME AS NUMBER OF INPUTS

    #	self.layers.append(input_layer)
    	layer_number = 1
    	number_of_inputs_from_previous_layer = number_of_inputs
    	for number_of_neurons in neurons_per_hidden_layer:
    	    hidden_layer = Layer(number_of_neurons, number_of_inputs_from_previous_layer, layer_number)

    	    self.layers.append(hidden_layer)
    	    number_of_inputs_from_previous_layer = number_of_neurons
    	    layer_number = layer_number + 1

    	output_layer = Layer(number_of_inputs, number_of_inputs_from_previous_layer, layer_number)
    	self.layers.append(output_layer)

    	self.activation_function = activation_function
        self.error_function = error_function
        self.batch_error = 0

    def info(self):
	print "Number of layers: {}\n".format(len(self.layers))

	print "Layers Info: \n"

	for layer in self.layers:
	    layer.info()

    def feedforward(self, external_input):
        #print "=== FEEDFORWARD ==="
        input_to_layer = external_input

	for layer in self.layers:
	    input_to_layer = layer.feedforward(input_to_layer, self.activation_function)

	return input_to_layer # which is the result from the output layer

    def backpropogate(self, expected_output, observed_output):
    #        print "=== BACKPROPAGATE ==="
        #print "Mean Squared Error: {}\n".format(self.error_function(expected_output, observed_output))
        self.batch_error = self.batch_error + self.error_function(expected_output, observed_output)

        number_of_layers = len(self.layers)
        delta = (expected_output - observed_output) * self.activation_function(self.layers[number_of_layers-1].output_of_layer, derivative=True) # output layer delta
        self.layers[number_of_layers-1].delta = delta
    #        self.layers[number_of_layers-1].bias_delta = delta
        delta_for_hidden_layer = self.layers[number_of_layers-1].weightmatrix.dotproduct(delta, transpose=True, bias=False) #self.layers[number_of_layers-1].weightmatrix.dotproduct(delta, transpose = True, bias = False) # delta to hidden layer

        for layer_number in reversed(range(0, number_of_layers-1)):
            delta = self.layers[layer_number].backpropogate(delta_for_hidden_layer, self.activation_function)
            delta_for_hidden_layer = delta


    def calculate_total_delta(self):
    #       print "=== CALCULATE DELTA ==="
        number_of_hidden_layers = len(self.layers)
        for layer_number in reversed(range(0, number_of_hidden_layers)):
            self.layers[layer_number].calculate_total_delta()

    def update_weights(self, batch_size):
    #        print "=== UPDATE WEIGHTS ==="
    #    print self.batch_error/32.0
        self.batch_error = 0
        number_of_hidden_layers = len(self.layers)
        for layer_number in range(0, number_of_hidden_layers):
            self.layers[layer_number].update_weights(batch_size)
