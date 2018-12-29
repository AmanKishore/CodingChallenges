'''
Missing Int:
    Find an integer that is not contained in a list of 4 billion integers.
'''

import random

def missing_int(integer_list):
  guess = random.randint(0, (1 << 64) - 1)
  for integer in integer_list:
    if integer == guess:
      return missing_int(integer_list)
  return guess