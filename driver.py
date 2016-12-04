from utils.utils import *
from neuralnet.neuralnet import NeuralNet
import numpy as np
from utils.imageutils import *
from utils.matrixutils import *
from utils.errorcalculator import *
from neuralnet.activationfunctions import *
from sklearn.metrics.regression import mean_squared_error

def main():
    # ======== INITIALIZE ======== #
    number_of_inputs = 1024
    #    number_of_layers = read_number("Input Number of Hidden Layers: ")
    #    neurons_per_layer = []
    number_of_iterations = 50
    number_of_layers = 2
    statistics_file_name = "output/output_neurons.txt"
    result_file = open(statistics_file_name, "wb+")
    neurons_per_layer = []

    for learning_rate in [0.001, 0.01]:
        result_file.write("Learning Rate: {}\n".format(learning_rate))
        for number_of_iterations in [50, 100, 150]:
            result_file.write("Number of iterations: {}\n".format(number_of_iterations))
            for number_of_neurons in [64, 128, 256, 512]:
                result_file.write("Number of neurons: {}\n".format(number_of_neurons))
                for i in range(number_of_layers):
                    neurons_per_layer.append(number_of_neurons)

                neural_net = NeuralNet(number_of_inputs, neurons_per_layer, sigmoid, mean_square_error, learning_rate)
                batch_size = 32

                # ======== TRAIN ======== #
                for i in range(0, number_of_iterations):
                    counter = 0

                    for raster in read_pgm_from_directory_generator("TrainImages"):
                        counter = counter + 1

                        raster = np.asarray(raster)
                        X = convert_to_1D_array(raster)
                        X = X.reshape(len(X), 1)

                        result = neural_net.feedforward(X)

                        neural_net.backpropogate(X, result)

                        neural_net.calculate_total_delta()

                        if counter == batch_size:
                            neural_net.update_weights(batch_size)
                            counter = 0

                    if counter > 0:
                        neural_net.update_weights(counter)

                # ======== VALIDATE ======== #
                counter = 0
                rmse = 0
                for raster in read_pgm_from_directory_generator("ValImages"):
                    raster = np.asarray(raster)
                    X = convert_to_1D_array(raster)
                    X = X.reshape(len(X), 1)
                    result = neural_net.feedforward(X)
                    rmse = rmse + mean_square_error(X, result)
                    counter = counter + 1
                result_file.write("Mean Squared Error for Validation Set: {}\n".format(rmse/counter))

                # ======== TEST ======== #
                counter = 0
                rmse = 0
                for raster in read_pgm_from_directory_generator("TestImages"):
                    raster = np.asarray(raster)
                    X = convert_to_1D_array(raster)
                    X = X.reshape(len(X), 1)
                    result = neural_net.feedforward(X)
                    rmse = rmse + mean_square_error(X, result)
                    counter = counter + 1
                result_file.write("Mean Squared Error for Test Set: {}\n".format(rmse/counter))

                result = result * 255
                result_file_name = "test_output_N{}_I{}_L{}.pgm".format(number_of_neurons, number_of_iterations, learning_rate)
                write_pgm_image(result, 32, 32, 255, result_file_name, directory="output/")

if __name__ == "__main__":
    main()
