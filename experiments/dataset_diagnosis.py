from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

import pandas as pd

print("=" * 70)
print("CARDIAC DATASET DIAGNOSIS")
print("=" * 70)

# ---------------------------------------------------
# Load Original Dataset
# ---------------------------------------------------

df = load_data("data/heart_disease.csv")

print("\nDataset Shape:")
print(df.shape)

# ---------------------------------------------------
# Target Distribution
# ---------------------------------------------------

print("\n" + "=" * 70)
print("TARGET DISTRIBUTION")
print("=" * 70)

print(df["Heart Disease Status"].value_counts())

print("\nPercentage")

print(
    df["Heart Disease Status"].value_counts(normalize=True) * 100
)

# ---------------------------------------------------
# Missing Values
# ---------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(df.isnull().sum())

# ---------------------------------------------------
# Data Cleaning
# ---------------------------------------------------

clean_df, encoders = clean_data(df)

# ---------------------------------------------------
# Label Encoding Check
# ---------------------------------------------------

print("\n" + "=" * 70)
print("TARGET LABEL ENCODING")
print("=" * 70)

print(encoders["Heart Disease Status"].classes_)

# ---------------------------------------------------
# Encoded Target Counts
# ---------------------------------------------------

print("\nEncoded Target Counts")

print(
    clean_df["Heart Disease Status"].value_counts()
)

# ---------------------------------------------------
# Target Correlation
# ---------------------------------------------------

print("\n" + "=" * 70)
print("FEATURE CORRELATION WITH TARGET")
print("=" * 70)

corr = clean_df.corr(numeric_only=True)["Heart Disease Status"]

corr = corr.drop("Heart Disease Status")

corr = corr.abs().sort_values(
    ascending=False
)

print(corr)

# ---------------------------------------------------
# Features with very weak correlation
# ---------------------------------------------------

print("\n" + "=" * 70)
print("FEATURES WITH CORRELATION > 0.05")
print("=" * 70)

print(corr[corr > 0.05])

print("\nDiagnosis Complete.")