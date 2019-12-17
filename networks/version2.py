# unweighted network

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from sqlalchemy.engine import create_engine

from pandas import DataFrame
import time
import datetime

import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()
import json

import plotly.graph_objs as go
pd.options.display.max_rows = 999

import networkx as nx
************-

data = [['x1', 'y1', 'z1'], ['x1', 'y1', 'z2'], ['x2', 'y2', 'z3'], ['x2', 'y1', 'z2']] 
df1 = pd.DataFrame(data, columns = ['node1', 'intermediary', 'node2']) 

edges_1 = df1[["node1", "intermediary"]].apply(tuple, axis = 1).tolist()
edges_2 = df1[["intermediary", "node2"]].apply(tuple, axis = 1).tolist()

# http://datanongrata.com/2019/06/12/plotting-networkx-plots-in-plot-ly-dolphins-part-2/


G = nx.Graph()

G.add_edges_from(edges_1)
G.add_edges_from(edges_2)

# layouts
#pos = nx.circular_layout(G)
#pos = nx.spring_layout(G)
pos = nx.fruchterman_reingold_layout(G)
#pos = nx.shell_layout(G)


nx.set_node_attributes(G, pos, 'pos')

node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers+text',
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        showscale=False,
        reversescale=True,
        color="orange",
        size=20,
        line = dict(width = 0)))

for node in G.nodes():
    x, y = G.node[node]['pos']
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    node_trace["text"] += tuple([node])
    
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

    
for edge in G.edges():
    x0, y0 = G.node[edge[0]]['pos']
    x1, y1 = G.node[edge[1]]['pos']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])
    
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                #titlefont_size=16,
                showlegend=False,
                plot_bgcolor = 'rgba(0,0,0,0)',
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()

# plotly.offline.plot(fig, filename='test.html')  
# periscope.plotly(go.Figure(data = [fig], layout=layout))
