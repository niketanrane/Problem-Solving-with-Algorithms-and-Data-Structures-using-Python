__author__ = "niketanrane"

def selectionSort(aList):
    #Due to the reduction in the number of exchanges(we only exchange once per pass), the selection sort typically executes faster than bubble sort.
    #in bubble sort, we exchange at each step. Here we remember the largest and swap with the last value.
    for passnum in range(len(aList) - 1, 0, -1):
        currentMaxIndex = 0
        for i in range(1, passnum+1):
            if aList[i] > aList[currentMaxIndex]:
                currentMaxIndex = i
        aList[currentMaxIndex], aList[passnum] = aList[passnum], aList[currentMaxIndex]


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)