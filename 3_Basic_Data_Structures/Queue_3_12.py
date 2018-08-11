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


q = Queue()
q.enqueue(4)
q.enqueue("Niketan")
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())