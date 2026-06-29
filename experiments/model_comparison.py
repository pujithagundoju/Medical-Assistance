"""
==============================================================
Model Comparison Experiment

Objective:
Compare multiple machine learning models for cardiac
risk prediction and identify the best performing model.

Author : Pujitha
==============================================================
"""

import os
import time
import warnings

import pandas as pd

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

warnings.filterwarnings("ignore")

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_PATH = "data/heart_disease.csv"

RESULTS_DIR = "results"

REPORTS_DIR = "reports"

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

def load_dataset():

    df = load_data(DATA_PATH)

    df, _ = clean_data(df)

    X = df.drop("Heart Disease Status", axis=1)

    y = df["Heart Disease Status"]

    return train_test_split(

        X,
        y,

        test_size=0.30,

        random_state=42,

        stratify=y

    )


# ---------------------------------------------------------
# Models
# ---------------------------------------------------------

def get_models():

    return {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42
            ),

        "Decision Tree":
            DecisionTreeClassifier(
                random_state=42,
                class_weight="balanced"
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                class_weight="balanced"
            ),

        "Extra Trees":
            ExtraTreesClassifier(
                n_estimators=200,
                random_state=42,
                class_weight="balanced"
            ),

        "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=42
            )

    }


# ---------------------------------------------------------
# Evaluate Model
# ---------------------------------------------------------

def evaluate_model(model, X_train, X_test, y_train, y_test):

    train_start = time.perf_counter()

    model.fit(X_train, y_train)

    train_time = time.perf_counter() - train_start

    predict_start = time.perf_counter()

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    predict_time = time.perf_counter() - predict_start

    return {

        "Accuracy":
            round(
                accuracy_score(y_test, predictions),
                4
            ),

        "Precision":
            round(
                precision_score(
                    y_test,
                    predictions,
                    zero_division=0
                ),
                4
            ),

        "Recall":
            round(
                recall_score(
                    y_test,
                    predictions,
                    zero_division=0
                ),
                4
            ),

        "F1 Score":
            round(
                f1_score(
                    y_test,
                    predictions,
                    zero_division=0
                ),
                4
            ),

        "ROC AUC":
            round(
                roc_auc_score(
                    y_test,
                    probabilities
                ),
                4
            ),

        "Training Time (s)":
            round(train_time, 4),

        "Prediction Time (s)":
            round(predict_time, 6)

    }


# ---------------------------------------------------------
# Summary Report
# ---------------------------------------------------------

def create_report(best):

    report_path = os.path.join(

        REPORTS_DIR,

        "model_comparison_summary.txt"

    )

    with open(report_path, "w") as file:

        file.write("="*60 + "\n")

        file.write("MODEL COMPARISON SUMMARY\n")

        file.write("="*60 + "\n\n")

        file.write(f"Best Model : {best['Model']}\n\n")

        file.write(f"Accuracy : {best['Accuracy']}\n")

        file.write(f"Precision : {best['Precision']}\n")

        file.write(f"Recall : {best['Recall']}\n")

        file.write(f"F1 Score : {best['F1 Score']}\n")

        file.write(f"ROC AUC : {best['ROC AUC']}\n\n")

        if best["ROC AUC"] < 0.60:

            file.write("Conclusion\n")
            file.write("-"*60 + "\n")

            file.write(
                "All evaluated models produced similar "
                "performance.\n"
            )

            file.write(
                "The dataset appears difficult to classify "
                "using the available features.\n"
            )

            file.write(
                "Future work should investigate class "
                "imbalance handling,\n"
            )

            file.write(
                "feature engineering and threshold tuning.\n"
            )

        else:

            file.write("Conclusion\n")
            file.write("-"*60 + "\n")

            file.write(
                f"{best['Model']} achieved the highest "
                "overall performance.\n"
            )

            file.write(
                "This model will be selected for "
                "hyperparameter tuning.\n"
            )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("="*70)

    print("MODEL COMPARISON")

    print("="*70)

    X_train, X_test, y_train, y_test = load_dataset()

    models = get_models()

    results = []

    for name, model in models.items():

        print(f"Evaluating : {name}")

        metrics = evaluate_model(

            model,

            X_train,

            X_test,

            y_train,

            y_test

        )

        metrics["Model"] = name

        results.append(metrics)

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(

        by=[
            "ROC AUC",
            "F1 Score",
            "Recall",
            "Accuracy"
        ],

        ascending=False

    ).reset_index(drop=True)

    results_df.insert(

        0,

        "Rank",

        range(1, len(results_df)+1)

    )

    csv_path = os.path.join(

        RESULTS_DIR,

        "model_comparison.csv"

    )

    results_df.to_csv(

        csv_path,

        index=False

    )

    best = results_df.iloc[0]

    create_report(best)

    print()

    print(results_df)

    print()

    print("="*70)

    print("BEST MODEL")

    print("="*70)

    print(f"Model : {best['Model']}")

    print(f"ROC AUC : {best['ROC AUC']}")

    print(f"F1 Score : {best['F1 Score']}")

    print(f"Recall : {best['Recall']}")

    print(f"Accuracy : {best['Accuracy']}")

    print()

    print("Results Saved")

    print(csv_path)

    print(os.path.join(

        REPORTS_DIR,

        "model_comparison_summary.txt"

    ))

    print("="*70)


if __name__ == "__main__":

    main()