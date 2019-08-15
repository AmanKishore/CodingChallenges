'''
Power Set:
    Return the power set of the inputted set.
'''

def getSubsets(sets):
    if len(sets) == 0:
        return [sets]
    b = getSubsets(sets[1:])
    print((b, sets))
    return [[sets[0]] + a for a in b] + b

print(getSubsets([1,2,3]))

    # allsets = []
    # if len(sets) == index:
    #     if [] not in allsets: # base case - add empty set
    #         allsets.append([])
    # else:
    #     allsets = getSubsets(sets, index+1) # Recurse to the end of the array and add the empty set
    #     item = sets[index] # Get element at index
    #     moresets = []
    #     for subset in allsets: # Get all elements at the index
    #         newSets = []
    #         [newSets.append(value) for value in subset if value not in newSets] # Create a new subset with the existing value
    #         newSets.append(item) # Add the new item to the end of the subset
    #         moresets.append(newSets) # Add it to the set of subsets
    #     [allsets.append(value) for value in moresets if value not in newSets] # Add this new set to the total set
    # return allsets