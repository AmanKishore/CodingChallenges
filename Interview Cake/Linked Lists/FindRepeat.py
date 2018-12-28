'''
Find Repeat
    We can find a duplicate integer in O(n) time while keeping our space cost at O(1).
'''

def find_duplicate(listi):
    n = len(listi) - 1

    # STEP 1: GET INSIDE A CYCLE
    # Start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    pos = n + 1
    for _ in range(n):
        pos = listi[pos - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a listi is *index* 1

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # Find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    pos_cycle = pos
    curr_pos = listi[pos - 1]  # 1 step ahead
    cycle_size = 1

    while curr_pos != pos_cycle:
        curr_pos = listi[curr_pos - 1]
        cycle_size += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # Start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    slow = n + 1
    fast = n + 1
    for _ in range(cycle_size):
        fast = listi[fast - 1]

    # Advance until the pointers are in the same position
    # which is the first node in the cycle
    while slow != fast:
        slow = listi[slow - 1]
        fast = listi[fast - 1]

    # Since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our listi
    return slow


