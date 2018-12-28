'''
Kth Last Node
    Find the Kth last node
'''

def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError('Impossible to find less than first to last node: %s' % k)

    left  = head
    right = head

    for _ in range(k - 1):   # Move right to the kth node
        if not right.next:
            raise ValueError('k is larger than the length of the linked list: %s' % k)
        right = right.next

    while right.next:    # Maintain a distance of k between the two pointers until end of list
        left  = left.next
        right = right.next

    return left
