'''
Second Largest:
    Find the second largest element in a tree.
'''

def find_largest(root):
    while root.right:
        root = root.right
    return root.value

def find_second_largest(root):

    # Find the second largest item in the binary search tree
    if not root or (not root.left and not root.right):
        raise ValueError('Too few nodes')
    
    while root:
        if root.left and not root.right:
            return find_largest(root.left)
        
        if (root.right and not root.right.left and not root.right.right):
            return root.value
        
        root = root.right