from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

import pandas as pd


def audit_dataset():

    df = load_data("data/heart_disease.csv")

    print("="*70)
    print("ORIGINAL DATA")
    print("="*70)

    print(df.head())

    print("\nShape:", df.shape)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\n")

    print("="*70)
    print("TARGET DISTRIBUTION")
    print("="*70)

    print(df["Heart Disease Status"].value_counts())

    print("\nPercentage")

    print(
        df["Heart Disease Status"].value_counts(normalize=True)*100
    )

    print("\n")

    print("="*70)
    print("AFTER PREPROCESSING")
    print("="*70)

    cleaned_df, encoders = clean_data(df)

    print(cleaned_df.head())

    print("\nEncoded Classes")

    print(encoders["Heart Disease Status"].classes_)

    print("\nEncoded Target Counts")

    print(cleaned_df["Heart Disease Status"].value_counts())


if __name__ == "__main__":
    audit_dataset()