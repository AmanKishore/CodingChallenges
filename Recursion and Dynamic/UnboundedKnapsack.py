'''
Unbounded Knapsack:
    Given a knapsack with a capacity and cakes with a value and a weight find the best max value.
'''

def max_duffel_bag_value(cake_tuples, weight_capacity):
    
    value_weight = [0] * (weight_capacity + 1)  # Set up the array to 
    value_weight[0] = 0
    
    for cake in cake_tuples:
        if cake[0] is 0 and cake[1] > 0: # Infinite cakes!
            return float('inf')
        for i in range(cake[0], len(value_weight)): # Update the value at each weight with the newest cake
            value_weight[i] = max(value_weight[i], cake[1] + value_weight[i - cake[0]]) # If the previously found value is better  

    return value_weight[weight_capacity]