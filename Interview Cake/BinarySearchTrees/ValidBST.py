'''
Valid BST:
    Validate a BST by checking each node
'''

def valid_bst(root, currmin = -float('inf'), currmax = float('inf')):
    
    # Determine if the tree is a valid binary search tree
    if not root:
        return True
    if (root.value >= currmax) or (root.value <= currmin):  # Checks upper and lower bound
        return False
    return  valid_bst(root.left, currmin, root.value) and valid_bst(root.right, root.value, currmax)