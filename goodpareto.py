import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
#Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
df = pd.read_csv('4_ERS_Table_LRV_976_Results_Rank_Score_Cost_Cluster10.csv')
df.head()
def pareto_frontier(Xs, Ys, maxX = False, maxY = True):
# Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
# Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]
# Loop through the sorted list
    for pair in myList[1:]:
        if maxY:
            if pair[1] >= p_front[-1][1]: # Look for higher values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
        else:
            if pair[1] <= p_front[-1][1]: # Look for lower values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
# Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    return p_frontX, p_frontY

trace3 = go.Scatter(x=df['Survivability_Model_Survivability_score'], y=df['CM_OUTPUT_Total_LCC'], mode='markers', marker=dict(
        size='16',
        color = df['CGV_Mercury_OUTPUT_MaxSpeed_mph'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    ), text=df['TradeBuilder_Design_Index'], hoverinfo='text',showlegend=False)
p_front = pareto_frontier(df['Survivability_Model_Survivability_score'],df['CM_OUTPUT_Total_LCC'])

trace4 = go.Scatter(x=p_front[0], y=p_front[1], mode='lines', showlegend=False)
layout = go.Layout(title='Survivablility Score vs Cost', hovermode='closest', xaxis=dict(
        title= 'Survivablility Score',
        gridwidth= 2,
    ), yaxis=dict(
        title= 'Cost',
        gridwidth= 2,
    ), plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace3, trace4], layout=layout)

# Plot data in the notebook
py.offline.plot(fig, filename='showtest')
