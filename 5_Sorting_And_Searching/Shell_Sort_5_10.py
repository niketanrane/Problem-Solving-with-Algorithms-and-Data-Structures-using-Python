__author__ = "niketanrane"

def gapInsertionSort(aList, start, gap):
    for index in range(start + gap, len(aList), gap):
        currentValue = aList[index]
        currentPos = index - gap
        while currentPos >= start and aList[currentPos] > currentValue:
            aList[currentPos + gap] = aList[currentPos]
            currentPos -= gap
        aList[currentPos + gap] = currentValue

    print("After this iteration list is", aList)


def shellSort(aList):
    sublistcount = len(aList) // 2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(aList, startposition, sublistcount)

      print("After increments of size", sublistcount, "The list is",aList)

      sublistcount = sublistcount // 2

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

'''
Note: We can say that big O-h tends to fall somewhere between O(n) and O(n2). For the increments 
shown in Listing 5, the performance is O(n^2). By changing the increment, for example using 2k−1 (1, 3, 7, 15, 31, and so on), 
a shell sort can perform at O(n^(1.5)).
'''