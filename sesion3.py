import networkx as nx
from math import log, floor 
from network2tikz import plot
from networkx.generators.classic import binomial_tree

levels = 50
colors = dict()
for v in range(levels + 1):
    high = 0.6
    low = 0.1
    active = v / (2 * levels)
    label = 'c' + str(v)
    start = '\\definecolor{' + label + '}{rgb}'
    if v % 3 == 0:
        end = '{' + f'{high:.2}' + ',' + f'{active:.2}' + ',' + f'{low:.2}' + '}'
    elif v % 3 == 1:
        end = '{' f'{active:.2}' + ',' + f'{low:.2}' + ',' + f'{high:.2}' + '}'        
    else:
        end = '{' + f'{low:.2}' + ', ' + f'{high:.2}' + ',' + f'{active:.2}' + '}'        
    colors[v] = start + end
    
def label(value):
    global levels
    return f'c{int(floor(value * levels))}'


G = binomial_tree(4)
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# hay que instalar graphviz
coords = graphviz_layout(G, prog = "dot") 

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
