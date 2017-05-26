import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
#Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
df = pd.read_csv('./data/data/output/model_output/4_ERS_Table_LRV_976_Results_Rank_Score_Cost_Cluster10.csv')
df.head()
#Boxmean = True for just show the mean, boxmean = 'sd' for mean and standard deviation, or delete boxmean for neither
trace0 = go.Box(
    y=df['Survivability_Model_Survivability_score'],
    name = 'Survivability Score',
    boxpoints='all',
    jitter=0.3,
    pointpos=0,
    marker = dict(
        color = 'rgb(214, 12, 140)',
    ),
    boxmean='sd'
)
trace1 = go.Box(
    y=df['NORMALIZED_Transport_Model_Transportability_score'],
    boxpoints='all',
    jitter=0.3,
    pointpos=0,
    name = 'Transport Score',
    marker = dict(
        color = 'rgb(0, 128, 128)',
    ), boxmean=True
)
data = [trace0, trace1]
py.offline.plot(data,filename='boxplot')
