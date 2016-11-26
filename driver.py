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
    number_of_layers = read_number("Input Number of Hidden Layers: ")
    neurons_per_layer = []
    counter = 0
    for i in range(number_of_layers):
        number_of_neurons = read_number("Input number of neurons in hidden layer {}: ".format(i+1))
        neurons_per_layer.append(number_of_neurons)

    neural_net = NeuralNet(number_of_inputs, neurons_per_layer, sigmoid, mean_square_error)

    for i in range(0, 50):
        print "Iteration {}\n".format(i)
        
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
                print "============================================ UPDATE WEIGHTS ==================================================="
                neural_net.update_weights(batch_size)
                counter = 0
    
        if counter > 0:
            neural_net.update_weights(counter)
 
    raster = read_pgm_image(open("TrainImages/Adrien_Brody_0004.pgm"))
    raster = np.asarray(raster)
    X = convert_to_1D_array(raster)
    X = X.reshape(len(X), 1)
    
    result = neural_net.feedforward(X)
    print "Input image {}".format(X)
    print "Result is: {}".format(result)
    
    print "Difference before scale up is : {}".format(X-result)
    result = result * 255
    write_pgm_image(result, 32, 32, 255, 'test_output.pgm', directory="/home/gerard/git/autoencoder/output/")
    
    print "====================================== TASK 3 ============================================ \n"
    neural_net.visualize_trained_autoencoder(number_of_inputs)
    

if __name__ == "__main__":
    main()
