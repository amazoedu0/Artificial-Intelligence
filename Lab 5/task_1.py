class Graph:
    def __init__(self, nodes=None, edges=None):
        """Initialize a graph object.
        Args:
            nodes:  Iterator of nodes. Each node is an object.
            edges:  Iterator of edges. Each edge is a tuple of 2 nodes.
        """
        self.nodes, self.adj = [], {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def length(self):
        """Returns the number of nodes in the graph.
        >>> g = Graph(nodes=[x for x in range(7)])
        >>> len(g)
        7
        """
        return len(self.nodes)

    def traverse(self):
        return 'V: %s\nE: %s' % (self.nodes, self.adj)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []

    def add_edge(self, u, v):   # undirected unweighted graph
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return sum(len(l) for _, l in self.adj.items()) // 2


class DGraph(Graph):
    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v]

    def dfs(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
        for child in self.adj[node]:
            self.dfs(child, visited)
        return visited

    def dfs_maze(self, node, goal, visited=[]):
        if goal == node:
            visited.append(node)
            return goal
        else:
            visited.append(node)
            for child in self.adj[node]:
                found = self.dfs_maze(child, goal, visited)
                if found != None:
                    return goal, visited

    def DLS(self, node, goal, depth):
        if depth == 0 and node == goal:
            return node
        if depth > 0:
            if node == goal:
                return goal
            for child in self.adj[node]:
                found = self.DLS(child, goal, depth-1)
                if found == goal:
                    return found
        return None

    def IDDFS(self, root, goal):
        for depth in range(10):
            found = self.DLS(root, goal, depth)
            if found == goal:
                return found


class WGraph(Graph):
    def __init__(self, nodes=None, edges=None):
        """Initialize a graph object.
        Args:
            nodes:  Iterator of nodes. Each node is an object.
            edges:  Iterator of edges. Each edge is a tuple of 2 nodes and a weight.
        """
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


D = DGraph()

graphNodes = ['A', 'B', 'E', 'M', 'K', 'Q', 'J', 'I', 'R',
              'N', 'F', 'S', 'O', 'C', 'G', 'T', 'D', 'P', 'H', 'L']
for n in graphNodes:
    D.add_node(n)

graphEdges = [('M', 'N'),('I', 'M'),('J', 'N'),('A', 'E'),('A', 'B'),('E', 'I'),('M', 'Q'),('N', 'R'),('F', 'G'),('B', 'F'),('F', 'J'),('C', 'D'),('F', 'J'),('G', 'C'),('G', 'H'),('J', 'K'),('G', 'K'),('K', 'L'),('J', 'N'),('N', 'O'),('O', 'P'),('O', 'S'),('K', 'O'),('P', 'T'),('R', 'S')]

for e in graphEdges:
    D.add_edge(e[0],e[1])

print("Depth First Search:")
print(D.dfs_maze('A', 'T'))
print("Depth Limited Search:")
print(D.DLS('A', 'T', 9))
print("Iterative Deepening Depth First Search:")
print(D.IDDFS('A', 'T'))
