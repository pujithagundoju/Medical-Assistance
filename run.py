import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

# Load dataset
X, y = load_breast_cancer(return_X_y=True)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Create explainer
explainer = shap.Explainer(model)

# Compute SHAP values
shap_values = explainer(X)

# -----------------------------
# Beeswarm Plot
# -----------------------------
shap.plots.beeswarm(
    shap_values[:, :, 1],
    max_display=10,
    show=False
)

plt.savefig("shap_beeswarm.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# Bar Plot
# -----------------------------
shap.plots.bar(
    shap_values[:, :, 1],
    max_display=10,
    show=False
)

plt.savefig("shap_bar.png", dpi=300, bbox_inches="tight")
plt.show()
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt

lime_explainer = LimeTabularExplainer(
    training_data=X_train.values,
    feature_names=X.columns.tolist(),
    class_names=["Low Risk", "High Risk"],
    mode="classification"
)

sample_index = 0

exp = lime_explainer.explain_instance(
    X_test.iloc[sample_index].values,
    model.predict_proba,
    num_features=10
)

fig = exp.as_pyplot_figure()

fig.savefig(
    "figures/chapter8/figure8_5_lime.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)