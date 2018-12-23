'''
Matching Parenthesis
    Write a function given the position of an opening parenthesis, finds the corresponding closing parenthesis.
'''

def get_closing_paren(input, idx):
    stack = []

    for i in range(idx + 1, len(input)):  # Start right after the index of first one
        if input[i] == '(':
            stack.append(i)
        elif input[i] == ')':
            if len(stack) == 0:
                return i
            else:
                stack.pop()
    return -1