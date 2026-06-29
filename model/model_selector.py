import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
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


# =====================================================
# Create folders
# =====================================================

os.makedirs("results", exist_ok=True)
os.makedirs("model", exist_ok=True)


# =====================================================
# Load Dataset
# =====================================================

print("=" * 70)
print("Loading Dataset...")
print("=" * 70)

df = load_data("data/cardio_train.csv")
df = clean_data(df)


# =====================================================
# Features and Target
# =====================================================

X = df.drop("Heart_Disease", axis=1)
y = df["Heart_Disease"]


# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# =====================================================
# Models
# =====================================================

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=1000,
            random_state=42
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            random_state=42,
            n_estimators=400,
            max_depth=12,
            min_samples_leaf=4,
            bootstrap=False,
            n_jobs=-1
        ),

    "Extra Trees":
        ExtraTreesClassifier(
            random_state=42,
            n_estimators=300,
            n_jobs=-1
        ),

    "Gradient Boosting":
        GradientBoostingClassifier(
            random_state=42
        ),

    "AdaBoost":
        AdaBoostClassifier(
            random_state=42
        )

}


# =====================================================
# Train and Evaluate
# =====================================================

results = []

best_model = None
best_auc = 0

print("\nTraining Models...\n")

for name, model in models.items():

    print(f"Training {name}...")

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, pred)

    prec = precision_score(y_test, pred)

    rec = recall_score(y_test, pred)

    f1 = f1_score(y_test, pred)

    auc = roc_auc_score(y_test, prob)

    results.append({

        "Model": name,
        "Accuracy": round(acc, 4),
        "Precision": round(prec, 4),
        "Recall": round(rec, 4),
        "F1 Score": round(f1, 4),
        "ROC AUC": round(auc, 4)

    })

    if auc > best_auc:

        best_auc = auc
        best_model = model


# =====================================================
# Results
# =====================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="ROC AUC",
    ascending=False
)

print("\n")
print("=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(results_df)


# =====================================================
# Save Results
# =====================================================

results_df.to_csv(
    "results/model_comparison.csv",
    index=False
)

joblib.dump(
    best_model,
    "model/best_model.pkl"
)

print("\n")
print("=" * 70)
print("BEST MODEL SAVED")
print("=" * 70)

print("Saved as:")
print("model/best_model.pkl")

print("\nBest ROC AUC:", best_auc)