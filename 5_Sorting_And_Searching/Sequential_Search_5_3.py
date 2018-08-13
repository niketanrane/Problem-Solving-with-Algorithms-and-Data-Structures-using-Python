__author__ = "niketan"

def sequentialSearch(aList, item):
    '''
    :param aList: List in which to search
    :param item: Item to search
    :return: boolean, if item is present or not
    '''
    pos = 0
    found = False

    while pos < len(aList):
        if aList[pos] == item:
            return True
        pos += 1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 32))
print(sequentialSearch(testlist, 3))
