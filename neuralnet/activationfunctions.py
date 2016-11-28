import numpy as np
import bigfloat

def sigmoid(out,derivative=False):
    if(derivative==True):
        return out*(1-out)
    return 1/(1+np.exp(-out))

def run_activation_function(input_matrix, activation_function, derivative = False):
    return sigmoid(input_matrix, derivative)
