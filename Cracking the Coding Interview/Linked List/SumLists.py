'''
Sum Lists:
    Given two linked lists with two integers find the sum 
    Input: (7 -> 1 -> 6) + (5 -> 9 -> 2)
    Output: (2 -> 1 -> 9)
'''

def sum_lists(n1, n2):
    result = set() # LinkedList()
    carry = 0
    while n1 or n2:
        result = carry # Use it to add to the final
        if n1:
            result += n1.value # Uses carry plus current value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        result.add(result % 10) # Adds to the tail
        carry = result // 10 # Makes the carry value

    if carry:
        result.add(carry) # If carry left over add it to the end of the linked list

    return result
