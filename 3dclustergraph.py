import plotly as py
import pandas as pd
'''Change the file to whatever file you wish to graph'''
df = pd.read_csv('./data/data/output/model_output/testing3.csv')
df.head()
#Here you change your x, y, and z axis to what you wish to graph. I suggest leaving one of them as your tradebuilder design number so it can be easily identified'''
scatter = dict(
    mode = "markers",
    name = "y",
    type = "scatter3d",
    x = df['TradeBuilder_Design_Index'], y = df['CGV_Mercury_OUTPUT_SpeedLimit_Shock_2_5g_15pctdeflect_16in_mph'], z = df['CGV_Mercury_OUTPUT_MaxSpeed_mph'],
    marker = dict( size=2, color="rgb(23, 190, 207)" )
)
#These need to reflect your entries ofr x,y,and z from above. This will mess your smilular plots
clusters = dict(
    alphahull = 7,
    name = "y",
    opacity = 0.1,
    type = "mesh3d",
    x = df['TradeBuilder_Design_Index'], y = df['CGV_Mercury_OUTPUT_SpeedLimit_Shock_2_5g_15pctdeflect_16in_mph'], z = df['CGV_Mercury_OUTPUT_MaxSpeed_mph']
)
#You can change what your graph is called in the first title, and the name of your x, y, and z axis in the title inside the respective axis dict belowS
layout = dict(
    title = '3d point clustering of Speeds',
    scene = dict(
        xaxis = dict( zeroline=False, title= 'x = Design Number'),
        yaxis = dict( zeroline=False, title= 'y = SpeedLimit Shock'),
        zaxis = dict( zeroline=False, title= 'z = Max Speed'),
    )
)
fig = dict( data=[scatter, clusters], layout=layout )
# Use py.iplot() for IPython notebook
#change the name of your file below
py.offline.plot(fig, filename='3dpointclustering2')
