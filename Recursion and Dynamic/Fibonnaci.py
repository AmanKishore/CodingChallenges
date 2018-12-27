'''
Fibonacci:
    Find the Nth fibonacci number.
'''

memo = {0 : 0, 1 : 1}

def fib(n):

    # Compute the nth Fibonacci number
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2) # Store the newest discovered number
    return memo[n]

def fib_bottom_up(n):
    if n < 0:
        raise ValueError('Index was negative. No such thing as a negative index in a series.')
    elif n in [0, 1]:
        return n

    # Bottom Up fibonacci serie
    prev_prev = 0  # 0th fibonacci
    prev = 1       # 1st fibonacci

    for _ in range(n - 1): # Go to two before because you already have first two included
        current = prev + prev_prev # Use the previous two to calculate the current
        prev_prev = prev
        prev = current

    return current