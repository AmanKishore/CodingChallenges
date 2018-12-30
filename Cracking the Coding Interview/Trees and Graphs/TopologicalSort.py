'''
Topological Sort:
    The linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering.
'''

from collections import defaultdict 
   
class Graph: 
    def __init__(self, vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices # No. of vertices 
  
    def addEdge(self, u, v): # Add edge
        self.graph[u].append(v) 
  
    def topologicalSort(self): 
        visited = [False]*self.V  # Marks everything not visited
        stack = [] 
  
        for i in range(self.V): # Sort all verticies
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        print(stack) 

    def topologicalSortUtil(self, v, visited, stack): 
  
        visited[v] = True # Current Node
  
        for i in self.graph[v]: # All adjacent verticies  
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack) 
  
        stack.insert(0, v) # Push current vertex
  
g = Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("Following is a Topological Sort of the given graph")
g.topologicalSort() 