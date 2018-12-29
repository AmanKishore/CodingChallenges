'''
Intersection:
    Deterimin if two linked lists intersect
'''

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    for _ in range(diff):
        longer = longer.next

    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next

    return longer