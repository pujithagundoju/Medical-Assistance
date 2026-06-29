# # from preprocessing.data_loader import load_data
# # from preprocessing.data_cleaning import clean_data

# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score

# # import joblib

# # df = load_data("data/heart_disease.csv")

# # df, encoders = clean_data(df)

# # X = df.drop("Heart Disease Status", axis=1)
# # y = df["Heart Disease Status"]

# # X_train, X_test, y_train, y_test = train_test_split(
# #     X,
# #     y,
# #     test_size=0.2,
# #     random_state=42

# # )

# # model = RandomForestClassifier(
# #     n_estimators=200,
# #     random_state=42
# # )

# # model.fit(X_train, y_train)

# # predictions = model.predict(X_test)

# # print("Accuracy:", accuracy_score(y_test, predictions))

# # joblib.dump(model, "model/heart_model.pkl")
# # joblib.dump(encoders, "model/encoders.pkl")
# from preprocessing.data_loader import load_data
# from preprocessing.data_cleaning import clean_data

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     roc_auc_score,
#     confusion_matrix,
#     classification_report
# )

# import joblib

# # ===============================
# # Load Dataset
# # ===============================
# df = load_data("data/heart_disease.csv")

# # ===============================
# # Clean Dataset
# # ===============================
# df, encoders = clean_data(df)

# # ===============================
# # Separate Features and Target
# # ===============================
# X = df.drop("Heart Disease Status", axis=1)
# y = df["Heart Disease Status"]

# # ===============================
# # Train-Test Split
# # ===============================
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42,
#     stratify=y
# )

# print("\nTraining Class Distribution")
# print(y_train.value_counts())

# print("\nTesting Class Distribution")
# print(y_test.value_counts())

# # ===============================
# # Train Random Forest
# # ===============================
# model = RandomForestClassifier(
#     n_estimators=300,
#     max_depth=None,
#     min_samples_split=2,
#     min_samples_leaf=1,
#     class_weight="balanced",
#     random_state=42,
#     n_jobs=-1
# )

# model.fit(X_train, y_train)

# # ===============================
# # Predictions
# # ===============================
# predictions = model.predict(X_test)
# probabilities = model.predict_proba(X_test)[:, 1]

# # ===============================
# # Evaluation
# # ===============================
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions)
# recall = recall_score(y_test, predictions)
# f1 = f1_score(y_test, predictions)
# roc_auc = roc_auc_score(y_test, probabilities)

# print("\n==============================")
# print("MODEL PERFORMANCE")
# print("==============================")
# print(f"Accuracy : {accuracy:.4f}")
# print(f"Precision: {precision:.4f}")
# print(f"Recall   : {recall:.4f}")
# print(f"F1 Score : {f1:.4f}")
# print(f"ROC AUC  : {roc_auc:.4f}")

# print("\nConfusion Matrix")
# print(confusion_matrix(y_test, predictions))

# print("\nClassification Report")
# print(classification_report(y_test, predictions))

# # ===============================
# # Save Model
# # ===============================
# joblib.dump(model, "model/heart_model.pkl")
# joblib.dump(encoders, "model/encoders.pkl")
# joblib.dump(list(X.columns), "model/feature_order.pkl")

# print("\nModel saved successfully.")
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data


# ============================================================
# Create model directory
# ============================================================

os.makedirs("model", exist_ok=True)


# ============================================================
# Load Dataset
# ============================================================

df = load_data("data/cardio_train.csv")
df = clean_data(df)


# ============================================================
# Features & Target
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
    stratify=y,
)


# ============================================================
# Random Forest
# ============================================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
)

print("\nTraining Random Forest...\n")

model.fit(X_train, y_train)


# ============================================================
# Prediction
# ============================================================

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]


# ============================================================
# Metrics
# ============================================================

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy_score(y_test,pred):.4f}")
print(f"Precision: {precision_score(y_test,pred):.4f}")
print(f"Recall   : {recall_score(y_test,pred):.4f}")
print(f"F1 Score : {f1_score(y_test,pred):.4f}")
print(f"ROC AUC  : {roc_auc_score(y_test,prob):.4f}")

print("\nConfusion Matrix")

print(confusion_matrix(y_test,pred))


# ============================================================
# Save Model
# ============================================================

joblib.dump(model, "model/random_forest.pkl")

print("\nModel saved successfully.")