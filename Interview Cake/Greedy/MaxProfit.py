'''
Max Profit:
    Write an efficient function that takes stock_prices and returns the best profit.
    Input:  stock_prices = [10, 7, 5, 8, 11, 9]
    Output: 6
'''

def get_max_profit(stock_prices):
    
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
        
    currmin = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for price in stock_prices[1:]:
        max_profit = max(price - currmin, max_profit)
        currmin = min(price, currmin)

    return max_profit