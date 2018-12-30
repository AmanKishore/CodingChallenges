'''
InOrder Successor:
    Find the inorder successor in a BST
'''

def inOrderSuccessor(root, n):
      
    if n.right: # If there is a right subtree, find the leftmost min value
        n = n.right
        while n.left: # loop down to find the leftmost leaf
            n = n.left
        return n
  
    p = n.parent
    while p and n != p.right: # Traverses us till node is on left of parent
        n = p 
        p = p.parent
    return p
