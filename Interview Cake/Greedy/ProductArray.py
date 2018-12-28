'''
Product Array:
    Write a function product_array() that takes a list of integers and returns a list of the products.
'''
def product_array(int_list):

    if not int_list or len(int_list) == 1: 
        raise IndexError('Too few elements')
        
    final = [1] * (len(int_list))  # Make a list with the products
    product = 1
    for i in range(len(int_list)): # Product before
        final[i] *= product
        product *= int_list[i]
        
    product = 1
    for j in range(len(int_list) - 1, -1, -1):  # Product After
        final[j] *= product
        product *= int_list[j]

    return final


