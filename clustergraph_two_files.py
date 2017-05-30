import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go

file1='Ride_Course0_Speed11_Config.txt'
file2='Ride_Course24_Speed5_Config.txt'

#Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
df = pd.read_csv('../courses/Ride_Course0_Speed11_Config.txt', delim_whitespace=True)
df.head()

Horizontal = 'Time(sec)'
Vertical = 'normalForce'

trace1 = go.Scatter(x=df[Horizontal], y=df[Vertical], mode='markers', marker=dict(
        size='4',
    ), name=Vertical+'1 vs '+Horizontal, showlegend=True)

df2 = pd.read_csv('../courses/Ride_Course24_Speed5_Config.txt', delim_whitespace=True)
df2.head()

trace2 = go.Scatter(x=df2[Horizontal], y=df2[Vertical], mode='markers', marker=dict(
        size='4',
    ), name=Vertical+'2 vs '+Horizontal, showlegend=True)

layout = go.Layout(title='Title', hovermode='closest', xaxis=dict(
        title= Horizontal,
        gridwidth= 2,
    ), yaxis=dict(
        title= Vertical+'1',
        gridwidth= 2,
    ), plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2], layout=layout)

# Plot data in the notebook
py.offline.plot(fig, filename='versus.html', auto_open=False)
