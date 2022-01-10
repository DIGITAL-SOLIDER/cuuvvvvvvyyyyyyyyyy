import plotly.figure_factory as ff
import pandas as pd
import csv

dr=pd.read_csv("cl.csv")
fig=ff.create_distplot([dr["Avg Rating"].tolist()],["Mobile Brand"],show_hist=True)
fig.show()