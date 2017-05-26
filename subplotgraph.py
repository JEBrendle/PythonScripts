import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
#Markers for scatter, lines for lines, lines+markers for line and markers, styled-scatter for cool bubbles
df = pd.read_csv('./data/data/output/model_output/4_ERS_Table_LRV_976_Results_Rank_Score_Cost_Cluster10.csv')
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

trace1 = go.Scatter(x=df['Survivability_Model_Survivability_score'], y=df['CM_OUTPUT_Total_LCC'], mode='markers', marker=dict(
        size='16',
        color = df['CM_OUTPUT_Total_LCC'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    ), text=df['TradeBuilder_Design_Index'], hoverinfo='text')
trace2 = go.Scatter(x=df['NORMALIZED_Transport_Model_Transportability_score'], y=df['CM_OUTPUT_Total_LCC'], mode='markers', marker=dict(
        size='16',
        color = df['CM_OUTPUT_Total_LCC'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    ), text=df['TradeBuilder_Design_Index'], hoverinfo='text')
trace3 = go.Scatter(x=df['NORMALIZED_CrewEff_Model_Crew_Effectiveness_score'], y=df['CM_OUTPUT_Total_LCC'], mode='markers', marker=dict(
        size='16',
        color = df['CM_OUTPUT_Total_LCC'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    ), text=df['TradeBuilder_Design_Index'], hoverinfo='text')
trace4 = go.Scatter(x=df['NORMALIZED_Stealth_Model_Silhouette_Averages_Total_ft2'], y=df['CM_OUTPUT_Total_LCC'], mode='markers', marker=dict(
        size='16',
        color = df['CM_OUTPUT_Total_LCC'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    ), text=df['TradeBuilder_Design_Index'], hoverinfo='text')

p_front1 = pareto_frontier(df['Survivability_Model_Survivability_score'],df['CM_OUTPUT_Total_LCC'])
pf1 = go.Scatter(x=p_front1[0], y=p_front1[1], mode='lines')

p_front2 = pareto_frontier(df['NORMALIZED_Transport_Model_Transportability_score'],df['CM_OUTPUT_Total_LCC'])
pf2 = go.Scatter(x=p_front2[0], y=p_front2[1], mode='lines')

p_front3 = pareto_frontier(df['NORMALIZED_CrewEff_Model_Crew_Effectiveness_score'],df['CM_OUTPUT_Total_LCC'])
pf3 = go.Scatter(x=p_front3[0], y=p_front3[1], mode='lines')

p_front4 = pareto_frontier(df['NORMALIZED_Stealth_Model_Silhouette_Averages_Total_ft2'],df['CM_OUTPUT_Total_LCC'])
pf4 = go.Scatter(x=p_front4[0], y=p_front4[1], mode='lines')


fig = py.tools.make_subplots(rows=2, cols=2, subplot_titles=('SurvivabilityvsCost', 'TrnasportvsCost',
                                                          'CrewvsCost', 'StealthvsCost'))
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)
fig.append_trace(pf1, 1, 1)
fig.append_trace(pf2, 1, 2)
fig.append_trace(pf3, 2, 1)
fig.append_trace(pf4, 2, 2)
# Plot data in the notebook

fig['layout']['xaxis1'].update(title='Survivability')
fig['layout']['xaxis2'].update(title='Transport')
fig['layout']['xaxis3'].update(title='Crew')
fig['layout']['xaxis4'].update(title='Stealth')

fig['layout']['yaxis1'].update(title='Cost')
fig['layout']['yaxis2'].update(title='Cost')
fig['layout']['yaxis3'].update(title='Cost')
fig['layout']['yaxis4'].update(title='Cost')
py.offline.plot(fig, filename='subplot')
