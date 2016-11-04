import numpy as np
from array import array

def convert_to_1D_array(NDArray):
    if isinstance(NDArray, list):
	NDArray = np.array(NDArray)
    
    if isinstance(NDArray,np.ndarray):
        return NDArray.flatten()
    else:
        print 'Invalid parameter passed expected a NDArray'

def convert_1D_to_2D_array(array, row_length):
    if row_length < 1:
	return "Invalid Row Length"
    elif type(array) == np.ndarray:
	array = array.tolist()
    
    return [array[i:i+row_length] for i in range(0, len(array), row_length)]
