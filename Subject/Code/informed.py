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

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []
    # undirected unweighted graph 
    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v] 
        self.adj[v] = self.adj.get(v, []) + [u]
    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return sum(len(l) for _, l in self.adj.items())

class DGraph(Graph):
    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, []) + [v]

    def dfs_maze(self, node, goal, visited=[]):
        if goal == node:
            visited.append(node)
            return goal
        elif node != goal: 
            visited.append(node)
            for child in self.adj[node]:
                found = self.dfs_maze(child, goal, visited)
            if found != None:
                return visited


class WGraph(Graph):
    def init(self, nodes=None,edges=None):
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
DWs=Graph()
DW = DGraph()
DW.add_node('A')
DW.add_node('B')
DW.add_node('C')
DW.add_node('D')
DW.add_node('E')
DW.add_node('F')
DW.add_node('G')
DW.add_node('H')
DW.add_node('I')
DW.add_node('J')
DW.add_node('K')
DW.add_node('L')
DW.add_node('M')
DW.add_node('N')
DW.add_node('O')
DW.add_node('P')
DW.add_node('Q')
DW.add_node('R')
DW.add_node('S')
DW.add_node('T')
DW.add_node('U')
DW.add_node('V')
DW.add_node('W')
DW.add_node('X')
DW.add_node('Y')
DW.add_node('Z')
DW.add_node('AA')
DW.add_node('AB')
DW.add_node('AC')
DW.add_node('AD')
DW.add_node('AE')
DW.add_node('AF')
DW.add_node('GOAL')
DW.add_edge('A', 'B')
DW.add_edge('A', 'N')
DW.add_edge('B', 'C')
DW.add_edge('B', 'H')
DW.add_edge('C', 'D')
DW.add_edge('D', 'E')
DW.add_edge('D', 'F')
DW.add_edge('E', 'GOAL')
DW.add_edge('F', 'G')
DW.add_edge('H', 'I')
DW.add_edge('H', 'J')
DW.add_edge('J', 'K')
DW.add_edge('K', 'L')
DW.add_edge('L', 'M')
DW.add_edge('M', 'GOAL')
DW.add_edge('N', 'O')
DW.add_edge('N', 'P')
DW.add_edge('P', 'Q')
DW.add_edge('P', 'T')
DW.add_edge('Q', 'R')
DW.add_edge('R', 'S')
DW.add_edge('S', 'GOAL')
DW.add_edge('T', 'U')
DW.add_edge('U', 'V')
DW.add_edge('U', 'X')
DW.add_edge('V', 'W')
DW.add_edge('W', 'GOAL')
DW.add_edge('X', 'Y')
DW.add_edge('X', 'Z')
DW.add_edge('Y', 'GOAL')
DW.add_edge('AA', 'GOAL')
DW.add_edge('AB', 'AC')
DW.add_edge('AC', 'AD')
DW.add_edge('AC', 'AF')
DW.add_edge('AD', 'AE')
DW.add_edge('AE', 'GOAL')
DW.add_edge('AF', 'GOAL')
print("The cheapest path is: "+DW.dfs_maze('A', 'GOAL'))