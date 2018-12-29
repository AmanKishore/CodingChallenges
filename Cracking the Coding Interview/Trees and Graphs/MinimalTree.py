'''
Minimal Tree:
    Given a sorted array (increasing order) find the tree with the minimum height
'''

def minimal_tree(arr):
    if not arr:
        return None
    mid = len(arr)//2
    node = TreeNode(arr[mid])
    node.left = minimal_tree(arr[:mid]) # Make the left subtree
    node.right = minimal_tree(arr[mid+1:]) # Make the right subtree
    return node

class TreeNode:
    def __init__(self, val):
        self.left
        self.right
        self.value = val