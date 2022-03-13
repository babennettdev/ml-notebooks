from typing import List
import numpy as np
import pandas as pd

def fill_na_with_mean_or_mode(dataframe: pd.DataFrame, columns_to_fill: List) -> float:
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
        if dataframe[column_to_fill].dtype == 'float' or dataframe[column_to_fill].dtype == 'float64' \
            or dataframe[column_to_fill].dtype == 'int' or dataframe[column_to_fill].dtype == 'int64':
                dataframe[column_to_fill].fillna(dataframe[column_to_fill].mean(),inplace=True) 
        else:
            dataframe[column_to_fill].replace('NaN',np.NaN,inplace=True)
            dataframe[column_to_fill].fillna(dataframe[column_to_fill].mode()[0],inplace=True)
    
    return dataframe