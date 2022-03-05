import pandas as pd

def one_hot_encode_adult_or_child(
    *, 
    titanic_dataframes: pd.DataFrame,
    ages: pd.Series
) -> pd.DataFrame: 
    """
    Function to one hot encode passenger sex ("male" or "female").

    Parameters
    ----------
    titanic_train_dataframes : pandas.DataFrame
        Input DataFrame.
    
    ages : pd.Series
        Series containing "age" data.

    Return
    ----------
    titanic_dataframes: pandas.DataFrame
    """
    is_adult = []
    is_child = []

    for age in ages:
        if age > 12:
            is_adult.append(1)
            is_child.append(0)
        else: 
            is_adult.append(0)
            is_child.append(1)



    is_adult_dataframes = pd.DataFrame(is_adult, columns=["isAdult"])
    is_child_dataframes = pd.DataFrame(is_child, columns=["isChild"])

    titanic_dataframes= pd.concat([titanic_dataframes, is_adult_dataframes ], axis=1)
    titanic_dataframes= pd.concat([titanic_dataframes, is_child_dataframes ], axis=1)

    return titanic_dataframes