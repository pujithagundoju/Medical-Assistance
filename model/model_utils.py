import joblib

from sklearn.model_selection import train_test_split

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
# Load Dataset
# ==========================================================

def load_dataset():

    df = load_data("data/cardio_train.csv")

    df = clean_data(df)

    return df


# ==========================================================
# Split Dataset
# ==========================================================

def split_dataset(df):

    X = df.drop("Heart_Disease", axis=1)

    y = df["Heart_Disease"]

    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


# ==========================================================
# Evaluate Model
# ==========================================================

def evaluate_model(model, X_test, y_test):

    pred = model.predict(X_test)

    prob = model.predict_proba(X_test)[:, 1]

    results = {

        "Accuracy":
            accuracy_score(y_test, pred),

        "Precision":
            precision_score(y_test, pred),

        "Recall":
            recall_score(y_test, pred),

        "F1 Score":
            f1_score(y_test, pred),

        "ROC AUC":
            roc_auc_score(y_test, prob)

    }

    return results


# ==========================================================
# Save Model
# ==========================================================

def save_model(model, filename):

    joblib.dump(model, filename)

    print(f"Model saved to {filename}")


# ==========================================================
# Load Model
# ==========================================================

def load_model(filename="model/best_model.pkl"):

    model = joblib.load(filename)

    return model


# ==========================================================
# Predict Probability
# ==========================================================

def predict_probability(model, sample):

    probability = model.predict_proba(sample)[0][1]

    prediction = model.predict(sample)[0]

    return prediction, probability