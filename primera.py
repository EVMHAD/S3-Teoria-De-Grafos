import json # for file IO
import networkx as nx # for the graphs
from random import randint # pseudo-randomness
from celluloid import Camera # creating animations
import matplotlib.pyplot as plt # for the drawings
from networkx.readwrite import json_graph # for output

G = nx.Graph() # simple undirected graph
n = 7 # graph order (= number of vertices)
m = 2 * n # graph size (= number of edges)

G.add_nodes_from(range(1, n + 1)) # add vertices 1, 2, ..., n

while len(G.edges) < m: # add edges until the goal size is reached
    v = randint(1, n) # pick a vertex uniformly at random
    u = randint(1, n) # pick another
    if v != u: # if they differ, add it
        G.add_edge(v, u) # unit weight by default

# set some options for the drawing
opt = { 'node_color': 'green',
        'node_size': 500,
        'width': 3,
        'with_labels': True }
coords = nx.spring_layout(G) # fix the positions
nx.draw(G, pos = coords, **opt) # create a drawing
plt.savefig('graph.png') # export it as an image file
plt.show() # open a window with it

        
output =  json_graph.node_link_data(G)
with open('graph.json', 'w') as target:
    json.dump(output, target) # write to file

with open('graph.json') as source:
    data = json.load(source) # read it back
G = json_graph.node_link_graph(data) # overwrite

fig = plt.figure() # make a new figure to animate
cam = Camera(fig) # for storing the frames
opt = { 'node_size': 500,
        'width': 3,
        'with_labels': True }
palette = ['green'] * n # make all green
for v in range(n):
    palette[v] = 'yellow' # highlight in yellow
    nx.draw(G, pos = coords, node_color = palette,  **opt)
    cam.snap() # take a snapshot
    palette[v] = 'gray' # make the 'used' ones blue
nx.draw(G, pos = coords, node_color = palette,  **opt)
cam.snap() # last frame all gray
gif = cam.animate(interval = 500, # milliseconds between frames
                  repeat = False) # do NOT loop (this is actually bugged)
gif.save('graph.gif', writer = 'imagemagick')
