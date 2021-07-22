from math import log
import networkx as nx
import matplotlib.pyplot as plt
from random import choice # pseudo-randomness
from celluloid import Camera # creating animations
from networkx.generators.random_graphs import powerlaw_cluster_graph
from networkx.algorithms.centrality import edge_betweenness_centrality

plt.rcParams["figure.figsize"] = (12, 12)
opt = { 'with_labels': False,
        'edgecolors': 'orange',
        'font_color': 'black' }

G = powerlaw_cluster_graph(40, 2, 0.02)
coords = nx.circular_layout(G) # this is a dictionary
fig, ax = plt.subplots()
cam = Camera(fig) 
current = choice(list(G.nodes())) # start at a random vertex
lw = { v : 0 for v in G.nodes() } # outline widths for nodes
step = 0
while True:
    step += 1
    neighbors = list(G.neighbors(current))
    if len(neighbors) == 0:
        break # nowhere to go
    neighbor = choice(neighbors)
    # update the rankings
    pr = nx.pagerank(G) # rank the vertices
    low = min(pr.values())
    high = max(pr.values())
    span = high - low
    if span > 0: # normalize if not constant
        pr = { v: (pr[v] - low) / span for v in G.nodes() } 
    eb = edge_betweenness_centrality(G) # rank the edges
    low = min(eb.values())
    high = max(eb.values())
    span = high - low
    if span > 0: # normalize if not constant
        eb = { e : (eb[e] - low) / span for e in G.edges() } 
    nc = [ log(pr.get(v, 1) + 1) for v in G.nodes() ] # node colors
    ns = [ 800 * pr.get(v, 1) + 300 for v in G.nodes() ] # node sizes
    ec = [ eb.get(e, 1) for e in G.edges() ] # edge colors
    ew = [ (5 * eb.get(e, 0) + 1 if (e != (current, neighbor) and e != (neighbor, current)) else 12) for e in G.edges() ] # edge widths
    lw[current] = 10 # from 
    lw[neighbor] = 5 # to
    nx.draw(G, pos = coords,
            cmap = plt.get_cmap('Greens'), edge_cmap = plt.get_cmap('Blues'),
            linewidths = [ lw[v] for v in G.nodes() ],
            node_color = nc, 
            node_size = ns, 
            edge_color = ec,
            width = ew,
            **opt)
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    ax.axis('off')
    ax.text(-0.9, 0.9, f'Step {step}', color = 'white')
    cam.snap() # take a snapshot
    G.remove_node(current) # remove the visited vertex
    lw[current] = 0 # will not be drawn anymore
    current = neighbor

gif = cam.animate(interval = 800, repeat = True) 
gif.save('sesion2b.gif', writer = 'imagemagick')
