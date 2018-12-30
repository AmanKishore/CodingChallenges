'''
First Common Ancestor:
    Design an algorithm to find the first common ancestor of two nodes in a binary tree.
'''

def findLCA(root, n1, n2): 
      
    if root is None: # If you reach the end of the tree 
        return None
  
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.key == n1 or root.key == n2: # Check to see if we have hit a node we are trying to find, then set the left/right
        return root  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
  
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: # Only if both left and right are found and have a value then return the root
        return root  
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca # Return whichever one has a value