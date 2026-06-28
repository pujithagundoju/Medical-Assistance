from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.ensemble import RandomForestClassifier
import pandas as pd


df = load_data("data/heart_disease.csv")
df, _ = clean_data(df)

X = df.drop("Heart Disease Status", axis=1)
y = df["Heart Disease Status"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")
print(importance)