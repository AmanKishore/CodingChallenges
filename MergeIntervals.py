'''
MergeIntervals:
    Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
    Input:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    Output:  [(0, 1), (3, 8), (9, 12)]
'''

def merge_ranges(meetings):

    # Merge meeting ranges
    meetings.sort(key = lambda x : x[0]) # Sort meeting times
    merged = []                          
    
    for i in meetings:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)                                       # Inputs new meeting if nothing overlaps 
        else:   
            merged[-1] = (merged[-1][0], max(merged[-1][1], i[1])) # Updates last inserted meeting if overlap

    return merged