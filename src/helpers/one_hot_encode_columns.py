from typing import List
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode_columns(
    *, 
    one_hot_encoder: OneHotEncoder,
    dataframe: pd.DataFrame,
    columns_to_encode: List
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

    Return
    ----------
    encoded_dataframe: pandas.DataFrame
    """
    for column_to_encode in columns_to_encode:
        encoded_dataframe = one_hot_encoder.fit_transform(dataframe[column_to_encode].values.reshape(-1, 1))
        encoded_dataframe = encoded_dataframe.astype('int')
        encoded_dataframe.columns = one_hot_encoder.get_feature_names([column_to_encode])
        encoded_dataframe = pd.DataFrame(encoded_dataframe.toarray(), columns=encoded_dataframe.columns)
        dataframe = pd.concat([dataframe, encoded_dataframe ], axis=1)
    return dataframe