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
        if goal==node:
            visited.append(node)
            return goal
        else:
            visited.append(node)
            for child in self.adj[node]:
                found = self.dfs_maze(child, goal, visited)
                if found!=None:
                    return goal, visited
    
    def DLS(self, node, goal, depth):
        if depth==0 and node==goal:
            return node
        if depth>0:
            if node==goal:
                return goal
            for child in self.adj[node]:
                found = self.DLS(child, goal, depth-1)
                if found==goal:
                    return found
        return None
    
    def IDDFS(self, root, goal):
        for depth in range(10):
            found = self.DLS(root, goal, depth)
            if found==goal:
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
        self.weight[(u,v)] = w
        self.weight[(v,u)] = w

    def get_weight(self, u, v):
        return self.weight[(u,v)]

class DWGraph(WGraph):
    def add_edge(self, u, v, w):
        self.adj[u] = self.adj.get(u, []) + [v]
        self.weight[(u,v)] = w
    
    def dfs_Cost(self, node, visited=[], cost=0):
        if node not in visited:
            visited.append(node)
        for child in self.adj[node]:
            visited, cost = self.dfs_Cost(child, visited, cost+self.get_weight(node, child))
        return visited, cost
    
    def DLS_Cost(self, node, goal, depth, cost=0, visited=[]):
        if depth==0 and node==goal:
            visited.append(node)
            return node, visited, cost
        if depth>0:
            if node==goal:
                return goal, visited, cost
            for child in self.adj[node]:
                found, visited, cost = self.DLS_Cost(child, goal, depth-1, cost+self.get_weight(node, child))
                if found==goal:
                    return found, visited, cost
        visited.append(node)
        return None, visited, cost
    
    def IDDFS_Cost(self, root, goal):
        for depth in range(10):
            found, visited, cost = self.DLS_Cost(root, goal, depth)
            if found==goal:
                return found, visited, cost
            
Dw=DWGraph()
graphNodes=['S','B','A','C']
graphEdges = [('S','B',5),('S', 'A', 1),('S', 'C', 5)]

for n in graphNodes:
    Dw.add_node(n)
for e in graphEdges:
    Dw.add_edge(e[0],e[1],e[2])

print("Depth First Search:")
print(Dw.dfs_Cost('S'))

print("Iterative Deepening Depth First Search:")
print(Dw.IDDFS_Cost('S', 'C'))
