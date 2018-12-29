'''
Intersection:
    Deterimine if and where two linked lists intersect
'''

def intersection(list1, list2):
    if list1.tail is not list2.tail:  # Checking whether the tails are equal
        return False

    s = list1 if len(list1) < len(list2) else list2
    l = list2 if len(list1) < len(list2) else list1

    diff = len(l) - len(s) # Finding the difference between the list sizes

    shorter, longer = s.head, l.head

    for _ in range(diff):
        longer = longer.next # Move the longer diff steps forward to match the length

    while shorter is not longer: # Keep going through until intersection is found
        shorter = shorter.next
        longer = longer.next

    return longer