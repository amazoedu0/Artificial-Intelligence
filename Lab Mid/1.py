class Graph:

    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []
    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f"{node} -> {self.adj_list[node]}\n"
        return string
    def add_edges(self, u, v):
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u)



edges = [
    ('1', '2'),
    ('1', '4'),
    ('1', '3'),
    ('3', '6'),
    ('4', '3'),
    ('2', '4'),
    ('2', '5'),
    ('5', '4'),
    ('5', '7'),
    ('4', '7'),
    ('7', '6'),
    ('4', '6')
]
nodes = ['1', '2', '3', '4', '5', '6', '7']

graph = Graph(nodes, is_directed=True)

for u, v in edges:
    graph.add_edges(u, v)

print(graph)