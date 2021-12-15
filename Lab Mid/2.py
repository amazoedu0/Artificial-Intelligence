class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes, self.adj = [], {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []

    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]


class DGraph(Graph):
    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v]

    def DFS(self, node, goal, visited=[]):
        if goal == node:
            visited.append(node)
            print(visited)
            return goal
        elif goal != node:
            visited.append(node)
            for child in self.adj[node]:
                found = self.DFS(child, goal, visited)
                if found != None:
                    return found, visited
        return None


D = DGraph()
nodes = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
edges = [('0', '3'),('3', '2'),('2', '5'),('5', '6'),
         ('0', '1'),('0', '8'),('8', '4'),('4', '3'),
         ('2', '7'),('7', '1')]

for n in nodes:
    D.add_node(n)

for u, v in edges:
    D.add_edge(u, v)

print("\n\nSHORTEST DISTANCE USING DFS: \n")
D.DFS('0', '6')