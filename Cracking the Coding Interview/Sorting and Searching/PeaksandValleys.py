'''
Peaks and Valleys:
    Sort the array into peaks and valleys
'''

def sortInWave(arr, n): 
      
    # Traverse all even elements 
    for i in range(0, n, 2): 
          
        # If current even element is smaller than previous 
        if (i > 0 and arr[i] < arr[i-1]): 
            arr[i], arr[i-1] = arr[i-1], arr[i] 
          
        # If current even element is smaller than next 
        if (i < n-1 and arr[i] < arr[i+1]): 
            arr[i], arr[i+1] = arr[i+1], arr[i] 