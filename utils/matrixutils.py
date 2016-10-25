import numpy as np
from array import array

def convert_to_1D_array(NDArray):
    if isinstance(NDArray,np.ndarray):
        return NDArray.flatten()
    else:
        print 'Invalid parameter passed expected a NDArray'