'''
Route Between Nodes:
    Determine if there is a path between two nodes
'''

from collections import defaultdict 
   
class Graph: # Adjacency List

    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): # function to add an edge to graph 
        self.graph[u].append(v) 

    def BFS(self, s, end): # BFS of the graph

        visited = set()
        queue = [] 
        queue.append(s) 
        visited.add(s)
  
        while queue: 
  
            s = queue.pop(0) # Dequeue a vertex from

            for i in self.graph[s]: # Get all the adjacent vertices of the dequeued vertex and
                if i not in visited: # determine if end node has been found
                    queue.append(i) 
                    visited.add(i)
                    if s == end:
                        return True
        return False