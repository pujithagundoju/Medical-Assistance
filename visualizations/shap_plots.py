# import shap
# import matplotlib.pyplot as plt

# def shap_bar_plot(shap_values, input_df):

#     shap.summary_plot(
#         shap_values,
#         input_df,
#         plot_type="bar",
#         show=False
#     )

#     return plt.gcf()
import matplotlib.pyplot as plt

def shap_bar_plot(shap_df):

    plt.figure(figsize=(8,6))

    shap_df = shap_df.sort_values(
        by="Impact",
        ascending=True
    )

    colors = [
        "green" if x < 0 else "red"
        for x in shap_df["SHAP_Value"]
    ]

    plt.barh(
        shap_df["Feature"],
        shap_df["SHAP_Value"],
        color=colors
    )

    plt.xlabel("SHAP Value")
    plt.ylabel("Feature")
    plt.title("SHAP Feature Importance")

    plt.tight_layout()

    return plt.gcf()