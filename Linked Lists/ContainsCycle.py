'''
Contains Cycle
    Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean 
    indicating whether the list contains a cycle.
'''

def contains_cycle(head):
    slow = head  # Start runners at head
    fast = head

    while fast is not None and fast.next is not None:  # Traverse through list
        slow = slow.next
        fast = fast.next.next
        if fast is slow:  # Fast reaches slow
            return True

    return False  # No cycle reached end