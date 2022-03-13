from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode_passenger_class(
    *, 
    one_hot_encoder: OneHotEncoder,
    titanic_dataframes: pd.DataFrame
) -> pd.DataFrame: 
    """
    Function to one hot encode passenger class (1, 2, 3) -> (first class, second class, third class).

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
    
    titanic_train_pclass_dataframes = one_hot_encoder.fit_transform(titanic_dataframes["Pclass"].values.reshape(-1, 1))
    titanic_train_pclass_dataframes.columns = one_hot_encoder.get_feature_names(['Pclass'])
    titanic_train_pclass_dataframes = pd.DataFrame(titanic_train_pclass_dataframes.toarray(), columns=titanic_train_pclass_dataframes.columns)
    titanic_dataframes= pd.concat([titanic_dataframes, titanic_train_pclass_dataframes ], axis=1)
    return titanic_dataframes