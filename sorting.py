
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

def shellSort(arr):
  
    comparisons = 0
    assignments = 0
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = int(n/2)
    gap = int(gap)

    assignments += 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
        comparisons += 1
  
        for i in range(gap,n):
            comparisons += 1
  
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
  
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i

            assignments+=2

            comparisons += 2
            while  j >= gap and arr[j-gap] >temp:

                comparisons += 2
                assignments += 2

                arr[j] = arr[j-gap]
                j -= gap
  
            assignments+=1

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        
        assignments+=1
        gap /= 2
        gap = int(gap)
    
    return arr, comparisons, assignments

def shannonSort(arr):
    comparions = 0
    assignments = 0
    loopcompare = 0
    loopassign = 0

    div5 = int(len(arr)/5)
    rem =  len(arr) % 5

    rowSortedList = []

    looplist = []

    # sort list by mulitiple of 5 lists
    for i in range (0,div5):
        looplist, loopcompare, loopassign = insertionSort(arr[i*5:i*5 + 4])
        rowSortedList += looplist
        comparions += loopcompare
        assignments += loopassign
    
    if rem > 1:
        looplist, loopcompare, loopassign = insertionSort(arr[-rem:])
        rowSortedList += looplist
        comparions += loopcompare
        assignments += loopassign

    threeSortedList = []

    #  sort list by 3 lists
    div3 = int(len(arr)/3)
    for i in range (0,1):
        looplist, loopcompare, loopassign = insertionSort(arr[div3*i:div3*i+div3])
        threeSortedList += looplist
        comparions += loopcompare
        assignments += loopassign

    looplist, loopcompare, loopassign = insertionSort(arr[2*div3:])
    threeSortedList += looplist
    comparions += loopcompare
    assignments += loopassign

    finalSortedList = []
    finalSortedList, loopcompare, loopassign = insertionSort(threeSortedList)
    comparions += loopcompare
    assignments += loopassign

    return finalSortedList, comparions, assignments