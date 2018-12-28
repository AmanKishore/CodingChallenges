'''
Reverse List
    Write a function to reverse a Linked List
'''


def reverse(head):
    curr = head
    prev = None
    nextn = None

    while curr: # Traverse through
        nextn = curr.next # Copy a pointer to the next element
        curr.next = prev # Reverse the 'next' pointer

        prev = curr # Step forward in the list
        curr = nextn

    return prev