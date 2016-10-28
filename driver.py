from utils.utils import *
from neuralnet.neuralnet import NeuralNet
import numpy as np

def main():
    number_of_layers = read_number("Input Number of Layers: ")
    number_of_inputs = read_number("Input number of inputs: ")
    neurons_per_layer = []

    for i in range(number_of_layers):
	number_of_neurons = read_number("Input number of neurons in layer {}: ".format(i))
	neurons_per_layer.append(number_of_neurons)

    neural_net = NeuralNet(number_of_inputs, neurons_per_layer, None)

    neural_net.info()

    X = np.array([  [1,0,0,1],
                [1,0,1,1],
                [1,1,0,1],
                [1,1,1,1] ])

    result = neural_net.feedforward(X)

    print "Result is: {}".format(result)

if __name__ == "__main__":
    main()
