import json 
import networkx as nx 
import matplotlib.pyplot as plt 
from networkx.readwrite import json_graph 

with open('graph.json') as source:
    data = json.load(source) 
G = json_graph.node_link_graph(data) 
coords = nx.spring_layout(G)  # layout
rank = nx.pagerank(G) # default damping

opt = { 'node_size': 500,
        'width': 3,
        'with_labels': True,
        'font_color': 'black',
        'edge_color': 'yellow' }

fig, ax = plt.subplots()
nx.draw(G,
        cmap = plt.get_cmap('Greens'), # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        node_color = [ rank[v] for v in G.nodes() ], **opt)
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.axis('off')
plt.savefig('rank.png')

# gonna add more stuff to this next week
