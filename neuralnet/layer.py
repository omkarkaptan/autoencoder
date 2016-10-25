from neuron import Neuron

class Layer:
    neurons = None
    layer_number = -1   
    def __init__(self, number_of_neurons, number_of_inputs_from_previous_layer, layer_number):
	
	self.neurons = []
	self.layer_number = layer_number

	for i in range(number_of_neurons):
	    neuron = Neuron(number_of_inputs_from_previous_layer, 0)

	    self.neurons.append(neuron)

    def info(self):
	print "Layer #: {}\n".format(self.layer_number)
	print "Number of neurons in layer: {}\n".format(len(self.neurons))
	print "Neurons Info:\n"

	for neuron in self.neurons:
	    neuron.info()
