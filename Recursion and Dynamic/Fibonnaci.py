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