'''
Coin Change:
    Find the number of ways to make change for a certain amount
'''


def change_possibilities(amount, coins):
    
    # Calculate the number of ways to make coins
    memo = [0] * (amount + 1)
    memo[0] = 1 # Number of ways to make 0 cents
    
    for change in coins: # Go through every coin
        for i in range(change, len(memo)):  # From the coin till the end, use the previous values
            memo[i] += memo[i - change]     # found to determine the number of coins needed

    return memo[amount]