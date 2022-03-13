from typing import List
from numpy import ndarray, number
import pandas as pd

def fill_na_with_mean(dataframe: pd.DataFrame, columns_to_fill: List) -> float:
    """
    Function to fill N/A columns in a DataFrame with the mean value.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Pandas dataframe.

    Return
    ----------
    filled_dataframe : pandas.DataFrame
    """
    for column_to_fill in columns_to_fill:
        dataframe[column_to_fill].fillna(dataframe[column_to_fill].mean(),inplace=True)
    
    return dataframe