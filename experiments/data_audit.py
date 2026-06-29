"""
data_audit.py

Runs the complete Exploratory Data Analysis (EDA)
for the Explainable Cardiac Risk Assessment project.

Author : Pujitha
"""

from preprocessing.data_loader import load_data

from experiments.utils import (
    create_directories,
    print_header,
    print_success
)

from experiments.statistics import (
    dataset_overview,
    duplicate_analysis,
    missing_value_analysis,
    target_distribution,
    numerical_statistics,
    categorical_statistics
)

from experiments.plots import (
    plot_class_distribution,
    plot_missing_values,
    plot_histograms,
    plot_boxplots,
    plot_correlation_heatmap
)


# ==========================================================
# Configuration
# ==========================================================

DATA_PATH = "data/heart_disease.csv"

TARGET_COLUMN = "Heart Disease Status"


# ==========================================================
# Main Function
# ==========================================================

def audit_dataset():

    print_header(
        "Cardiac Risk Dataset Audit"
    )

    # ------------------------------------------------------
    # Create folders
    # ------------------------------------------------------

    create_directories()

    # ------------------------------------------------------
    # Load Original Dataset
    # ------------------------------------------------------

    df = load_data(DATA_PATH)

    # ------------------------------------------------------
    # Dataset Statistics
    # ------------------------------------------------------

    summary = dataset_overview(df)

    duplicates = duplicate_analysis(df)

    missing = missing_value_analysis(df)

    target = target_distribution(
        df,
        TARGET_COLUMN
    )

    numerical_statistics(df)

    categorical_statistics(df)

    # ------------------------------------------------------
    # Visualizations
    # ------------------------------------------------------

    plot_class_distribution(
        df,
        TARGET_COLUMN
    )

    plot_missing_values(
        missing
    )

    plot_histograms(df)

    plot_boxplots(df)

    plot_correlation_heatmap(df)

    # ------------------------------------------------------
    # Console Summary
    # ------------------------------------------------------

    print_header(
        "Audit Summary"
    )

    print(f"Rows              : {df.shape[0]}")

    print(f"Columns           : {df.shape[1]}")

    print(f"Duplicate Rows    : {duplicates}")

    print(
        f"Missing Columns   : "
        f"{(missing['Missing Values'] > 0).sum()}"
    )

    print(
        f"Target Classes    : "
        f"{len(target)}"
    )

    print_success(
        "EDA Completed Successfully."
    )

    print_success(
        "CSV files saved in results/csv/"
    )

    print_success(
        "Plots saved in results/plots/"
    )


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    audit_dataset()