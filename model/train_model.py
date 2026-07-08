
# import os
# import joblib
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     roc_auc_score,
#     confusion_matrix,
# )

# from preprocessing.data_loader import load_data
# from preprocessing.data_cleaning import clean_data


# # ============================================================
# # Create model directory
# # ============================================================

# os.makedirs("model", exist_ok=True)


# # ============================================================
# # Load Dataset
# # ============================================================

# df = load_data("data/cardio_train.csv")
# df = clean_data(df)


# # ============================================================
# # Features & Target
# # ============================================================

# X = df.drop("Heart_Disease", axis=1)
# y = df["Heart_Disease"]


# # ============================================================
# # Train-Test Split
# # ============================================================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42,
#     stratify=y,
# )


# # ============================================================
# # Random Forest
# # ============================================================

# model = RandomForestClassifier(
#     n_estimators=300,
#     max_depth=12,
#     min_samples_split=5,
#     min_samples_leaf=2,
#     random_state=42,
#     n_jobs=-1,
# )

# print("\nTraining Random Forest...\n")

# model.fit(X_train, y_train)


# # ============================================================
# # Prediction
# # ============================================================

# pred = model.predict(X_test)
# prob = model.predict_proba(X_test)[:, 1]


# # ============================================================
# # Metrics
# # ============================================================

# print("=" * 60)
# print("MODEL PERFORMANCE")
# print("=" * 60)

# print(f"Accuracy : {accuracy_score(y_test,pred):.4f}")
# print(f"Precision: {precision_score(y_test,pred):.4f}")
# print(f"Recall   : {recall_score(y_test,pred):.4f}")
# print(f"F1 Score : {f1_score(y_test,pred):.4f}")
# print(f"ROC AUC  : {roc_auc_score(y_test,prob):.4f}")

# print("\nConfusion Matrix")

# print(confusion_matrix(y_test,pred))


# # ============================================================
# # Save Model
# # ============================================================

# joblib.dump(model, "model/random_forest.pkl")

# print("\nModel saved successfully.")
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc,
    ConfusionMatrixDisplay
)

# ============================================================
# Create Required Directories
# ============================================================

os.makedirs("model", exist_ok=True)
os.makedirs("figures/chapter8", exist_ok=True)

# ============================================================
# Load Dataset
# ============================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = load_data("data/cardio_train.csv")
df = clean_data(df)

print(f"Dataset Shape : {df.shape}")

# ============================================================
# Features and Target
# ============================================================

X = df.drop("Heart_Disease", axis=1)
y = df["Heart_Disease"]

# ============================================================
# Train-Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ============================================================
# Train Random Forest
# ============================================================

print("\nTraining Random Forest...\n")

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ============================================================
# Predictions
# ============================================================

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ============================================================
# Evaluation Metrics
# ============================================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

# ============================================================
# Print Metrics
# ============================================================

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC AUC  : {roc_auc:.4f}")

print("\nConfusion Matrix")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ============================================================
# 10-Fold Cross Validation
# ============================================================

print("=" * 60)
print("10-FOLD CROSS VALIDATION")
print("=" * 60)

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=10,
    scoring="accuracy",
    n_jobs=-1
)

print(f"Average Accuracy : {cv_scores.mean():.4f}")
print(f"Standard Deviation : {cv_scores.std():.4f}")

# ============================================================
# Save Metrics
# ============================================================

metrics_df = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC",
        "10-Fold CV Accuracy"
    ],

    "Value":[
        accuracy,
        precision,
        recall,
        f1,
        roc_auc,
        cv_scores.mean()
    ]

})

metrics_df.to_csv(
    "model/model_metrics.csv",
    index=False
)

# ============================================================
# Confusion Matrix
# ============================================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Disease", "Disease"]
)

disp.plot(
    cmap="Blues",
    values_format="d"
)

plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "figures/chapter8/figure8_1_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ============================================================
# ROC Curve
# ============================================================

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(6,6))

plt.plot(
    fpr,
    tpr,
    linewidth=2.5,
    label=f"ROC Curve (AUC = {roc_auc:.4f})"
)

plt.plot(
    [0,1],
    [0,1],
    '--',
    linewidth=1.5,
    label="Random Guess"
)

plt.xlim([0,1])
plt.ylim([0,1.05])

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title("ROC Curve for Random Forest Classifier")

plt.grid(alpha=0.3)

plt.legend(loc="lower right")

plt.tight_layout()

plt.savefig(
    "figures/chapter8/figure8_2_roc_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ============================================================
# SHAP & LIME FIGURES
# ============================================================

from explainability.shap_analysis import get_shap_explanation
from explainability.lime_analysis import get_lime_explanation

from visualizations.shap_plots import shap_bar_plot
from visualizations.lime_plots import lime_bar_plot

print("\nGenerating SHAP & LIME Figures...")

sample = X_test.iloc[[0]]

# ---------------- SHAP ----------------

shap_df = get_shap_explanation(sample)

fig = shap_bar_plot(shap_df)

fig.savefig(
    "figures/chapter8/figure8_3_shap_bar.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

# ---------------- LIME ----------------

lime_df = get_lime_explanation(sample)

fig = lime_bar_plot(lime_df)

fig.savefig(
    "figures/chapter8/figure8_4_lime_bar.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("SHAP & LIME figures saved successfully.")
# ============================================================
# Save Model
# ============================================================

joblib.dump(
    model,
    "model/random_forest.pkl"
)

print("\nRandom Forest model saved successfully.")

print("\nEvaluation metrics saved to model/model_metrics.csv")

print("\nFigures saved to figures/chapter8/")