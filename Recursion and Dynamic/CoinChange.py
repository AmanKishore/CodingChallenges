'''
Coin Change:
    Find the number of ways to make change for a certain amount
'''


def change_possibilities(amount, change):
    
    # Calculate the number of ways to make change
    memo = [0] * (amount + 1)
    memo[0] = 1 # Number of ways to make 0 cents
    
    for change in change: # Go through every coin
        for i in range(change, len(memo)):  # From the coin till the end, use the previous values
            memo[i] += memo[i - change]     # found to determine the number of coins needed

    return memo[amount]