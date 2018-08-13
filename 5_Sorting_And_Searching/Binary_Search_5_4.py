__author__ = "niketan"

def binarySearch(orderedList, item):
    '''
    :param aList: Ordered List in which to search
    :param item: Item to search
    :return: boolean, if item is present or not
    '''
    left = 0
    right = len(orderedList) - 1
    while left <= right:
        mid = (left + right) // 2
        if orderedList[mid] == item:
            return True
        elif orderedList[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 32))
print(binarySearch(testlist, 3))