class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes, self.adj = [], {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def length(self):
        return len(self.nodes)

    def traverse(self):
        return 'V: %s\nE: %s' % (self.nodes, self.adj)

    def __str__(self):
        return "".join(f"{node} -> {self.adj[node]}\n" for node in self.nodes)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []

    def add_edge(self, u, v):  # undirected unweighted graph
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return sum(len(l) for _, l in self.adj.items())


class DGraph(Graph):
    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v]


class WGraph(Graph):
    def __init__(self, nodes=None, edges=None):
        self.nodes, self.adj, self.weight = [], {}, {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def add_edge(self, u, v, w):
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]
        self.weight[(u, v)] = w
        self.weight[(v, u)] = w

    def get_weight(self, u, v):
        return self.weight[(u, v)]


class DWGraph(WGraph):
    def add_edge(self, u, v, w):
        self.adj[u] = self.adj.get(u, []) + [v]
        self.weight[(u, v)] = w

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.adj:
            return None
        for node in self.adj[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.adj:
            return None
        Shortest = None
        for node in self.adj[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath and (not Shortest or len(newpath) < len(Shortest)):
                    Shortest = newpath
        return Shortest


directedWeightedGraph = DWGraph()

graphNodes = ['A','B','C','D','E','F']
graphEdges =[('A', 'B', 2),('A', 'C', 1),('B', 'C', 2),('B', 'D', 5),('C', 'D', 1),('C', 'F', 3),('D', 'C', 1),('D', 'E', 4),('E', 'F', 3),('F', 'C', 1),('F', 'E', 2)]

for n in graphNodes:
    directedWeightedGraph.add_node(n)
for e in graphEdges:
    directedWeightedGraph.add_edge(e[0],e[1],e[2])

print(directedWeightedGraph)

print("\nPath is")
print(directedWeightedGraph.find_path('A', 'D'))
print("\nShortest Path is")
print(directedWeightedGraph.find_shortest_path('A', 'D'))