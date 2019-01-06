'''
Superbalanced:
    A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.
'''

def superbalanced(root):
    if not root:
        return True
    
    depths = []  # Keep track of unique depths

    nodes = [] # Stack for DFS

    nodes.append((root, 0))  # Use a tuple to keep track of depth and node at same time
    while len(nodes) != 0:
        node, depth = nodes.pop()

        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)
            
            if len(depths) > 2 or (len(depths) == 2 and abs(depth[0] - depth[1]) > 1):  # Conditions for superbalance
                return False
        
        else:
            if node.left:  # Not a leaf keep stepping down
                nodes.append((node.left, depth+1))
            if node.right:
                nodes.append((node.right, depth+1))
    return True