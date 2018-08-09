__author__ = "niketanrane"
class Stack:
    '''
    Stack data structure using Python
    '''
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        pass

    def clear(self):
        self.items = []

    def size(self):
        return len(self.items)

def decToBin(n):
    st = Stack()
    while n > 0:
        st.push(n%2)
        n //= 2

    binary = ''
    while not st.isEmpty():
        binary += str(st.pop())

    return binary

print(decToBin(42))
