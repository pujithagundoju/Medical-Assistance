import os
import time
import pandas as pd

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.ensemble import RandomForestClassifier


def evaluate_random_forest():

    print("=" * 70)
    print("Random Forest - 5 Fold Cross Validation")
    print("=" * 70)

    os.makedirs("results", exist_ok=True)

    # Load data
    df = load_data("data/heart_disease.csv")

    df, encoders = clean_data(df)

    X = df.drop("Heart Disease Status", axis=1)
    y = df["Heart Disease Status"]

    # Model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    # Stratified KFold
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    scoring = {
        "accuracy": "accuracy",
        "precision": "precision",
        "recall": "recall",
        "f1": "f1",
        "roc_auc": "roc_auc"
    }

    start = time.time()

    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=scoring,
        return_train_score=False
    )

    end = time.time()

    results = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
            "ROC AUC"
        ],
        "Mean": [
            scores["test_accuracy"].mean(),
            scores["test_precision"].mean(),
            scores["test_recall"].mean(),
            scores["test_f1"].mean(),
            scores["test_roc_auc"].mean()
        ],
        "Std Dev": [
            scores["test_accuracy"].std(),
            scores["test_precision"].std(),
            scores["test_recall"].std(),
            scores["test_f1"].std(),
            scores["test_roc_auc"].std()
        ]
    })

    print(results)

    print("\nExecution Time:", round(end-start,2), "seconds")

    results.to_csv(
        "results/random_forest_cv.csv",
        index=False
    )

    print("\nSaved to results/random_forest_cv.csv")


if __name__ == "__main__":

    evaluate_random_forest()