import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    matthews_corrcoef,
    cohen_kappa_score,
    brier_score_loss,
    RocCurveDisplay,
    ConfusionMatrixDisplay
)

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ==========================================================
# Create folders
# ==========================================================

os.makedirs("results", exist_ok=True)
os.makedirs("results/plots", exist_ok=True)


# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 70)
print("Loading Dataset")
print("=" * 70)

df = load_data("data/cardio_train.csv")
df = clean_data(df)

X = df.drop("Heart_Disease", axis=1)
y = df["Heart_Disease"]


# ==========================================================
# Train Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================================
# Load Best Model
# ==========================================================

print("\nLoading Best Model...")

model = joblib.load("model/best_model.pkl")


# ==========================================================
# Prediction
# ==========================================================

pred = model.predict(X_test)

prob = model.predict_proba(X_test)[:, 1]


# ==========================================================
# Metrics
# ==========================================================

accuracy = accuracy_score(y_test, pred)

precision = precision_score(y_test, pred)

recall = recall_score(y_test, pred)

f1 = f1_score(y_test, pred)

roc_auc = roc_auc_score(y_test, prob)

mcc = matthews_corrcoef(y_test, pred)

kappa = cohen_kappa_score(y_test, pred)

brier = brier_score_loss(y_test, prob)


# ==========================================================
# Print Metrics
# ==========================================================

print("\n")
print("=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

print(f"Accuracy               : {accuracy:.4f}")
print(f"Precision              : {precision:.4f}")
print(f"Recall                 : {recall:.4f}")
print(f"F1 Score               : {f1:.4f}")
print(f"ROC AUC                : {roc_auc:.4f}")
print(f"Matthews Corrcoef      : {mcc:.4f}")
print(f"Cohen Kappa            : {kappa:.4f}")
print(f"Brier Score            : {brier:.4f}")


# ==========================================================
# Classification Report
# ==========================================================

print("\n")
print("=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)

print(classification_report(y_test, pred))


# ==========================================================
# Save Metrics
# ==========================================================

metrics_df = pd.DataFrame({

    "Metric": [

        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC",
        "Matthews Corrcoef",
        "Cohen Kappa",
        "Brier Score"

    ],

    "Value": [

        accuracy,
        precision,
        recall,
        f1,
        roc_auc,
        mcc,
        kappa,
        brier

    ]

})

metrics_df.to_csv(
    "results/model_metrics.csv",
    index=False
)


# ==========================================================
# Confusion Matrix
# ==========================================================

cm = confusion_matrix(y_test, pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.title("Confusion Matrix")

plt.savefig(
    "results/plots/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================================
# ROC Curve
# ==========================================================

RocCurveDisplay.from_predictions(
    y_test,
    prob
)

plt.title("ROC Curve")

plt.savefig(
    "results/plots/roc_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("\n")
print("=" * 70)
print("Evaluation Complete")
print("=" * 70)

print("Saved Files:")

print("results/model_metrics.csv")

print("results/plots/confusion_matrix.png")

print("results/plots/roc_curve.png")