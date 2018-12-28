'''
Permutation Palindrome
    Write an efficient function that checks whether any permutation of an input string is a palindrome.
    Ex: "ivicc" should return True
        "civil" should return False 
'''

def palindrome_permutation(string):
    unpaired = set()  # Track Odd Characters

    for char in string:
        if char in unpaired:
            unpaired.remove(char)
        else:
            unpaired.add(char)

    return len(unpaired) <= 1 # Not a permutation if there is more than one odd
