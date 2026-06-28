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


def evaluate_splits():

    print("=" * 70)
    print("CARDIAC RISK MODEL - TRAIN TEST SPLIT EVALUATION")
    print("=" * 70)

    # Create results folder automatically
    os.makedirs("results", exist_ok=True)

    # -------------------------
    # Load Dataset
    # -------------------------

    df = load_data("data/heart_disease.csv")

    df, encoders = clean_data(df)

    X = df.drop("Heart Disease Status", axis=1)
    y = df["Heart Disease Status"]

    # -------------------------
    # Different Split Ratios
    # -------------------------

    split_ratios = [
        0.40,
        0.35,
        0.30,
        0.25,
        0.20,
        0.15,
        0.10
    ]

    results = []

    # -------------------------
    # Evaluate Each Split
    # -------------------------

    for test_size in split_ratios:

        train_percent = int((1 - test_size) * 100)
        test_percent = int(test_size * 100)

        print(f"\nEvaluating Split {train_percent}:{test_percent}")

        X_train, X_test, y_train, y_test = train_test_split(

            X,
            y,

            test_size=test_size,

            random_state=42,

            stratify=y

        )

        # Balanced Random Forest

        model = RandomForestClassifier(

            n_estimators=200,

            random_state=42,

            class_weight="balanced"

        )

        # -------------------------
        # Training
        # -------------------------

        train_start = time.time()

        model.fit(X_train, y_train)

        train_end = time.time()

        # -------------------------
        # Prediction
        # -------------------------

        predict_start = time.time()

        predictions = model.predict(X_test)

        probabilities = model.predict_proba(X_test)[:, 1]

        predict_end = time.time()

        # -------------------------
        # Metrics
        # -------------------------

        accuracy = accuracy_score(

            y_test,

            predictions

        )

        precision = precision_score(

            y_test,

            predictions,

            average="binary",

            zero_division=0

        )

        recall = recall_score(

            y_test,

            predictions,

            average="binary",

            zero_division=0

        )

        f1 = f1_score(

            y_test,

            predictions,

            average="binary",

            zero_division=0

        )

        auc = roc_auc_score(

            y_test,

            probabilities

        )

        cm = confusion_matrix(

            y_test,

            predictions

        )

        tn, fp, fn, tp = cm.ravel()

        results.append({

            "Train %": train_percent,

            "Test %": test_percent,

            "Accuracy": round(accuracy, 4),

            "Precision": round(precision, 4),

            "Recall": round(recall, 4),

            "F1 Score": round(f1, 4),

            "ROC AUC": round(auc, 4),

            "True Positive": tp,

            "True Negative": tn,

            "False Positive": fp,

            "False Negative": fn,

            "Training Time (s)": round(

                train_end - train_start,

                4

            ),

            "Prediction Time (s)": round(

                predict_end - predict_start,

                4

            )

        })

    # -------------------------
    # Results Table
    # -------------------------

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(

        by="ROC AUC",

        ascending=False

    )

    print("\n")

    print("=" * 70)

    print("FINAL RESULTS")

    print("=" * 70)

    print(results_df)

    # -------------------------
    # Save CSV
    # -------------------------

    csv_path = "results/split_results.csv"

    results_df.to_csv(

        csv_path,

        index=False

    )

    print("\n")

    print(f"Results saved successfully to:\n{csv_path}")

    # -------------------------
    # Best Split
    # -------------------------

    best = results_df.iloc[0]

    print("\n")

    print("=" * 70)

    print("BEST SPLIT FOUND")

    print("=" * 70)

    print(

        f"{best['Train %']}:{best['Test %']}"

    )

    print(

        f"ROC AUC : {best['ROC AUC']}"

    )

    print(

        f"Accuracy : {best['Accuracy']}"

    )

    print(

        f"F1 Score : {best['F1 Score']}"

    )


if __name__ == "__main__":

    evaluate_splits()