from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np

def mean_square_error(expectedValues, observedValues):
    return sqrt(mean_squared_error(expectedValues, observedValues))

def element_error(expectedValues, observedValues, error_function = mean_square_error):
    return error_function(expectedValues, observedValues)
    
def batch_error(expectedBatchValues, observedBatchSize, error_function = mean_square_error):
    error_sum = 0
    batchSize = len(expectedBatchValues)
    
    for index in range(batchSize):
        error_sum = error_sum + error_function(expectedBatchValues[index], observedBatchSize[index])
    return error_sum / batchSize