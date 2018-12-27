'''
String Permuatations:
    Write a recursive function for generating all permutations of an input string. Return them as a set.
'''

def get_permutations(string):  # Ex: string = 'abc'
    # Base case
    if len(string) <= 1: # string = 'a' adds a to set
        return set([string])  # This returns the first character to the permutation set

    all_but_last = string[:-1] # Stored as a local variable so different for each run through
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last_char
    permutations_all_but_last = get_permutations(all_but_last)

    # Put the last_char char in all possible positions for each of
    # the above permutations
    permutations = set()
    for substring in permutations_all_but_last:  # Adds to permutations by placing it at each index
        for i in range(len(all_but_last) + 1):

            # Ex: substring = 'a' and last_char = 'b'
                # i = 0: 'ba'
                # i = 1: 'ab'
            permutation = (substring[:i] + last_char + substring[i:])
            permutations.add(permutation) # Add each new permuation to ther permutation set

    return permutations  # Adds to the overall set