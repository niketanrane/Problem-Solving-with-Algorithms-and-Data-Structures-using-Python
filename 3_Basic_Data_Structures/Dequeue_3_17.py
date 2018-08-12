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


