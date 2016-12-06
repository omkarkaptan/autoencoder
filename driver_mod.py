from utils.utils import *
from neuralnet.neuralnet import NeuralNet
import numpy as np
from utils.imageutils import *
from utils.matrixutils import *
from utils.errorcalculator import *
from neuralnet.activationfunctions import *
from sklearn.metrics.regression import mean_squared_error

def main():
    # Initialize Neural Net
    number_of_inputs = 1024
    batch_size = 32
    #number_of_layers = read_number("Input Number of Hidden Layers: ")
    number_of_layers = 2
    neurons_per_layer = []
    counter = 0

    for k in range(6, 7):        
        for j in range(number_of_layers):
            #number_of_neurons = read_number("Input number of neurons in hidden layer {}: ".format(i+1))
            number_of_neurons = 2**k
            neurons_per_layer.append(number_of_neurons)

        neural_net = NeuralNet(number_of_inputs, neurons_per_layer, sigmoid, mean_square_error, 0.01)

        for i in range(0, 50):
            print "Iteration {}\n".format(i)
            
            counter = 0
        
            for raster in read_pgm_from_directory_generator("TrainImages"):
                counter = counter + 1

                raster = np.asarray(raster)
                X = convert_to_1D_array(raster)
                X = X.reshape(len(X), 1)
                X.astype('float64')
                
                result = neural_net.feedforward(X)
                
                neural_net.backpropogate(X, result)
                
                neural_net.calculate_total_delta()
                
                if counter == batch_size:
#                    print "============================================ UPDATE WEIGHTS ==================================================="
                    neural_net.update_weights(batch_size)
                    counter = 0
        
            if counter > 0:
                neural_net.update_weights(counter)
    
    
        raster = read_pgm_image(open("TestImages/Aaron_Eckhart_0001.pgm"))
        raster = np.asarray(raster)
        X = convert_to_1D_array(raster)
        X = X.reshape(len(X), 1)
        
        result = neural_net.feedforward(X)
        print "Input image {}".format(X)
        print "Result is: {}".format(result)
        
        result = result * 255
        write_pgm_image(result, 32, 32, 255, "test_output_{}.pgm".format(number_of_neurons), directory="output/")

if __name__ == "__main__":
    main()
