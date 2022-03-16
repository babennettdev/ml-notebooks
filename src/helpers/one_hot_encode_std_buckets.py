from typing import List
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode_std_buckets(
    *, 
    one_hot_encoder: OneHotEncoder,
    dataframe: pd.DataFrame,
    columns_to_encode: List,
    number_of_std_to_bucket: int
    bucket_zero: bool = False,
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
    
    bucket_zero : bool
        Create a bucket specifically for values equal to 0.

    Return
    ----------
    encoded_dataframe: pandas.DataFrame
    """
    for column_to_encode in columns_to_encode:
        column_prefix = f'{column_to_encode}_'

        for i, row in dataframe.iterrows():

            if dataframe[column_to_encode][i] == 0 and bucket_zero == True:
                dataframe[f'{column_prefix}_is_zero'][i] = 1
            
            else:
                column_mean = dataframe[column_to_encode].mean()
                column_std = dataframe[column_to_encode].std()

                for std_to_bucket in number_of_std_to_bucket:
                    dataframe[f'column_prefix_std_{std_to_bucket}'][i] = 0
                    dataframe[f'column_prefix_std_-{std_to_bucket}'][i] = 0
                    if dataframe[column_to_encode][i] >= ( column_mean + column_std * std_to_bucket ) \
                        and dataframe[column_to_encode][i] < ( column_mean + column_std * std_to_bucket ):
                            
                            dataframe[f'column_prefix_std_{std_to_bucket}'][i] = 1
                    
                    elif dataframe[column_to_encode][i] < ( column_mean - column_std * std_to_bucket ) \
                        and dataframe[column_to_encode][i] > ( column_mean + column_std * std_to_bucket ):
                            
                            dataframe[f'column_prefix_std_-{std_to_bucket}'][i] = 1
                    
                    elif std_to_bucket == number_of_std_to_bucket
                        if dataframe[column_to_encode][i] >= ( column_mean + column_std * std_to_bucket ):
                            dataframe[f'column_prefix_std_{std_to_bucket}'][i] = 1

                        elif dataframe[column_to_encode][i] < ( column_mean - column_std * std_to_bucket ):
                            dataframe[f'column_prefix_std_-{std_to_bucket}'][i] = 1


    return dataframe