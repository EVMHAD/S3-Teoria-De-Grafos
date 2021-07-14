from math import log
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import powerlaw_cluster_graph
from networkx.algorithms.centrality import edge_betweenness_centrality

plt.rcParams["figure.figsize"] = (15, 15)

G = powerlaw_cluster_graph(30, 3, 0.05)
coords = nx.spectral_layout(G)  # a different layout this time
rank = nx.pagerank(G) # default damping
print(list(rank.items())[:3])

# normalize to [0, 1] and logscale
low = min(rank.values())
high = max(rank.values())
span = high - low
rank = [ log((rank[v] - low) / span + 1) for v in G.nodes() ]

opt = { 'node_size': 800,
        'width': 3,
        'with_labels': True,
        'font_color': 'black',
        'edge_color': 'orange' }

fig, ax = plt.subplots()
nx.draw(G,
        pos = coords,
        cmap = plt.get_cmap('Greens'), # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        node_color = [ rank[v] for v in G.nodes() ], **opt)
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.axis('off')
plt.savefig('rank.png')

centrality = edge_betweenness_centrality(G)
print(list(centrality.items())[:3])
 
# normalize to [0, 1]
low = min(centrality.values())
high = max(centrality.values())
span = high - low
weight = [(centrality[e] - low) / span for e in G.edges()]

del opt['width'] # discard the constants
width = 10 # set a maximum
del opt['edge_color']
fig, ax = plt.subplots()
nx.draw(G,
        pos = coords,        
        cmap = plt.get_cmap('Greens'),
        edge_cmap = plt.get_cmap('Oranges'),
        node_color = rank,
        edge_color = weight,
        width = [width * w for w in weight] ,
        **opt)
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.axis('off')
plt.savefig('centrality.png')



