from layer import Layer 
from numpy.core.test_rational import denominator
import numpy as np
from utils.imageutils import *

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

    def info(self):
	print "Number of layers: {}\n".format(len(self.layers))

	print "Layers Info: \n"

	for layer in self.layers:
	    layer.info()

    def feedforward(self, external_input):
        print "=== FEEDFORWARD ==="
        input_to_layer = external_input
	 
	for layer in self.layers:
	    input_to_layer = layer.feedforward(input_to_layer, self.activation_function)

	return input_to_layer # which is the result from the output layer
    
    def backpropogate(self, expected_output, observed_output):
        print "=== BACKPROPAGATE ==="
        print "Mean Squared Error: {}\n".format(self.error_function(expected_output, observed_output))
        delta = expected_output - observed_output
        number_of_hidden_layers = len(self.layers)
        for layer_number in reversed(range(0, number_of_hidden_layers)):
            delta = self.layers[layer_number].backpropogate(delta, self.activation_function)
        
    def calculate_total_delta(self):
        print "=== CALCULATE DELTA ==="
        number_of_hidden_layers = len(self.layers)
        for layer_number in reversed(range(0, number_of_hidden_layers)):
            self.layers[layer_number].calculate_total_delta()
            
    def update_weights(self, batch_size):
        print "=== UPDATE WEIGHTS ==="
        number_of_hidden_layers = len(self.layers)
        for layer_number in range(0, number_of_hidden_layers):
            self.layers[layer_number].update_weights(batch_size)
            
    def visualize_trained_autoencoder(self, image_size):
        print "VISUALIZE TRAINED AUTO ENCODER - for first hidden layer"
        first_hidden_layer = self.layers[0]
        number_of_neurons = len(first_hidden_layer.weightmatrix.weightmatrix)
        for neuron_index in range(number_of_neurons): # Those many times images will be created
            output_image = []
            for pixel_index in range(image_size): # Setting each pixel value
                
                neuron_net_input = first_hidden_layer.weightmatrix.neuron_net_input(neuron_index) # RMSE of all the inputs to that neuron
                input_weight_to_neuron = first_hidden_layer.weightmatrix.weightmatrix[neuron_index][pixel_index] # Weight of the pixel_index onto the neuron_index
                
                output_image.append(input_weight_to_neuron / neuron_net_input)
                
            output_image = np.asarray(output_image).reshape(len(output_image), 1)
            write_pgm_image(output_image, 32, 32, 255, 'trained_autoencoder_output ' + str(neuron_index) + '.pgm', directory="/home/gerard/git/autoencoder/trainedencoder/output/")
