import json
import pandas as pd

def calculate_numeric_constants(*, dataframe: pd.DataFrame, path_to_constants_file: str) -> float:
    """
    Function to calculate a dataframe's standard deviation, mean, minimum, maximum, and 25th, 50th, and 75th percentiles.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Pandas dataframe.

    path_to_constants_file : str
        Path to the file where you want to store the constants JSON.

    Return
    ----------
    None
    """
    constants_dict = {}

    for column in dataframe.columns:
        if dataframe[column].dtype in ['float', 'float64', 'int', 'int64']:
            constants_dict[column] = {
                "std": dataframe[column].std(),
                "mean": dataframe[column].mean(),
                "minimum": dataframe[column].min(),
                "maximum": dataframe[column].max(),
                "25th_percentile": dataframe[column].quantile(.25), 
                "50th_percentile": dataframe[column].quantile(.50), 
                "75th_percentile": dataframe[column].quantile(.75)
            }

    with open(path_to_constants_file, 'w') as outfile:
        json.dump(constants_dict, outfile)

    return None