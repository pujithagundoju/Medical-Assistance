# import pandas as pd

# def load_data(path):
#     return pd.read_csv(path)
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the cardiovascular dataset.

    Parameters
    ----------
    file_path : str
        Path to cardio_train.csv

    Returns
    -------
    pd.DataFrame
    """

    try:
        df = pd.read_csv(file_path, sep=";")

        print("=" * 60)
        print("Dataset Loaded Successfully")
        print("=" * 60)
        print(f"Shape : {df.shape}")

        return df

    except Exception as e:
        raise Exception(f"Unable to load dataset.\n{e}")