import lime
import lime.lime_tabular

def build_lime_explainer(model, X_train, feature_names):
    
    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=X_train,
        feature_names=feature_names,
        class_names=["Low Risk", "High Risk"],
        mode="classification"
    )

    return explainer