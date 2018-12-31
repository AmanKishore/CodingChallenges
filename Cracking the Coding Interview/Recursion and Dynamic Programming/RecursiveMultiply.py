'''
Recursive Multiply:
    Multiply two positive integers without using * or /
'''


def minProduct3(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b 
    return minProduct3Helper(smaller, bigger)

def minProduct3Helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1 # Divide the smaller by two
    halfProd = minProduct3Helper(s, bigger) # Keep recursively calling till the base case
    if smaller % 2 == 0: 
        return halfProd + halfProd # If smaller is even
    else: 
        return halfProd + halfProd + bigger # If smaller is off
