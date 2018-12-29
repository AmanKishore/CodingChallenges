'''
Group Anagrams:
    Write a method to sort an array of strings so that all of the anagrams are next to each other.
'''

def GroupAnagrams(strings):
    anagrams = {}
    for i in range(len(strings)):
        key = "".join(sorted(strings[i].lower())) # get the key by sorting the string
        if key not in anagrams: # Check if dictionary has the key
            anagrams[key] = [] # Add the key with a list
        anagrams[key].append(strings[i]) # Add the string to the list
    keys = anagrams.keys()
    index = 0 
    for i in range(len(keys)): # Build the sorted list 
        values = anagrams.get(keys[i]) 
        for j in range(len(values)): # Looping through every value in the key list
            strings[index] = values[j]
            index += 1
    return strings