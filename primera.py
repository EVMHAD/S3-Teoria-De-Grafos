import json # for file IO
import networkx as nx # for the graphs
from random import randint # for pseudorandomness
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

output =  json_graph.node_link_data(G)
with open('graph.json', 'w') as target:
    json.dump(output, target) # write to file

with open('graph.json') as source:
    data = json.load(source) # read it back
stored = json_graph.node_link_graph(data) 

# set some options for the drawing
opt = { 'node_color': 'green',
        'node_size': 500,
        'width': 3,
        'with_labels': True }
nx.draw(stored, **opt) # create the drawing
plt.show() # open a window with it
plt.savefig('graph.png') # export it as an image file
