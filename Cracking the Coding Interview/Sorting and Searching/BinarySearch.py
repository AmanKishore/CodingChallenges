'''
Binary Search
    Implement a binary search
'''

def binary_search(array, target):
    l = 0
    r = len(array) - 1

    while l < r:
        m = (l + r)//2
        if array[m] == target:
            return m
        elif array[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
