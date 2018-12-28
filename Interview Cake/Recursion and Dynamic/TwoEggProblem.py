'''
Two Egg Problem:
    Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.
'''

def eggDrop(n, k): 
    # A 2D table where entery eggFloor[i][j] will represent minimum 
    # number of trials needed for i eggs and j floors. 
    eggFloor = [[0] *(k + 1) for x in range(n+1)] 
  
    for i in range(1, n+1): # We need one trial for one floor and 0 trials for 0 floors 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    for j in range(1, k+1): # We always need j trials for one egg and j floors. 
        eggFloor[1][j] = j 
  
    # Fill rest of the entries in table using optimal substructure 
    # property 
    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = float('inf')
            for x in range(1, j+1): 
                # Max of the number of eggs you need from the xth floor
                # if it does break the problem reduces to x-1 floors and n-1 eggs
                # if it doesn't break, only have to look above, problem reduces to k - x floors and n eggs
                # you can check the max for every floor and choose the one that yields the min
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
  
    # eggFloor[n][k] holds the result 
    return eggFloor[n][k] 
  
# Driver program to test to pront printDups 
n = 2   
k = 36
print("Minimum number of trials in worst case with " + str(n) + " eggs and " 
       + str(k) + " floors is " + str(eggDrop(n, k))) 