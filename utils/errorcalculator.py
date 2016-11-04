from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np

def element_mean_square_error(expectedValues, observedValues):
    return sqrt(mean_squared_error(expectedValues, observedValues))
    
def batch_mean_square_error(expectedBatchValues, observedBatchSize):
    batch_mean_square_sum = np.sum(element_mean_square_error(expectedBatchValues, observedBatchSize))
    return batch_mean_square_sum / len(expectedBatchValues)
    
print batch_mean_square_error(np.array([[2,2,3] ,[2,2,3], [2,2,3]]), np.array([[0,2,6], [0,2,6], [0,2,6]]))