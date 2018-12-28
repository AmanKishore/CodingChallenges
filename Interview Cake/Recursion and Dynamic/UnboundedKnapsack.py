'''
Unbounded Knapsack:
    Given a knapsack with a capacity and cakes with a value and a weight find the best max value.
'''

def max_duffel_bag_value(cake_tuples, weight_capacity):
    
    best_value = [0] * (weight_capacity + 1)  # Set up the array to find max values
    
    for weight, value in cake_tuples:
        if weight is 0 and value > 0: # Infinite cakes!
            return float('inf')
        for i in range(weight, len(best_value)): # Update the value at each weight with the newest cake
            best_value[i] = max(best_value[i], value + best_value[i - weight]) # If the previously found value is better  

    return best_value[weight_capacity]