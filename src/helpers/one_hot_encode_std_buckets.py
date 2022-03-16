from typing import List
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd

def one_hot_encode_std_buckets(
    *, 
    one_hot_encoder: OneHotEncoder,
    dataframe: pd.DataFrame,
    columns_to_encode: List,
    number_of_std_to_bucket: int,
    bucket_zero: bool = False,
    std_mean_constants_json: dict = {}
) -> pd.DataFrame: 
    """
    Function to one hot encode passenger sex ("male" or "female").

    Parameters
    ----------
    one_hot_encoder : sklearn.preprocessing.OneHotEncoder
        OneHotEncoder from sci-kit learn.

    dataframe : pandas.DataFrame
        Pandas dataframe.

    columns_to_encode : List
        List of columns on the dataframe to encode.

    number_of_std_to_bucket : int
        Number of standard deviations to bucket (greater than 0)

    bucket_zero : bool
        Create a bucket specifically for values equal to 0.

    std_mean_constants_json : object
        A JSON object with keys from {columns_to_encode} containing 
        keys "mean" and "std" with the mean and standard deviation
        of the column (meant for importing training values to transform test values)

    Return
    ----------
    encoded_dataframe: pandas.DataFrame
    """
    for column_to_encode in columns_to_encode:
        if bucket_zero == True:
            bucket_zero_array = np.zeros(len(dataframe.index), dtype=int)
            encoded_dataframe = pd.DataFrame(bucket_zero_array, columns=[f'{column_to_encode}_is_zero'])
            dataframe = pd.concat([dataframe, encoded_dataframe ], axis=1)

        for std_to_bucket in range(1, number_of_std_to_bucket+1):

                low_std_array = np.zeros(len(dataframe.index), dtype=int)
                low_std_encoded_dataframe = pd.DataFrame(low_std_array, columns=[f'{column_to_encode}_std_{std_to_bucket}'])
                dataframe = pd.concat([dataframe, low_std_encoded_dataframe ], axis=1)

                high_std_array = np.zeros(len(dataframe.index), dtype=int)
                high_std_encoded_dataframe = pd.DataFrame(high_std_array, columns=[f'{column_to_encode}_std_-{std_to_bucket}'])
                dataframe = pd.concat([dataframe, high_std_encoded_dataframe ], axis=1)

        for i in range(0, len(dataframe.index)):

            if dataframe[column_to_encode][i] == 0 and bucket_zero == True:
                dataframe.at[i, f'{column_to_encode}_is_zero'] = 1
            
            else:
                if (column_to_encode in std_mean_constants_json):
                    column_mean = std_mean_constants_json[column_to_encode]['mean']
                    column_std = std_mean_constants_json[column_to_encode]['std']

                else: 
                    column_mean = dataframe[column_to_encode].mean()
                    column_std = dataframe[column_to_encode].std()

                for std_to_bucket in range(1, number_of_std_to_bucket+1):
 
                    if dataframe[column_to_encode][i] >= ( column_mean + column_std * (std_to_bucket - 1) ) \
                        and dataframe[column_to_encode][i] < ( column_mean + column_std * std_to_bucket ):
                            dataframe.at[i, f'{column_to_encode}_std_{std_to_bucket}'] = 1
                    
                    elif dataframe[column_to_encode][i] < ( column_mean - column_std * (std_to_bucket - 1) ) \
                        and dataframe[column_to_encode][i] > ( column_mean - column_std * std_to_bucket ):
                            dataframe.at[i, f'{column_to_encode}_std_-{std_to_bucket}'] = 1
                    
                    elif std_to_bucket == number_of_std_to_bucket:
                        if dataframe[column_to_encode][i] >= ( column_mean + column_std * (std_to_bucket - 1) ):
                            dataframe.at[i, f'{column_to_encode}_std_{std_to_bucket}'] = 1

                        elif dataframe[column_to_encode][i] < ( column_mean - column_std * (std_to_bucket - 1) ):
                            dataframe.at[i, f'{column_to_encode}_std_-{std_to_bucket}'] = 1


    return dataframe