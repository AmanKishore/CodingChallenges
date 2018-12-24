'''
InPlace Shuffle
    Write a function for doing an in-place shuffle of a list
'''
import random

def shuffle(the_list):
    for i in range(len(the_list)): # Shuffle the input in place
        randidx = random.randrange(i, len(the_list))
        if randidx != i:
            the_list[randidx], the_list[i] = the_list[i], the_list[randidx]
