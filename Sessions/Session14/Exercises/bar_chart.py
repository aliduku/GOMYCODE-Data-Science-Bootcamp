import plotly.express as px
import pandas as pd

df = pd.read_csv("bar_chart_homework_data.csv")

fig = px.bar(df, x="Cities", y="Frequency", color="Cities", height=400)
fig.update_layout(title_text="frequency of the cities", xaxis_title="Cities", yaxis_title="Frequency")

fig.show()