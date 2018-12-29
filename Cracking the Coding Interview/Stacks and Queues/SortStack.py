'''
Sort Stack:
    Sort with the smallest items on the top using only stacks.
'''

def sort_stack(stack):
    r = []
    while stack:
        tmp = stack.pop()
        while r and r[-1] > tmp: # Check if the top of the sorted stack is greater than the top of the given stack
            stack.append(r.pop()) # If it is, push the top of the sorted stack into the given stack
        r.append(tmp) # Always push in the tmp 
    while r:
        stack.append(r.pop()) # This will make it least to greatest
    