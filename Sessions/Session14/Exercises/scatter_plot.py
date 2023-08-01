import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv("scatter_data.csv")

trace = go.Scatter(x=df['Area (ft.)'], y=df['Price'], mode='markers', marker=dict(color=df['Building Type']))

data = [trace]

layout = go.Layout(title='Year of Sale vs. Price', xaxis=dict(title='Year of sale'), yaxis=dict(title='Price'))

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)