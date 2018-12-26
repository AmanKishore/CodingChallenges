'''
Graph Coloring:
    Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.
'''

class GraphNode:
    
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):

    for n in graph: # Create a valid coloring for the graph
        illegal = []
        for neigh in n.neighbors: # Check the neighbors colors
            if neigh == n:
                raise Exception('Loop')
            if neigh.color: # Make a list of illegal colors
                illegal.append(neigh.color)

        for c in colors: # Assign the color
            if c not in illegal:
                n.color = c
                break
    
    return graph