'''
Parens:
    Print all valid combos of n parenthesis.
'''

def parens(n):
    if n <= 0:
        return ['']
    else:
        combos = []
        helper('', n, n, combos)
        return combos


def helper(string, left, right, combos):
    if left <= 0 and right <= 0: # If you have run out of open and closed append the combo
        combos.append(string)
    else:
        if left > 0: # If you still have some left
            helper(string + '(', left - 1, right, combos)
        if right > left and right > 0: # If you have more right than left
            helper(string + ')', left, right - 1, combos)
n = 3
print(parens(n))