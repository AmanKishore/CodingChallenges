'''
Eight Queens:
    Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that
    none of them share the same row, column or diagonal. In this case, "diagonal" means all
    diagonals, not just the two that bisect the board.
'''

def n_queens(n):
    ways = list()
    helper(n, 0, list(), ways)
    return ways

def helper(n, c, queens, ways):
    if c == n: # Number of queens reached
        ways.append(queens)
        return None
    for r in range(n):
        position = [r, c]
        if is_valid(position, queens): # Checks to see if there are any queens in the same row or columns or diagonal
            queens_cp = queens.copy() # Makes a shallow copy so that queens and queens_cp don't point to the same memory
            queens_cp.append(position)
            helper(n, c+1, queens_cp, ways)

def is_valid(position, queens):
    for queen in queens:
        if queen[0] == position[0]: # Checks row
            return False
        if queen[1] == position[1]: # Checks column
            return False
        if (abs(queen[0] - position[0]) == abs(queen[1] - position[1])):  # Checks diagonal
            return False
    return True
