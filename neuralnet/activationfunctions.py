import numpy as np
import bigfloat

def sigmoid(out,derivative=False):
    #np.seterr(all="raise")
    try:
        if(derivative==True):
            return out*(1-out)
        return 1/(1+np.exp(-out))
    except Exception as e:
        print "Overflow exception input: {}\n".format(out)
        print "Max input: {}\n".format(np.amax(out))
        print "Min input: {}\n".format(np.amin(out))
        np.seterr(all="print")

def run_activation_function(input_matrix, activation_function, derivative = False):
    return sigmoid(input_matrix, derivative)
