import plotly.express as px
import pandas as pd

df = pd.read_csv("returns1020.csv")
df["Date"] = pd.to_datetime(df["Date"])

df = df.set_index("Date").stack().reset_index().rename(columns={"level_1":"Returns", 0:"Value"})

fig = px.area(df, x='Date', y='Value', color='Returns')

fig.update_layout(title='Daily Returns of GSPC and FTSI', xaxis_title='Date', yaxis_title='Returns')

fig.show()