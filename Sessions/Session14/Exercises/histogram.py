import plotly.express as px
import pandas as pd

df = pd.read_csv("histogram_data.csv")

fig = px.histogram(df, x='Price', nbins=15)

fig.show()