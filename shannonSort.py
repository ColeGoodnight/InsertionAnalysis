from insertionSort import insertionSort

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