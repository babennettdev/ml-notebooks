from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode_embarked(
    *, 
    one_hot_encoder: OneHotEncoder,
    titanic_dataframes: pd.DataFrame
) -> pd.DataFrame: 
    """
    Function to one hot encode embarked ("male" or "female").

    Parameters
    ----------
    one_hot_encoder : sklearn.preprocessing.OneHotEncoder
        OneHotEncoder from sci-kit learn.

    titanic_train_dataframes : pandas.DataFrame
        Input DataFrame.

    Return
    ----------
    titanic_dataframes: pandas.DataFrame
    """
    
    titanic_train_embarked_dataframes = one_hot_encoder.fit_transform(titanic_dataframes["Embarked"].values.reshape(-1, 1))
    titanic_train_embarked_dataframes.columns = one_hot_encoder.get_feature_names(['Embarked'])
    titanic_train_embarked_dataframes = pd.DataFrame(titanic_train_embarked_dataframes.toarray(), columns=titanic_train_embarked_dataframes.columns)
    titanic_dataframes= pd.concat([titanic_dataframes, titanic_train_embarked_dataframes ], axis=1)
    return titanic_dataframes