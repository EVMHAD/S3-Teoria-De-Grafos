import json 
import networkx as nx
from math import log, floor 
from network2tikz import plot
from networkx.readwrite import json_graph 

levels = 256
colors = dict()
for v in range(levels + 1):
    label = 'c' + str(v)
    start = '\\definecolor{' + label + '}{rgb}'
    end = '{0.8, ' + f'{0.5 + v / (2 * levels):.2}' + ', 0.2}' 
    colors[v] = start + end

def label(value):
    global levels
    return f'c{int(floor(value * levels))}'

with open('graph.json') as source:
    data = json.load(source) 
G = json_graph.node_link_graph(data) 
coords = nx.kamada_kawai_layout(G, scale = 3) # another layout

rank = nx.pagerank(G) 
low = min(rank.values())
high = max(rank.values())
span = high - low
if span > 0:
    for v in rank:
        rank[v] = log((rank[v] - low) / span + 1)

opt = {}
opt['node_label'] = [ f'N{v}' for v in G.nodes() ]
opt['node_color'] = [ label(rank[v]) for v in G.nodes() ] 
opt['node_opacity'] = 0.95
opt['edge_curved'] = 0.8

plot( (G.nodes(), G.edges()), 'temp.tex', **opt)

# we need to add the palette definitions to the LaTeX source
with open('graph.tex', 'w') as target:
    with open('temp.tex') as source:
        print(source.readline().strip(), file = target) # \documentclass{standalone}
        print(source.readline().strip(), file = target) # \usepackage{tikz-network}
        for color in colors.values(): # PUT THE COLORS
            print(color, file = target)
        for line in source: # the rest of it
            print(line.strip(), file = target)
