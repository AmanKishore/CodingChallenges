'''
Triple Step:
    A child can run up and hop 1, 2, or 3 steps at a time. How many ways can it make it up the stairs.
'''

memo = {0 : 1, 1 : 1, 2 : 2}

def step(n):

    if n in memo:
        return memo[n]
    else:
        memo[n] = step(n-1) + step(n-2) + step(n-3) # Store the newest discovered number
    return memo[n]

print(step(4))