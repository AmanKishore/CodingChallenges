'''
Tower of Hanoi:
    Solve the tower hanoi
'''


def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper) # move tower of size n - 1 to helper:
        if source: # move disk from source peg to target peg
            target.append(source.pop())
        hanoi(n - 1, helper, source, target) # move tower of size n-1 from helper to target
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)
