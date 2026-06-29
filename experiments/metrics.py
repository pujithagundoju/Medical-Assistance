"""
metrics.py

Reusable evaluation metrics for machine learning experiments.

Author : Pujitha
Project : Explainable Cardiac Risk Assessment using LLMs
"""

from __future__ import annotations

import time
from typing import Dict, Any

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    balanced_accuracy_score,
    confusion_matrix,
    matthews_corrcoef,
    cohen_kappa_score,
    classification_report,
    roc_curve
)

from experiments.utils import save_dataframe


# ==========================================================
# Timing Utilities
# ==========================================================

def start_timer() -> float:
    """
    Start timer.
    """
    return time.perf_counter()


def stop_timer(start_time: float) -> float:
    """
    Stop timer.
    """
    return round(time.perf_counter() - start_time, 6)


# ==========================================================
# Confusion Matrix Metrics
# ==========================================================

def calculate_confusion_metrics(
    y_true,
    y_pred
) -> Dict[str, float]:
    """
    Calculate confusion-matrix-based metrics.
    """

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        y_pred
    ).ravel()

    specificity = 0.0
    sensitivity = 0.0

    if (tn + fp) != 0:
        specificity = tn / (tn + fp)

    if (tp + fn) != 0:
        sensitivity = tp / (tp + fn)

    return {

        "True Positive": tp,

        "True Negative": tn,

        "False Positive": fp,

        "False Negative": fn,

        "Specificity": round(specificity, 4),

        "Sensitivity": round(sensitivity, 4)

    }


# ==========================================================
# Complete Evaluation Metrics
# ==========================================================

def calculate_metrics(
    y_true,
    y_pred,
    probabilities=None
) -> Dict[str, Any]:
    """
    Calculate all evaluation metrics.
    """

    metrics = {

        "Accuracy":
            accuracy_score(
                y_true,
                y_pred
            ),

        "Precision":
            precision_score(
                y_true,
                y_pred,
                zero_division=0
            ),

        "Recall":
            recall_score(
                y_true,
                y_pred,
                zero_division=0
            ),

        "F1 Score":
            f1_score(
                y_true,
                y_pred,
                zero_division=0
            ),

        "Balanced Accuracy":
            balanced_accuracy_score(
                y_true,
                y_pred
            ),

        "MCC":
            matthews_corrcoef(
                y_true,
                y_pred
            ),

        "Cohen Kappa":
            cohen_kappa_score(
                y_true,
                y_pred
            )

    }

    if probabilities is not None:

        metrics["ROC AUC"] = roc_auc_score(
            y_true,
            probabilities
        )

    else:

        metrics["ROC AUC"] = None

    metrics.update(

        calculate_confusion_metrics(

            y_true,

            y_pred

        )

    )

    return metrics


# ==========================================================
# Classification Report
# ==========================================================

def classification_report_dataframe(
    y_true,
    y_pred
) -> pd.DataFrame:
    """
    Return classification report as DataFrame.
    """

    report = classification_report(

        y_true,

        y_pred,

        output_dict=True,

        zero_division=0

    )

    return pd.DataFrame(report).transpose()


# ==========================================================
# ROC Curve Data
# ==========================================================

def calculate_roc_curve(
    y_true,
    probabilities
):
    """
    Return ROC curve values.
    """

    return roc_curve(
        y_true,
        probabilities
    )


# ==========================================================
# Save Metrics
# ==========================================================

def save_metrics(
    metrics: Dict[str, Any],
    filename: str
):
    """
    Save metrics as CSV.
    """

    df = pd.DataFrame(
        [metrics]
    )

    save_dataframe(
        df,
        filename
    )

    return df


# ==========================================================
# Rank Models
# ==========================================================

def rank_models(
    results_df: pd.DataFrame,
    metric: str = "ROC AUC"
) -> pd.DataFrame:
    """
    Rank models based on a metric.
    """

    ranked = results_df.sort_values(

        by=metric,

        ascending=False

    ).reset_index(drop=True)

    ranked.insert(

        0,

        "Rank",

        range(1, len(ranked) + 1)

    )

    return ranked