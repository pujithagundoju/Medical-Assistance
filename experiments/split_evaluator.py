"""
===========================================================
Train-Test Split Evaluation

Objective:
Evaluate different train-test split ratios to identify
the most suitable split for the cardiac risk prediction model.

Author : Pujitha
===========================================================
"""

import os
import time
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

DATA_PATH = "data/heart_disease.csv"

RESULTS_FOLDER = "results"

RESULT_FILE = os.path.join(
    RESULTS_FOLDER,
    "split_results.csv"
)

REPORT_FOLDER = "reports"

REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "split_evaluation_summary.txt"
)

SPLITS = [
    0.40,
    0.35,
    0.30,
    0.25,
    0.20,
    0.15,
    0.10
]


# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

def load_dataset():

    df = load_data(DATA_PATH)

    df, _ = clean_data(df)

    X = df.drop("Heart Disease Status", axis=1)

    y = df["Heart Disease Status"]

    return X, y


# ----------------------------------------------------------
# Evaluate One Split
# ----------------------------------------------------------

def evaluate_split(X, y, test_size):

    train_percent = int((1 - test_size) * 100)

    test_percent = int(test_size * 100)

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=test_size,

        random_state=42,

        stratify=y

    )

    model = RandomForestClassifier(

        n_estimators=200,

        random_state=42,

        class_weight="balanced"

    )

    # ----------------------
    # Training
    # ----------------------

    train_start = time.perf_counter()

    model.fit(X_train, y_train)

    training_time = time.perf_counter() - train_start

    # ----------------------
    # Prediction
    # ----------------------

    predict_start = time.perf_counter()

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    prediction_time = time.perf_counter() - predict_start

    # ----------------------
    # Confusion Matrix
    # ----------------------

    tn, fp, fn, tp = confusion_matrix(

        y_test,

        predictions

    ).ravel()

    # ----------------------
    # Metrics
    # ----------------------

    return {

        "Train %": train_percent,

        "Test %": test_percent,

        "Accuracy": round(
            accuracy_score(y_test, predictions), 4
        ),

        "Precision": round(
            precision_score(
                y_test,
                predictions,
                zero_division=0
            ), 4
        ),

        "Recall": round(
            recall_score(
                y_test,
                predictions,
                zero_division=0
            ), 4
        ),

        "F1 Score": round(
            f1_score(
                y_test,
                predictions,
                zero_division=0
            ), 4
        ),

        "ROC AUC": round(
            roc_auc_score(
                y_test,
                probabilities
            ), 4
        ),

        "True Positive": tp,

        "True Negative": tn,

        "False Positive": fp,

        "False Negative": fn,

        "Training Time (s)": round(
            training_time,
            4
        ),

        "Prediction Time (s)": round(
            prediction_time,
            6
        )

    }


# ----------------------------------------------------------
# Save Summary Report
# ----------------------------------------------------------

def generate_report(best_result):

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    with open(REPORT_FILE, "w") as report:

        report.write("=" * 60 + "\n")

        report.write("TRAIN-TEST SPLIT EVALUATION\n")

        report.write("=" * 60 + "\n\n")

        report.write(
            f"Best Split : "
            f"{best_result['Train %']}:{best_result['Test %']}\n\n"
        )

        report.write(
            f"Accuracy : {best_result['Accuracy']}\n"
        )

        report.write(
            f"Precision : {best_result['Precision']}\n"
        )

        report.write(
            f"Recall : {best_result['Recall']}\n"
        )

        report.write(
            f"F1 Score : {best_result['F1 Score']}\n"
        )

        report.write(
            f"ROC AUC : {best_result['ROC AUC']}\n\n"
        )

        report.write(
            f"Training Time : "
            f"{best_result['Training Time (s)']} sec\n"
        )

        report.write(
            f"Prediction Time : "
            f"{best_result['Prediction Time (s)']} sec\n\n"
        )

        report.write("Conclusion\n")

        report.write("-" * 60 + "\n")

        report.write(
            "The selected split achieved the highest ROC-AUC\n"
            "while maintaining balanced Accuracy, Precision,\n"
            "Recall and F1-score. This split will be used\n"
            "for subsequent experiments.\n"
        )


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    print("\n" + "=" * 70)

    print("CARDIAC RISK - TRAIN TEST SPLIT EVALUATION")

    print("=" * 70)

    os.makedirs(RESULTS_FOLDER, exist_ok=True)

    X, y = load_dataset()

    results = []

    for split in SPLITS:

        train_percent = int((1 - split) * 100)

        test_percent = int(split * 100)

        print(
            f"Evaluating Split "
            f"{train_percent}:{test_percent}"
        )

        results.append(

            evaluate_split(
                X,
                y,
                split
            )

        )

    results_df = pd.DataFrame(results)

    # Rank using ROC-AUC → F1 → Accuracy

    results_df = results_df.sort_values(

        by=[
            "ROC AUC",
            "F1 Score",
            "Accuracy"
        ],

        ascending=False

    ).reset_index(drop=True)

    results_df.insert(

        0,

        "Rank",

        range(1, len(results_df) + 1)

    )

    results_df.to_csv(

        RESULT_FILE,

        index=False

    )

    best = results_df.iloc[0]

    generate_report(best)

    print("\n")

    print(results_df)

    print("\n" + "=" * 70)

    print("BEST SPLIT")

    print("=" * 70)

    print(
        f"Split : "
        f"{best['Train %']}:{best['Test %']}"
    )

    print(
        f"ROC-AUC : {best['ROC AUC']}"
    )

    print(
        f"F1 Score : {best['F1 Score']}"
    )

    print(
        f"Accuracy : {best['Accuracy']}"
    )

    print("\nResults Saved To")

    print(f"✔ {RESULT_FILE}")

    print(f"✔ {REPORT_FILE}")

    print("=" * 70)


if __name__ == "__main__":

    main()