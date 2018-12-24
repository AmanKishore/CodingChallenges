'''
Reroll Die
    Simulate Die
'''
from random import randint

def rand5():  # Simulate a 5 sided die using a 7 sided die
    roll = randint(0, 7)
    if roll <= 5:
        return roll 
    else:
        rand5()

def rand7():  # Simulate a 7 sided die using 5 sided die
    while True:
        roll1 = randint(0, 5)
        roll2 = randint(0, 5)
        outcome_number = (roll1-1) * 5 + (roll2-1) + 1  # Numbers between 1 and 25

        if outcome_number > 21: # Re-roll
            continue

        return outcome_number % 7 + 1
