__author__ = "niketan"

def sequentialSearchOrdered(orderedList, item):
    '''

    :param aList: Ordered List in which to search
    :param item: Item to search
    :return: boolean, if item is present or not
    '''
    pos = 0
    found = False

    while pos < len(orderedList) and orderedList[pos] <= item:
        if orderedList[pos] == item:
            return True
        pos += 1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearchOrdered(testlist, 32))
print(sequentialSearchOrdered(testlist, 3))