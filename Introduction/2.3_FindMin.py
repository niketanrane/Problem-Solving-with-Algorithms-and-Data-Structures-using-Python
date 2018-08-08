__author__ = 'niketanrane'

import random
import time

def findMinQuad(arr):
    minSoFar = arr[0]
    for i in arr:
        minElem = True
        for j in arr:
            if i > j:
                minElem = False
        if minElem:
            minSoFar = i
    return minSoFar


def findMinLin(arr):
    minSoFar = arr[0]
    for i in arr:
        if i < minSoFar:
            minSoFar = i
    return minSoFar

for listSize in range(10000, 100001, 10000):
    arr = [random.randrange(10000) for x in range(listSize)]
    start = time.time()
    #print(findMinQuad(arr))
    print(findMinLin(arr))
    end = time.time()
    print("%d %f" %(listSize, end - start))