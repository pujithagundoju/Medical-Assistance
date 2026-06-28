import shap
import matplotlib.pyplot as plt

def shap_bar_plot(shap_values, input_df):

    shap.summary_plot(
        shap_values,
        input_df,
        plot_type="bar",
        show=False
    )

    return plt.gcf()