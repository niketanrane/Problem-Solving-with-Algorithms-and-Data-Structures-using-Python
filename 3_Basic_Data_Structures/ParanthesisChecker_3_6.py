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

def parChecker(symbolString):
    st = Stack()
    for ch in symbolString:
        if ch == "(":
            st.push(ch)
        elif ch == ")":
            if st.isEmpty():
                break
            else:
                st.pop()
    else:
        # no break
        if not st.isEmpty():
           return False
        return True
    return False

print(parChecker("(())(54ghh45t5re())(())"))