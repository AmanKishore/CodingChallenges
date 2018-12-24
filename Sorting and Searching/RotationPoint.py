'''
Rotation Point
    Find the rotation point in an array
'''

def find_rotation_point(nums):
    
    l = 0 # Starting index
    r = len(nums) - 1 # Ending index
    
    while l < r:
        m = l + (r-l)/2
        if nums[m] >= nums[0]:   # Check if checker needs to move up or down
            l = m
        else:
            r = m
            
        if l + 1 == r:  # Boundries have converged
            return r
        
    return -1