from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

df = load_data("data/heart_disease.csv")

df, encoders = clean_data(df)

X = df.drop("Heart Disease Status", axis=1)
y = df["Heart Disease Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42

)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

joblib.dump(model, "model/heart_model.pkl")
joblib.dump(encoders, "model/encoders.pkl")
