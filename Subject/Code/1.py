# from queue import LifoQueue

# class Graph:
#   def __init__(self,nodes,is_directed=False):
#     self.nodes=nodes
#     self.adj_list={}
#     self.is_directed=is_directed
#     for node in self.nodes:
#       self.adj_list[frozenset(node)]={}
#   def __str__(self):
#     string=""
#     for node in self.nodes:
#       string += f"{node} -> {self.adj_list[node]}\n"
#     return string
#   def directed(self,src,dst):
#     for dest in dst:
#       if dest in self.nodes:
#         self.adj_list[src].append(dest)
    
#   def un_directed(self,src,dst):
#     for dest in dst:
#       if dest in self.nodes:
#         self.adj_list[src].append(dest)
#         self.adj_list[dest].append(src)
#   def add_edge(self,src,dst):
#     if self.is_directed:
#       self.directed(src,dst)
#     else:
#       self.un_directed(src,dst)
#   def degree(self,node):
#     return len(self.adj_list[node])

#   def dfs(self,node):
#     checked=[False for node in self.nodes]
#     dfs(self.nodes[self.nodes.index('S')],checked)

#   def dfs(self,node,checked):
#     stack = LifoQueue(maxsize=len(self.nodes))
#     stack.put(node)
#     depthFirstSearch=[]
#     while node!='G':
#       depthFirstSearch.append(stack.get())
#       nodes = self.adj_list[node]
#       for n in nodes:
#         index=self.nodes.index['n']
#         if not checked[index]:
#           checked[index]=True
#           dfs(self,n,checked)
#     return depthFirstSearch

# def find_path(graph, src, dst, path=[]):
#   path += src
#   if src not in graph.nodes:
#     return None
#   if src==dst:
#     return path
#   for node in graph.adj_list[src]:
#     if node not in path:
#       new_path = find_path(graph, node, dst, path)
#       if new_path:
#         return new_path
#   return None
 
 
#   """
#   a1 a2 a3 a4 a5 a6 a7 a8
#   b1 b2 b3 b4 b5 b6 b7 b8
#   c1 c2 c3 c4 c5 c6 c7 c8
#   d1 d2 d3 d4 d5 d6 d7 d8
#   e1 e2 e3 e4 e5 e6 e7 e8
#   f1 f2 f3 f4 f5 f6 f7 f8
#   g1 g2 g3 g4 g5 g6 g7 g8
#   h1 h2 h3 h4 h5 h6 h7 h8  

#   """

# nodes = [
#     {'a1':0}, {'a2':3}, {'a3':0}, {'a4':0}, {'a5':1}, {'a6':0}, {'a7':0}, {'a8':0}, 
#     {'b1':0}, {'b2':1}, {'b3':0}, {'b4':6}, {'b5':9}, {'b6':4}, {'b7':3}, {'b8':0}, 
#     {'c1':0}, {'c2':9}, {'c3':7}, {'c4':7}, {'c5':0}, {'c6':0}, {'c7':1}, {'c8':5}, 
#     {'d1':4}, {'d2':7}, {'d3':0}, {'d4':3}, {'d5':6}, {'d6':2}, {'d7':7}, {'d8':0}, 
#     {'e1':0}, {'e2':5}, {'e3':0}, {'e4':5}, {'e5':0}, {'e6':8}, {'e7':0}, {'e8':0}, 
#     {'f1':0}, {'f2':0}, {'f3':4}, {'f4':0}, {'f5':5}, {'f6':2}, {'f7':0}, {'f8':0}, 
#     {'g1':2}, {'g2':8}, {'g3':3}, {'g4':0}, {'g5':0}, {'g6':7}, {'g7':8}, {'g8':1}, 
#     {'h1':0}, {'h2':0}, {'h3':8}, {'h4':0}, {'h5':4}, {'h6':0}, {'h7':0}, {'h8':0}, 
#     ] 

# edges = [
#          ({'a2':3}, {'b2':1}), ({'a5':1}, {'b5':9}), ({'b4':6}, {'b5':9}), ({'b5':9}, {'b6':4}),
#          ({'b6':4}, {'b7':3}), ({'b2':1}, {'c2':9}), ({'c2':9}, {'c3':7}), ({'c3':7}, {'c4':7}),
#          ({'c7':1}, {'c8':5}), ({'c2':9}, {'d2':7}), ({'d1':4}, {'d2':7}), ({'c4':7}, {'d4':3}),
#          ({'d4':3}, {'d5':6}), ({'d6':2}, {'d7':7}), ({'c7':1}, {'d7':7}), ({'d2':7}, {'e2':5}),
#          ({'d4':3}, {'e4':5}), ({'d6':2}, {'e6':8}), ({'e6':8}, {'f6':2}), ({'f3':4}, {'g3':3}),
#          ({'f5':5}, {'f6':2}), ({'f6':2}, {'g6':7}), ({'g1':2}, {'g2':8}), ({'g2':8}, {'g3':3}),
#          ({'g6':7}, {'g7':8}), ({'g7':8}, {'g8':1}), ({'g3':3}, {'h3':8})
#   ]

# # nodes = ['A','B','C','D','E','F','G','H','P','Q','R','S']
#         #0, 1, 2 ,3 ,4 ,5
# #         #-6, -5, -4, -3, -2, -1
# # edges = [('B','A'),('D','B'),('D','C'),('C','A'),('D','E'),('S','D'),('S','E'),('S','P'),('P','Q'),('H','Q'),('H','P'),
# #          ('E','H'),('E','R'),('R','F'),('F','C'),('F','G')]
 


# directed = Graph(nodes, True)
# un_directed = Graph(nodes,False)

# for src,dest in edges:
#   directed.add_edge(src,dest)
# print(f"DIRECTED\n{directed}")
# path = [] 
# print(find_path(directed, 'd5', 'c8', path))

# for src,dest in edges:
#   un_directed.add_edge(src,dest)
# print(f"\nUNDIRECTED\n{un_directed}")
# path = [] 
# print(find_path(un_directed, 'd5', 'c8', path))


# # direct = Graph(['A','H','M','D'])
# # undirect = Graph(['A','H','M','D'])




from queue import LifoQueue

class Graph:
  def __init__(self,nodes,is_directed=False):
    self.nodes=nodes
    self.adj_list={}
    self.is_directed=is_directed
    for node in self.nodes:
      self.adj_list[node]=[]
  def __str__(self):
    string=""
    for node in self.nodes:
      string += f"{node} -> {self.adj_list[node]}\n"
    return string
  def directed(self,src,dst):
    for dest in dst:
      if dest in self.nodes:
        self.adj_list[src].append(dest)
    
  def un_directed(self,src,dst):
    for dest in dst:
      if dest in self.nodes:
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
  def add_edge(self,src,dst):
    if self.is_directed:
      self.directed(src,dst)
    else:
      self.un_directed(src,dst)
  def degree(self,node):
    return len(self.adj_list[node])

  def dfs(self,node):
    checked=[False for node in self.nodes]
    dfs(self.nodes[self.nodes.index('S')],checked)

  def dfs(self,node,checked):
    stack = LifoQueue(maxsize=len(self.nodes))
    stack.put(node)
    depthFirstSearch={}
    while node!='G':
      depthFirstSearch.append(stack.get())
      nodes = self.adj_list[node]
      for n in nodes:
        index=self.nodes.index['n']
        if not checked[index]:
          checked[index]=True
          dfs(self,n,checked)
    return depthFirstSearch

def find_path(graph, src, dst, path=[]):
  path += src
  if src not in graph.nodes:
    return None
  if src==dst:
    return path
  for node in graph.adj_list[src]:
    if node not in path:
      new_path = find_path(graph, node, dst, path)
      if new_path:
        return new_path
  return None
 
 
nodes = ['A','B','C','D','E','F','G','H','P','Q','R','S']
        # 0, 1, 2 ,3 ,4 ,5
        #-6, -5, -4, -3, -2, -1
edges = [('B','A'),('D','B'),('D','C'),('C','A'),('D','E'),('S','D'),('S','E'),('S','P'),('P','Q'),('H','Q'),('H','P'),
         ('E','H'),('E','R'),('R','F'),('F','C'),('F','G')]
 

directed = Graph(nodes, True)
for src,dest in edges:
  directed.add_edge(src,dest)
print(f"DIRECTED\n{directed}")
path = []
print(find_path(directed, 'G', 'G', path))

un_directed = Graph(nodes, False)
for src,dest in edges:
  un_directed.add_edge(src,dest)
print(f"DIRECTED\n{un_directed}")
path = []
print(find_path(un_directed, '', 'G', path))

"""
  # a1 a2 a3 a4 a5 a6 a7 a8
  # b1 b2 b3 b4 b5 b6 b7 b8
  # c1 c2 c3 c4 c5 c6 c7 c8
  # d1 d2 d3 d4 d5 d6 d7 d8
  # e1 e2 e3 e4 e5 e6 e7 e8
  # f1 f2 f3 f4 f5 f6 f7 f8
  # g1 g2 g3 g4 g5 g6 g7 g8
  # h1 h2 h3 h4 h5 h6 h7 h8  
# 
nodes = [
    {'a1':0}, {'a2':3}, {'a3':0}, {'a4':0}, {'a5':1}, {'a6':0}, {'a7':0}, {'a8':0}, 
    {'b1':0}, {'b2':1}, {'b3':0}, {'b4':6}, {'b5':9}, {'b6':4}, {'b7':3}, {'b8':0}, 
    {'c1':0}, {'c2':9}, {'c3':7}, {'c4':7}, {'c5':0}, {'c6':0}, {'c7':1}, {'c8':5}, 
    {'d1':4}, {'d2':7}, {'d3':0}, {'d4':3}, {'d5':6}, {'d6':2}, {'d7':7}, {'d8':0}, 
    {'e1':0}, {'e2':5}, {'e3':0}, {'e4':5}, {'e5':0}, {'e6':8}, {'e7':0}, {'e8':0}, 
    {'f1':0}, {'f2':0}, {'f3':4}, {'f4':0}, {'f5':5}, {'f6':2}, {'f7':0}, {'f8':0}, 
    {'g1':2}, {'g2':8}, {'g3':3}, {'g4':0}, {'g5':0}, {'g6':7}, {'g7':8}, {'g8':1}, 
    {'h1':0}, {'h2':0}, {'h3':8}, {'h4':0}, {'h5':4}, {'h6':0}, {'h7':0}, {'h8':0},
    'G','S' 
    ] 
# 
edges = [
         ({'a2':3}, {'b2':1}), ({'a5':1}, {'b5':9}), ({'b4':6}, {'b5':9}), ({'b5':9}, {'b6':4}),
         ({'b6':4}, {'b7':3}), ({'b2':1}, {'c2':9}), ({'c2':9}, {'c3':7}), ({'c3':7}, {'c4':7}),
         ({'c7':1}, {'c8':5}), ({'c2':9}, {'d2':7}), ({'d1':4}, {'d2':7}), ({'c4':7}, {'d4':3}),
         ({'d4':3}, {'d5':6}), ({'d6':2}, {'d7':7}), ({'c7':1}, {'d7':7}), ({'d2':7}, {'e2':5}),
         ({'d4':3}, {'e4':5}), ({'d6':2}, {'e6':8}), ({'e6':8}, {'f6':2}), ({'f3':4}, {'g3':3}),
         ({'f5':5}, {'f6':2}), ({'f6':2}, {'g6':7}), ({'g1':2}, {'g2':8}), ({'g2':8}, {'g3':3}),
         ({'g6':7}, {'g7':8}), ({'g7':8}, {'g8':1}), ({'g3':3}, {'h3':8}),('S',{'d5':6}),({'c8':5},'G')
  ]
# 
# 
# 
# directed = Graph(nodes, True)
un_directed = Graph(nodes,False)
# 
for src,dest in edges:
  un_directed.add_edge(src,dest)
print(f"\nUNDIRECTED\n{un_directed}")
path = []
print(find_path(un_directed, {'d5':6},{'c8':5}, path))
"""


