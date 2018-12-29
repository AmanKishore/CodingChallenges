'''
Remove Duplicates:
    Remove duplicates from a linked list.
'''

def remove_dups(llist):
    if llist.head is None:
        return

    curr = llist.head
    seen = set([curr.value])
    while curr.next:
        if curr.next.value in seen: # If next is duplicate
            curr.next = curr.next.next # Skip it
        else:
            seen.add(curr.next.value) # Add it to the seen hash set
            curr = curr.next

    return llist