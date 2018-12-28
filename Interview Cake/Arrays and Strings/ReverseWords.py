'''
Reverse Words:
    Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.     
    Input:  [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
    Output:  ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e' ]
'''

def reverse_words(message):
    reverse_characters(message, 0, len(message)-1) # Reverse all the characters

    start = 0

    for i in range(len(message) + 1):   # Reverse each word's characters
        if (i == len(message)) or (message[i] == ' '):  # Reached end of word
            reverse_characters(message, start, i - 1)
            start = i + 1


def reverse_characters(message, left, right):
    while left < right:
        message[left], message[right] = message[right], message[left]  # Swap the left char and right char
        left  += 1
        right -= 1