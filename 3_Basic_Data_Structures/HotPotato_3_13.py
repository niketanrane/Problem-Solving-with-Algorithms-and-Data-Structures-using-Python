__author__ = "niketanrane"

class Queue:
    '''
    A queue class implementation in Python
    '''
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

def hotPotato(nameList, num):
    q = Queue()

    for name in nameList:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            front = q.dequeue()
            q.enqueue(front)

        q.dequeue()

    return q.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))