'''
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''

def twoSum(nums, target):
    buff_dict = {} # Empty dict for storing traversed
    for i in range(len(nums)):
        if nums[i] in buff_dict: # If the other time exists to get to the target use that
            return [buff_dict[nums[i]], i]
        buff_dict[target - nums[i]] = i  # Otherwise use that as the required time
    return None
