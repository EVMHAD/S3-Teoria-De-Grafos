import json 
import networkx as nx
from math import floor # round down
from network2tikz import plot
from networkx.readwrite import json_graph 

levels = 12
colors = dict()
for v in range(levels + 1):
    label = 'c' + str(v)
    start = '\\definecolor{' + label + '}{rgb}'
    end = '{0.5, ' + f'{0.5 + v / (levels / 2):.2}' + ', 0.5}' 
    colors[v] = start + end

def label(value):
    global levels
    return f'c{int(floor(value * levels))}'

with open('graph.json') as source:
    data = json.load(source) 
G = json_graph.node_link_graph(data) 
coords = nx.kamada_kawai_layout(G, scale = 3) # another layout

# normalize this to [0, 1] so that the colors look different
rank = nx.pagerank(G) 
low = min(rank.values())
high = max(rank.values())
span = high - low
for v in rank:
    rank[v] = (rank[v] - low) / span

style = {}
style['node_label'] = [  str(v) for v in G.nodes() ]
style['node_color'] = [ label(rank[v]) for v in G.nodes() ] 
style['node_opacity'] = 0.9
style['edge_curved'] = 0.2

plot( (G.nodes(), G.edges()), 'temp.tex', **style)

# we need to add the palette definitions to the LaTeX source
with open('graph.tex', 'w') as target:
    with open('temp.tex') as source:
        print(source.readline().strip(), file = target) # \documentclass{standalone}
        print(source.readline().strip(), file = target) # \usepackage{tikz-network}
        for color in colors.values():
            print(color, file = target)
        for line in source: # the rest of it
            print(line.strip(), file = target)
