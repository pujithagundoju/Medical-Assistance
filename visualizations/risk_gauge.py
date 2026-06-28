import plotly.graph_objects as go

def create_gauge(probability):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={"text": "Heart Disease Risk"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    return fig