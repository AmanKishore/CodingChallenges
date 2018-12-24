'''
Reroll Die
    Simulate Die
'''


def rand5():
    roll = rand7()
    if roll <= 5:
        return roll 
    else:
        rand5()
    