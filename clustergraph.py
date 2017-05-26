import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join
import re

mypath = '../../courses/'

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
    #trace2 = go.Scatter(x=df['TradeBuilder_Design_Index'], y=df['CGV_CG_Longitudinal_WRT_FrontAxle_in'], mode='styled-scatter', name='Wheel Size' )
    Horizontal = 'Time(sec)'
    Vertical = 'Time(sec)'
    trace3 = go.Scatter(x=df[Horizontal], y=df[Vertical], mode='markers', marker=dict(
            size='4',
            colorscale='Viridis',
            showscale=False
        ), name='Time vs Normal Force', showlegend=False)

    layout = go.Layout(title=files[i], hovermode='closest', xaxis=dict(
            title= Horizontal,
            gridwidth= 2,
        ), yaxis=dict(
            title= Vertical,
            gridwidth= 2,
        ), plot_bgcolor='rgb(230, 230,230)')

    fig = go.Figure(data=[trace3], layout=layout)

    files[i] = re.sub('_Config.txt$', '', files[i])
    files[i] = re.sub('Ride_Course', 'C', files[i])
    files[i] = re.sub('Speed', 'S', files[i])

    # Plot data in the notebook
    py.offline.plot(fig, filename=files[i]+'.html', auto_open=False)

    i+=1
