'''
Single Riffle Shuffle:
    Write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2. 
    Input:  ([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
    Output: true
'''

def is_single_riffle(half1, half2, shuffled_deck):
    idx1, idx2 = 0, 0

    for card in shuffled_deck:
        if idx1 <= len(half1) - 1 and card == half1[idx1]: # Top card is in half1
            idx1 += 1
        elif idx2 <= len(half2) - 1 and card == half2[idx2]: # Top card is in half2
            idx2 += 1
        else:  # If the top card in shuffled_deck doesn't match the top
            return False
    return True