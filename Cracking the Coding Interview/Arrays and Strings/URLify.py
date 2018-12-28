'''
URLify:
    Write a method to replace all teh spaces in a string with '%20'. The string has sufficient space to hold it
    Input:  "Mr John Smith    "
    Output: "Mr%20John%20Smith"
'''

def URLify(string, length):
    new_index = len(string)

    for i in reversed(range(length)): # Reverses the range
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'  # When you find a space replace it
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]  # Otherwise keep moving the characters 
            new_index -= 1

    return string