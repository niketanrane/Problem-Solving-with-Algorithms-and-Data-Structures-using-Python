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

def decToBase(n, base):
    digits = "0123456789ABCDEF"

    st = Stack()
    while n > 0:
        st.push(n % base)
        n //= base

    binary = ''
    while not st.isEmpty():
        binary += str(digits[st.pop()])

    return binary

print("Binary: ", decToBase(42, 2))
print("Octal: ", decToBase(25, 8))
print("Hexadecimal: ", decToBase(256, 16))
print("Decimal: ", decToBase(42, 10))
