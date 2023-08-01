import plotly.express as px
import pandas as pd

df = pd.read_csv("bar_chart_homework_data.csv")

fig = px.pie(df, values="Frequency", names='Cities', color='Cities', title='frequency of the cities')
fig.update_traces(textposition='inside', textinfo='percent+label')

fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')

fig.show()