from numpy import ScalarType, ndarray, number
import pandas as pd

def calculate_average(values: ndarray) -> float:
    """
    Function to calculate the average of a numerical array.

    Parameters
    ----------
    values : ndarray
        N-dimensional numerical array.

    Return
    ----------
    average: float
    """

    sum = 0

    for value in values:
        if not pd.isna(value):
            sum = sum + value[0]

    average = sum / values.size
    return average