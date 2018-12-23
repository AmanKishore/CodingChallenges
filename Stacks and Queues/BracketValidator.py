'''
Bracket Validator
    Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
'''

def is_valid(inputs):
    paren_map = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    openers = set(paren_map.keys())
    closers = set(paren_map.values())

    ostack = []
    for char in inputs:
        if char in openers:
            ostack.append(char)
        elif char in closers:
            if not ostack:
                return False
            else:
                if not paren_map[ostack.pop()] == char: # Checks to make sure that popped corresponds to push
                    return False

    return not ostack


