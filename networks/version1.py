# create weighted network

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from sqlalchemy.engine import create_engine

from pandas import DataFrame
import time
import datetime
timestr = time.strftime("%Y%m%d")

import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()
import json
#import plotly.graph_objects as go
import plotly.graph_objs as go
pd.options.display.max_rows = 999

import networkx as nx

#################

data = [[1, 2, 5], [1, 3, 12], [2, 4, 7]] 
df = pd.DataFrame(data, columns = ['source', 'target', 'weight']) 

tuples = [tuple(x) for x in df.values]

G = nx.Graph()   
G.add_weighted_edges_from(tuples)
pos = nx.fruchterman_reingold_layout(G)
label = []
for node in pos:
    label.append(str(node))

    edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]

nx.set_node_attributes(G, pos, 'pos')

# create node dictionary
node_dict = {}
for i, j in enumerate(G.nodes):
    node_dict[j] = i

# get node positions
node_positions = []
for node in G.nodes():
    node_positions.append(list(G.node[node]['pos']))
node_positions = np.asarray(node_positions)

# get edges list
final_edges_list = []
for edge in G.edges:
    if edge[0] in node_dict:
        if edge[1] in node_dict:
            final_edges_list.append((node_dict[edge[0]], node_dict[edge[1]]))
final_edges_list = np.asarray(final_edges_list)

nodes = dict(type='scatter',
           x=node_positions[:,0],
           y=node_positions[:,1],
           mode = 'markers+text',
           textposition="top center",
           text = label,
           hoverinfo = 'text',
           marker=dict(size=15, color='black', opacity=0.75))

edges_list= [dict(type='scatter',
             x=[node_positions[e[0]][0], node_positions[e[1]][0]],
             y=[node_positions[e[0]][1], node_positions[e[1]][1]],
             mode='lines',
             line=dict(color = "grey", width=weights[k]), opacity=0.5)  for k, e in enumerate(final_edges_list)]

data = edges_list + [nodes]

fig = go.Figure(data = dict(data=data),
             layout=go.Layout())

fig.update_layout(showlegend = False,
                  plot_bgcolor = 'rgba(0,0,0,0)',
                  paper_bgcolor='rgba(0,0,0,0)',
                  hovermode='closest',
                  margin=dict(b=20,l=5,r=5,t=40),
                  xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                  yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
fig.show()
