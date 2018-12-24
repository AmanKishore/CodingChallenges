'''
Appears Twice:
    Find the number that appears twice in a list of n+1 elements with values from 0 to n
'''

def find_repeat(nums):
    n = len(nums) - 1
    sum_wo_duplicate = (n(n - 1))/2
    return sum(nums) - sum_wo_duplicate # Return the difference which finds the duplicate variable