from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode_passenger_sex(
    *, 
    one_hot_encoder: OneHotEncoder,
    titanic_train_dataframes: pd.DataFrame
) -> pd.DataFrame: 
    """
    Function to one hot encode passenger sex ("male" or "female").

    Parameters
    ----------
    one_hot_encoder : sklearn.preprocessing.OneHotEncoder
        OneHotEncoder from sci-kit learn.

    titanic_train_dataframes : pandas.DataFrame
        Input DataFrame.

    Return
    ----------
    titanic_train_dataframes: pandas.DataFrame
    """
    
    titanic_train_sex_dataframes = one_hot_encoder.fit_transform(titanic_train_dataframes["Sex"].values.reshape(-1, 1))
    titanic_train_sex_dataframes.columns = one_hot_encoder.get_feature_names(['Sex'])
    titanic_train_sex_dataframes = pd.DataFrame(titanic_train_sex_dataframes.toarray(), columns=titanic_train_sex_dataframes.columns)
    titanic_train_dataframes= pd.concat([titanic_train_dataframes, titanic_train_sex_dataframes ], axis=1)
    return titanic_train_dataframes