import plotly.express as px
import pandas as pd

df = pd.read_csv("returns1020.csv")
df["Date"] = pd.to_datetime(df["Date"])

fig = px.line(df, x='Date', y=['GSPCRet', 'FTSERet'])
fig.update_layout(title='Daily Returns of GSPC and FTSI', xaxis_title='Date', yaxis_title='Returns')

fig.show()