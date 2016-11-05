from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np

def element_mean_square_error(expectedValues, observedValues):
    return sqrt(mean_squared_error(expectedValues, observedValues))
    
def batch_mean_square_error(expectedBatchValues, observedBatchSize):
    error_sum = 0
    batchSize = len(expectedBatchValues)
    for index in range(batchSize):
        error_sum = error_sum + element_mean_square_error(expectedBatchValues[index], observedBatchSize[index])
    return error_sum / batchSize
