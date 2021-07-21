from math import log
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import powerlaw_cluster_graph
from networkx.algorithms.centrality import edge_betweenness_centrality

plt.rcParams["figure.figsize"] = (15, 15)

G = powerlaw_cluster_graph(30, 3, 0.05)
coords = nx.circular_layout(G)
rank = nx.pagerank(G) # default damping

# normalize to [0, 1] and logscale
low = min(rank.values())
high = max(rank.values())
span = high - low
rank = [ (rank[v] - low) / span for v in G.nodes() ]
logrank = [ log(rank[v] + 1) for v in G.nodes() ]
rank = [ 1200 * v + 300 for v in rank]

opt = { 'with_labels': True,
        'font_color': 'black' }

centrality = edge_betweenness_centrality(G)
low = min(centrality.values())
high = max(centrality.values())
span = high - low
weight = [(centrality[e] - low) / span for e in G.edges()]

from random import choice # pseudo-randomness
from celluloid import Camera # creating animations

fig, ax = plt.subplots()
cam = Camera(fig) # for storing the frames

current = choice(list(G.nodes()))

for paso in range(12):
    neighbor = choice(list(G.neighbors(current)))
    nx.draw(G,
            pos = coords,        
            cmap = plt.get_cmap('Greens'),
            edge_cmap = plt.get_cmap('Oranges'),
            node_color = logrank,
            node_size = rank,
            edge_color = weight,
            width = [12 * w + 1 for w in weight] ,
            **opt)
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    ax.axis('off')
    print(current, neighbor)
    cam.snap() # take a snapshot
    rank[current] = 0
    rank[neighbor] = 0
    current = neighbor
cam.snap() # take a snapshot
print('listo')

gif = cam.animate(interval = 200, # milliseconds between frames
                  repeat = True) 
gif.save('tmp.gif', writer = 'imagemagick')
