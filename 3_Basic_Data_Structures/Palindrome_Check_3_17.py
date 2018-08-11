__author__ = "niketanrane"

class Dequeue:
    '''
    Dequeue implementation in Python
    '''
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def addFront(self, value):
        self.items.append(value)

    def addRear(self, value):
        self.items.insert(0, value)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

def palChecker(aString):
    deq = Dequeue()

    for ch in aString:
        deq.addRear(ch)

    flag = True
    while deq.size() > 1:
        front  = deq.removeFront()
        rear = deq.removeRear()
        if front is not rear:
            flag = False
            break

    return flag == True

print(palChecker("lsdkjfskf"))
print(palChecker("radar"))
print(palChecker("a"))


