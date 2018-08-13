__author__ = "niketanrane"

def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


def shortBubbleSort(aList):
    #It will check if at current pass whether we have done at least one exchange, if not list is sorted. -> STOP
    for passnum in range(len(aList) - 1, 0, -1):
        exchanged = False
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                exchanged = True
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
        if exchanged == False:
            print(passnum)
            break

aList = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(aList)
print(aList)

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
