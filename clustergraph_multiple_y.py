import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join
import re

mypath = '../courses/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

i = 0
while (i < len(files)):
    #Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
    df = pd.read_csv(mypath+files[i], delim_whitespace=True)
    df.head()
    '''trace1 = go.Scatter(
                        x=df['CGV_Vehicle_Index'], y=df['CGV_Weight_Max_lbs'], # Data
                        mode='lines', name='MaxWeight' # Additional options
                    )'''
    #trace2 = go.Scatter(x=df['Time(sec)'], y=df['normalForce'], mode='styled-scatter', name='Wheel Size' )
    Horizontal = 'Time(sec)'
    Vertical1 = 'normalForce'
    Vertical2 = 'speed'

    trace3 = go.Scatter(x=df[Horizontal], y=df[Vertical1], mode='markers', marker=dict(
            size='4',
        ), showlegend=True)

    trace4 = go.Scatter(x=df[Horizontal], y=df[Vertical2], mode='markers', marker=dict(
            size='4',
        ), showlegend=True)

    layout = go.Layout(title=files[i], hovermode='closest', xaxis=dict(
            title= Horizontal,
            gridwidth= 2,
        ), yaxis=dict(
            title= Vertical1,
            gridwidth= 2,
        ), yaxis2=dict(
            title= Vertical2,
            gridwidth= 2,
            titlefont=dict(
                color='rgb(148,103,189)'
            ),
            tickfont=dict(
                color='rgb(148,103,189)'
            ),
            overlaying='y',
            side='right',
        ), plot_bgcolor='rgb(230, 230,230)')

    fig = go.Figure(data=[trace3, trace4], layout=layout)

    files[i] = re.sub('_Config.txt$', '', files[i])
    files[i] = re.sub('Ride_Course', 'C', files[i])
    files[i] = re.sub('Speed', 'S', files[i])

    # Plot data in the notebook
    py.offline.plot(fig, filename=files[i]+'.html', auto_open=False)

    i+=1
