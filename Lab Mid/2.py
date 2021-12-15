def add_vertex(a):

    global graph

    global vertices_no

    if a in graph:

        print("Vertex ", a, " already exists.")

    else:

        vertices_no = vertices_no + 1

        graph[a] = []


def add_edge(a1, a2, e):

    global graph

    if a1 not in graph:

        print("Vertex ", a1, " does not exist.")

    elif a2 not in graph:

        print("Vertex ", a2, " does not exist.")

    else:

        temp = [a2, e]

        graph[a1].append(temp)


def print_graph():

    global graph

    for vertex in graph:

        for edges in graph[vertex]:

            print(vertex, " -> ", edges[0])


graph = {}

vertices_no = 0

vert = [1, 2, 3, 4, 5, 6, 7]
edg = [
    (1, 3, 1),
    (1, 4, 1),
    (1, 2, 1),
    (2, 4, 3),
    (2, 5, 3),
    (3, 6, 4),
    (4, 3, 1),
    (4, 6, 1),
    (4, 7, 1),
    (5, 4, 1),
    (5, 7, 1),
    (7, 6, 1)
]
for v in vert:
    add_vertex(v)
for s,d,v in edg:
    add_edge(s,d,v)

print_graph()
