def isOrdered(list):
    for previous,current in zip(list, list[1:]):
        if (previous > current):
            return False

    return True