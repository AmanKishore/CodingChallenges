'''
Merge Sorted Lists:
    Write a function to merge our lists of orders into one sorted list.    
    Input:  list1 = [3, 4, 6, 10, 11, 15]
            list2 = [1, 5, 8, 12, 14, 19]
    Output: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
'''

def merge_lists(list1, list2):
    msize = len(list1) + len(list2)  # Set up our merged
    merged = [None] * msize

    curr_list2 = 0
    curr_list1 = 0
    curr_merged = 0
    while curr_merged < msize:
        list1_done = curr_list1 >= len(list1)
        list2_done = curr_list2 >= len(list2)
        if (not list1_done and  (list2_done or list1[curr_list1] < list2[curr_list2])): # list1 not done and list2 done
            merged[curr_merged] = list1[curr_list1]
            curr_list1 += 1
        else:
            merged[curr_merged] = list2[curr_list2]
            curr_list2 += 1

        curr_merged += 1

    return merged