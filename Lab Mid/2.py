# To import package
import networkx

# To create an empty undirected graph
G = networkx.Graph()


nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
edges = [(0, 1),(0, 8),(0, 3),(3, 2),(8, 4),(4, 3),(2, 7),(7, 1),(2, 5),(5, 6)]

for n in nodes:
    G.add_node(n)

for u,v in edges:
    G.add_edge(u,v)


# To get all the nodes of a graph
node_list = G.nodes()
print("#1")
print(node_list)

# To get all the edges of a graph
edge_list = G.edges()
print("#2")
print(edge_list)
