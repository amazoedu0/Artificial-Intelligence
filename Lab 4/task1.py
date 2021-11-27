from queue import LifoQueue


class Graph:
    def __init__(self, nodes, is_directed=False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f"{node} -> {self.adj_list[node]}\n"
        return string

    def directed(self, src, dst, cost):
        for dest in dst:
            if dest in self.nodes:
                self.adj_list[src].append((dest, cost))

    def un_directed(self, src, dst, cost):
        for dest in dst:
            if dest in self.nodes:
                self.adj_list[src].append((dest, cost))
                self.adj_list[dest].append((src, cost))

    def add_edge(self, src, dst, cost):
        if self.is_directed:
            self.directed(src, dst, cost)
        else:
            self.un_directed(src, dst, cost)

    def degree(self, node):
        return len(self.adj_list[node])


def find_path(graph, src, dst, path=[]):
    path += src
    if src not in graph.nodes:
        return None
    if src == dst:
        return path
    que = LifoQueue(graph.adj_list[src])
    for node in graph.adj_list[src]:
        if node not in path:
            node = que.get()
            new_path = find_path(graph, node, dst, path)
            if new_path:
                return new_path
    return None


def shortest_path(g, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    if start not in g.nodes:
        return None
    q = PriorityQueue(g.adj_list[start])
    while not q.is_empty():
        node = q.pop()
        newpath = shortest_path(g, node[0], end, path)
        if newpath:
            return newpath
    return None


nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 2), ('A', 'C', 1), ('B', 'C',
                                   2), ('B', 'D', 5), ('C', 'D', 1), ('C', 'F', 3),
    ('D', 'C', 1), ('D', 'E', 4), ('E', 'F', 3), ('F', 'C', 1), ('F', 'E', 2)
]

g = Graph(nodes, True)

for src, dst, cost in edges:
    g.add_edge(src, dst, cost)

print(g)
path = []
print(find_path(g, 'A', 'E'))
