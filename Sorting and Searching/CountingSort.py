'''
Counting Sort
    Use counting sort to sort a list in O(n) time
'''

def sort_scores(unsorted_values, highest_possible_values):

    sort = [0] * (highest_possible_values + 1)  # Sort the scores in O(n) time
    for val in unsorted_values:
        sort[val] += 1
        
    final = []
    
    for i in range(len(sort) - 1, -1, -1):  # Traverses from the back of the list
        if sort[i] != 0:
            for j in range(sort[i]):
                final.append(i)
            
    return final
