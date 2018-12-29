'''
Partition:
    Partition a linked list with anode the values less than before it and a node the values greater than or equal to the right.
'''

def partition(node, x):
    head = tail = node

    while node:
        nextNode = node.next
        if node.value < x: # If a value is less than x add to the front
            node.next = head
            head = node
        else:              # Else add it to the back
            tail.next = node
            tail = node
            node.next = None
        node = nextNode
        
    # Error check in case nodes are less than x
    if node.tail.next is not None:
        node.tail.next = None