'''
Contains Cycle
    Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean 
    indicating whether the list contains a cycle. Return head
'''

def cycle_beginning(head):
    slow = head  # Start runners at head
    fast = head

    while fast is not None and fast.next is not None:  # Traverse through list
        slow = slow.next
        fast = fast.next.next
        if fast is slow:  # Fast reaches slow
            break
    if fast is None or fast.next is None:
        return None
    
    slow = head
    while slow != fast:  # Finds the beginning
        fast = fast.next
        slow = slow.next

    return fast  # Beginning of cycle




def removeLoop(head, slow):
    ptr1 = ptr2 = slow
    k = 1
    while ptr1.next != ptr2:  # Count the number of nodes in the cycle
        ptr1 = ptr1.next
        k += 1
    
    ptr1 = ptr2 = head
    for _ in range(k): # Move 
        ptr2 = ptr2.next
    
    while ptr2 != ptr1: # Move both pointers at the same place they will meet at loop starting node
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    ptr2 = ptr2.next
    while(ptr2.next != ptr1): # Get pointer to the last node before the start
        ptr2 = ptr2.next
    
    ptr2.next = None  # delete the loop
