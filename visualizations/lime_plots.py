from lime.lime_tabular import LimeTabularExplainer

def create_lime_explainer(X_train):

    return LimeTabularExplainer(
        training_data=X_train.values,
        feature_names=X_train.columns,
        mode="classification"
    )