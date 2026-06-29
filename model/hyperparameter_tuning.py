import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV,
    StratifiedKFold
)
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ==========================================================
# Create folders
# ==========================================================

os.makedirs("model", exist_ok=True)


# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 70)
print("Loading Dataset...")
print("=" * 70)

df = load_data("data/cardio_train.csv")
df = clean_data(df)


# ==========================================================
# Features & Target
# ==========================================================

X = df.drop("Heart_Disease", axis=1)
y = df["Heart_Disease"]


# ==========================================================
# Train-Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================================
# Base Model
# ==========================================================

rf = RandomForestClassifier(
    random_state=42,
    n_jobs=-1
)


# ==========================================================
# Parameter Grid
# ==========================================================

param_grid = {

    "n_estimators": [200, 300, 400, 500],

    "max_depth": [8, 10, 12, 15, 20, None],

    "min_samples_split": [2, 5, 10],

    "min_samples_leaf": [1, 2, 4],

    "max_features": [
        "sqrt",
        "log2",
        None
    ],

    "bootstrap": [
        True,
        False
    ]

}


# ==========================================================
# Cross Validation
# ==========================================================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# ==========================================================
# Randomized Search
# ==========================================================

print("\nSearching Best Parameters...\n")

search = RandomizedSearchCV(

    estimator=rf,

    param_distributions=param_grid,

    n_iter=20,

    scoring="roc_auc",

    cv=cv,

    verbose=2,

    random_state=42,

    n_jobs=-1

)

search.fit(X_train, y_train)


# ==========================================================
# Best Model
# ==========================================================

best_model = search.best_estimator_


# ==========================================================
# Prediction
# ==========================================================

pred = best_model.predict(X_test)

prob = best_model.predict_proba(X_test)[:, 1]


# ==========================================================
# Results
# ==========================================================

print("\n")
print("=" * 70)
print("BEST PARAMETERS")
print("=" * 70)

print(search.best_params_)


print("\n")
print("=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)

print(f"Accuracy : {accuracy_score(y_test,pred):.4f}")

print(f"Precision: {precision_score(y_test,pred):.4f}")

print(f"Recall   : {recall_score(y_test,pred):.4f}")

print(f"F1 Score : {f1_score(y_test,pred):.4f}")

print(f"ROC AUC  : {roc_auc_score(y_test,prob):.4f}")


# ==========================================================
# Save Model
# ==========================================================

joblib.dump(
    best_model,
    "model/best_random_forest.pkl"
)


print("\n")
print("=" * 70)
print("Best Model Saved Successfully")
print("=" * 70)

print("Location:")
print("model/best_random_forest.pkl")
import json

with open("model/best_parameters.json", "w") as f:
    json.dump(search.best_params_, f, indent=4)

print("Best parameters saved to model/best_parameters.json")