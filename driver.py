from utils.utils import *
from neuralnet.neuralnet import NeuralNet

def main():
    number_of_layers = read_number("Input Number of Layers: ")
    number_of_inputs = read_number("Input number of inputs: ")
    neurons_per_layer = []

    for i in range(number_of_layers):
	number_of_neurons = read_number("Input number of neurons in layer {}: ".format(i))
	neurons_per_layer.append(number_of_neurons)

    neural_net = NeuralNet(number_of_inputs, neurons_per_layer)

    neural_net.info()

if __name__ == "__main__":
    main()
