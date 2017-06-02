import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join
import re

mypath = '../courses/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

t=[]
l=[]

print(range(len(files)))

for i in range(len(files)):
    #Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
    df = pd.read_csv(mypath+files[i], error_bad_lines=False,  delim_whitespace=True)
    df.head()
    '''trace1 = go.Scatter(
                        x=df['CGV_Vehicle_Index'], y=df['CGV_Weight_Max_lbs'], # Data
                        mode='lines', name='MaxWeight' # Additional options
                    )'''
    #trace2 = go.Scatter(x=df['Time(sec)'], y=df['normalForce'], mode='styled-scatter', name='Wheel Size' )
    Horizontal = 'Time(sec)'
    Vertical = 'normalForce'
    trace3 = go.Scattergl(x=df[Horizontal], y=df[Vertical], mode='markers', marker=dict(
            size='4',
        ), name=files[i], showlegend=True, visible="legendonly")
    
    t.append(trace3)

layout = go.Layout(title=files[i], hovermode='closest', xaxis=dict(
    title= Horizontal,
           gridwidth= 2,
       ), yaxis=dict(
           title= Vertical,
           gridwidth= 2,
       ),)
    
    #l.append(layout)

fig = go.Figure(data=t, layout=layout)

    #files[i] = re.sub('_Config.txt$', '', files[i])
    #files[i] = re.sub('Ride_Course', 'C', files[i])
    #files[i] = re.sub('Speed', 'S', files[i])

    # Plot data in the notebook
py.offline.plot(fig, filename='test.html', auto_open=False)

