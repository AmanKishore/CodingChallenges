'''
One Away:
    There are three types of edits on strings: remove, insert, or replace. Determine if two strings are one away
    Ex: plae, ple -> true
        plae, bae -> false
'''

def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) - len(s2) < 0:
        first, second = s1, s2
    else:
        first, second = s2, s1
    i = j = 0
    foundDiff = False
    while i < len(first) and j < len(second):
        if first[i] != second[j]:
            if foundDiff: # Check to make sure this is the first difference found
                return False
            foundDiff = True
            if len(first) == len(second): # If there is a replace, move the shorter pointer forward
                i += 1
        else:
            i += 1
        j += 1
    return True