"""
plots.py

Visualization utilities for EDA and model evaluation.

Author : Pujitha
Project : Explainable Cardiac Risk Assessment using LLMs
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from experiments.utils import (
    PLOTS_DIR,
    create_directories,
    safe_filename,
    print_header
)


# ==========================================================
# Save Plot
# ==========================================================

def save_plot(
    figure,
    folder: str,
    filename: str
) -> Path:
    """
    Save matplotlib figure.

    Parameters
    ----------
    figure : matplotlib.figure.Figure

    folder : str

    filename : str
    """

    create_directories()

    save_folder = PLOTS_DIR / folder

    save_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    filepath = save_folder / (
        safe_filename(filename) + ".png"
    )

    figure.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(figure)

    return filepath


# ==========================================================
# Class Distribution
# ==========================================================

def plot_class_distribution(
    df: pd.DataFrame,
    target_column: str
):
    """
    Plot target distribution.
    """

    print_header(
        "Plotting Class Distribution"
    )

    fig, ax = plt.subplots(
        figsize=(6, 5)
    )

    counts = (
        df[target_column]
        .value_counts()
    )

    counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Target Distribution"
    )

    ax.set_xlabel(
        target_column
    )

    ax.set_ylabel(
        "Count"
    )

    for container in ax.containers:
        ax.bar_label(container)

    save_plot(
        fig,
        "eda",
        "target_distribution"
    )


# ==========================================================
# Missing Values
# ==========================================================

def plot_missing_values(
    missing_df: pd.DataFrame
):
    """
    Plot missing values.
    """

    print_header(
        "Plotting Missing Values"
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.bar(

        missing_df["Column"],

        missing_df["Missing Values"]

    )

    ax.set_title(
        "Missing Values"
    )

    ax.set_ylabel(
        "Count"
    )

    plt.xticks(
        rotation=90
    )

    save_plot(
        fig,
        "eda",
        "missing_values"
    )


# ==========================================================
# Histograms
# ==========================================================

def plot_histograms(
    df: pd.DataFrame
):
    """
    Plot histogram for every numerical feature.
    """

    print_header(
        "Generating Histograms"
    )

    numerical = df.select_dtypes(
        include="number"
    )

    for column in numerical.columns:

        fig, ax = plt.subplots(
            figsize=(6, 4)
        )

        ax.hist(
            numerical[column].dropna(),
            bins=30
        )

        ax.set_title(column)

        ax.set_xlabel(column)

        ax.set_ylabel("Frequency")

        save_plot(

            fig,

            "histograms",

            column

        )


# ==========================================================
# Boxplots
# ==========================================================

def plot_boxplots(
    df: pd.DataFrame
):
    """
    Plot boxplot for every numerical feature.
    """

    print_header(
        "Generating Boxplots"
    )

    numerical = df.select_dtypes(
        include="number"
    )

    for column in numerical.columns:

        fig, ax = plt.subplots(
            figsize=(5, 5)
        )

        ax.boxplot(

            numerical[column].dropna(),

            vert=True

        )

        ax.set_title(column)

        save_plot(

            fig,

            "boxplots",

            column

        )


# ==========================================================
# Correlation Heatmap
# ==========================================================

def plot_correlation_heatmap(
    df: pd.DataFrame
):
    """
    Plot correlation heatmap.
    """

    print_header(
        "Generating Correlation Heatmap"
    )

    corr = (
        df.select_dtypes(
            include="number"
        )
        .corr()
    )

    fig, ax = plt.subplots(
        figsize=(12, 10)
    )

    image = ax.imshow(
        corr,
        aspect="auto"
    )

    plt.colorbar(image)

    ax.set_xticks(
        range(len(corr.columns))
    )

    ax.set_xticklabels(

        corr.columns,

        rotation=90

    )

    ax.set_yticks(
        range(len(corr.columns))
    )

    ax.set_yticklabels(
        corr.columns
    )

    ax.set_title(
        "Correlation Heatmap"
    )

    save_plot(
        fig,
        "heatmaps",
        "correlation_heatmap"
    )


# ==========================================================
# Feature Importance
# ==========================================================

def plot_feature_importance(
    importance_df: pd.DataFrame
):
    """
    Plot feature importance.
    """

    print_header(
        "Plotting Feature Importance"
    )

    importance_df = (
        importance_df
        .sort_values(
            by="Importance",
            ascending=True
        )
    )

    fig, ax = plt.subplots(
        figsize=(8, 7)
    )

    ax.barh(

        importance_df["Feature"],

        importance_df["Importance"]

    )

    ax.set_title(
        "Feature Importance"
    )

    ax.set_xlabel(
        "Importance"
    )

    save_plot(

        fig,

        "feature_importance",

        "feature_importance"

    )


# ==========================================================
# ROC Curve (Reusable)
# ==========================================================

def plot_roc_curve(
    fpr,
    tpr,
    auc_score
):
    """
    Plot ROC curve.
    """

    fig, ax = plt.subplots(
        figsize=(6, 6)
    )

    ax.plot(
        fpr,
        tpr,
        label=f"AUC = {auc_score:.3f}"
    )

    ax.plot(
        [0, 1],
        [0, 1],
        "--"
    )

    ax.set_xlabel(
        "False Positive Rate"
    )

    ax.set_ylabel(
        "True Positive Rate"
    )

    ax.set_title(
        "ROC Curve"
    )

    ax.legend()

    save_plot(
        fig,
        "roc_curves",
        "roc_curve"
    )


# ==========================================================
# Confusion Matrix
# ==========================================================

def plot_confusion_matrix(
    confusion_matrix
):
    """
    Plot confusion matrix.
    """

    fig, ax = plt.subplots(
        figsize=(5, 5)
    )

    image = ax.imshow(
        confusion_matrix
    )

    plt.colorbar(image)

    for i in range(
        confusion_matrix.shape[0]
    ):

        for j in range(
            confusion_matrix.shape[1]
        ):

            ax.text(

                j,

                i,

                confusion_matrix[i, j],

                ha="center",

                va="center"

            )

    ax.set_xlabel(
        "Predicted"
    )

    ax.set_ylabel(
        "Actual"
    )

    ax.set_title(
        "Confusion Matrix"
    )

    save_plot(
        fig,
        "roc_curves",
        "confusion_matrix"
    )