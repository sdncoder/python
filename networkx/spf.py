import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path

G = nx.Graph()

G.add_edge('j', 'l', weight=10)
G.add_edge('j', 't', weight=10)
G.add_edge('j', 'd', weight=10)
G.add_edge('l', 'd', weight=10)
G.add_edge('l', 't', weight=10)
G.add_edge('l', 'h', weight=10)
G.add_edge('h', 'a', weight=10)
G.add_edge('h', 'g', weight=10)
G.add_edge('a', 't', weight=10)
G.add_edge('t', 'd', weight=10)
G.add_edge('a', 'c', weight=10)
G.add_edge('d', 'c', weight=10)
G.add_edge('c', 'g', weight=10)
G.add_edge('c', 'y', weight=10)
G.add_edge('g', 'r', weight=10)
G.add_edge('g', 'm', weight=10)
G.add_edge('g', 'y', weight=10)
G.add_edge('m', 'y', weight=10)
G.add_edge('y', 'r', weight=10)
G.add_edge('y', 's', weight=10)
G.add_edge('s', 'r', weight=10)


#elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
#esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# edges
nx.draw_networkx_edges(G, pos, width=2)
#nx.draw_networkx_edges(G, pos, edgelist=esmall,
    #                   width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
paths = list(nx.shortest_path(G, 'j', 'r'))
#flow = shortest_augmenting_path(G, 'j', 'r', capacity = 5)
print(paths)
#print(flow)
plt.axis('off')
plt.show()
