# Python program for implementation of Insertion Sort
  
# Function to do insertion sort
def insertionSort(arr):
  
    comparisons = 0
    assignments = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        comparisons += 1
        assignments += 2

        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            comparisons += 2
            assignments += 2
            arr[j+1] = arr[j]
            j -= 1
        assignments+=1
        arr[j+1] = key
    
    return arr, comparisons, assignments
