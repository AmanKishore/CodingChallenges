'''
Mesh Message:
    Find the shortest route for a message from one user (the sender) to another (the recipient). 
    Return a list of users that make up this route.
'''

def bfs_get_path(graph, start_node, end_node):
    
    # Find the shortest route in the network between the two users
    if start_node not in graph or end_node not in graph:
        raise Exception('Start or End Node not in graph')
    visited = set()
    parent = {}
    queue = []
    
    queue.append(start_node)
    
    while queue:
        n = queue.pop(0)
        
        for node in graph[n]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                parent[node] = n
    
    path = []
    n = end_node
    while n != start_node:
        path.insert(0, n)
        if n not in parent:
            return None
        n = parent[n]
        
        
    path.insert(0, start_node)

    return path