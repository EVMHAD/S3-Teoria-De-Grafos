import networkx as nx # for the graphs
from random import randint # pseudo-randomness

G = nx.Graph() # simple undirected graph
n = 12 # graph order (= number of vertices)
m = int(round(2.5 * n)) # graph size (= number of edges)

G.add_nodes_from(range(1, n + 1)) # add vertices 1, 2, ..., n

while len(G.edges) < m: # add edges until the goal size is reached
    v = randint(1, n) # pick a vertex uniformly at random
    u = randint(1, n) # pick another
    if v != u: # if they differ, add it
        G.add_edge(v, u) # unit weight by default

# print('grafo', G.nodes(), G.edges())

import matplotlib.pyplot as plt # for the drawings

opt = { 'node_color': 'orange',
        'node_size': 2500,
        'width': 6,
        'with_labels': True }
coords = nx.spring_layout(G) # fix the positions
nx.draw(G, pos = coords, **opt) # create a drawing
plt.savefig("sesion1.png")

import json # for file IO
from networkx.readwrite import json_graph # for output

output = json_graph.node_link_data(G)
with open('graph.json', 'w') as target:
    json.dump(output, target) # write to file

from celluloid import Camera # creating animations
    
fig = plt.figure() # make a new figure to animate
cam = Camera(fig) # for storing the frames
opt = { 'node_size': 2000,
        'width': 4,
        'with_labels': True }
palette = ['green'] * n # make all green
for v in range(n):
    palette[v] = 'yellow' # highlight in yellow
    nx.draw(G, pos = coords, node_color = palette,  **opt)
    cam.snap() # take a snapshot
    palette[v] = 'blue' # make the 'used' ones blue
nx.draw(G, pos = coords, node_color = palette,  **opt)
cam.snap() # last frame all blue
gif = cam.animate(interval = 100, # milliseconds between frames
                  repeat = True) 
gif.save('tmp.gif', writer = 'imagemagick')

