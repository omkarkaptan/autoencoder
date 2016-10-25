import numpy as np

def sigmoid(out,derivative=False):
    if(derivative==True):
        return out*(1-out)
    return 1/(1+np.exp(-out))