from sklearn.preprocessing import LabelEncoder

def clean_data(df):

    df = df.copy()

    df.fillna(df.median(numeric_only=True), inplace=True)

    categorical_cols = df.select_dtypes(include=["object"]).columns

    encoders = {}

    for col in categorical_cols:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(df[col].astype(str))

        encoders[col] = encoder

    return df, encoders