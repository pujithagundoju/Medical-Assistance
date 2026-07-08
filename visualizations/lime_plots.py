# from lime.lime_tabular import LimeTabularExplainer

# def create_lime_explainer(X_train):

#     return LimeTabularExplainer(
#         training_data=X_train.values,
#         feature_names=X_train.columns,
#         mode="classification"
#     )
import matplotlib.pyplot as plt

def lime_bar_plot(lime_df):

    plt.figure(figsize=(8,6))

    lime_df = lime_df.sort_values(
        by="Contribution",
        ascending=True
    )

    colors = [
        "green" if x < 0 else "red"
        for x in lime_df["Contribution"]
    ]

    plt.barh(
        lime_df["Feature"],
        lime_df["Contribution"],
        color=colors
    )

    plt.xlabel("Contribution")
    plt.ylabel("Feature")
    plt.title("LIME Feature Importance")

    plt.tight_layout()

    return plt.gcf()