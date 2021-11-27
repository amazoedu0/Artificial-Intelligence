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
        string = ""
        for node in self.nodes:
            string += f"{node} -> {self.adj[node]}\n"
        return string
        
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
        self.pathCost=0
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
    
    def find_shortest_path(self, start, end, path=[],cost=0):
        path = path + [start]
        if start == end:
            self.pathCost=cost
            return path,cost
        if start not in self.adj:
            return None,cost
        for node in self.adj[start]:
            if node not in path:
                cost=cost+self.get_weight(start,node)
                newpath = self.find_shortest_path(node, end, path,cost)
                if newpath:
                    return newpath
        return None,cost


directedWeightedGraph = DWGraph()
directedWeightedGraph.add_node('A')
directedWeightedGraph.add_node('B')
directedWeightedGraph.add_node('C')
directedWeightedGraph.add_node('D')
directedWeightedGraph.add_node('E')
directedWeightedGraph.add_node('F')
directedWeightedGraph.add_edge('A', 'B', 2)
directedWeightedGraph.add_edge('A', 'C', 1)
directedWeightedGraph.add_edge('B', 'C', 2)
directedWeightedGraph.add_edge('B', 'D', 5)
directedWeightedGraph.add_edge('C', 'D', 1)
directedWeightedGraph.add_edge('C', 'F', 3)
directedWeightedGraph.add_edge('D', 'C', 1)
directedWeightedGraph.add_edge('D', 'E', 4)
directedWeightedGraph.add_edge('E', 'F', 3)
directedWeightedGraph.add_edge('F', 'C', 1)
directedWeightedGraph.add_edge('F', 'E', 2)


print(directedWeightedGraph)

print("\nPath is")
print(directedWeightedGraph.find_path('A', 'F'))
print("\nShortest Path is")
print(directedWeightedGraph.find_shortest_path('A', 'F'))
