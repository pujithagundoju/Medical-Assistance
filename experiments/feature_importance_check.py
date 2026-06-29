import os
import pandas as pd
import matplotlib.pyplot as plt

from preprocessing.data_loader import load_data
from preprocessing.data_cleaning import clean_data

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_PATH = "data/heart_disease.csv"

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

df = load_data(DATA_PATH)
df, _ = clean_data(df)

X = df.drop("Heart Disease Status", axis=1)
y = df["Heart Disease Status"]

# ---------------------------------------------------------
# Train-Test Split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------------
# Train Model
# ---------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ---------------------------------------------------------
# Feature Importance
# ---------------------------------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n==============================")
print("FEATURE IMPORTANCE")
print("==============================")
print(importance)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

csv_path = os.path.join(
    RESULTS_DIR,
    "feature_importance.csv"
)

importance.to_csv(csv_path, index=False)

# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

plt.figure(figsize=(10, 7))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.gca().invert_yaxis()

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")

plot_path = os.path.join(
    RESULTS_DIR,
    "feature_importance.png"
)

plt.tight_layout()
plt.savefig(plot_path)
plt.close()

print("\nSaved:")
print(csv_path)
print(plot_path)