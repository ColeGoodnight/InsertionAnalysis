import random

def generateSorted(n):
    retList = []
    for i in range(0,n):
        retList.append(i)
    return retList

def generateReverseSorted(n):
    retList = []
    for i in range(0,n):
        retList.append(n-i)
    
    return retList

# sort is a percentage value to determine 
# where the sorted array will be split for shuffling
def generateRandomPercentageSorted(n, sort):
    retList = []
    retList = generateSorted(n)
    split = int(n*sort)+1
    copy = retList[:split]
    random.shuffle(copy)
    retList[:split] = copy
    return retList

def generatePercentageSorted(n, sort):
    retList = []
    retList = generateSorted(n)
    split = int(n*sort)+1
    retList[:split] = retList[:split][::-1]
    return retList

def generateRandomSorted(n):
    retList = []
    retList = generateSorted(n)
    random.shuffle(retList)
    return retList