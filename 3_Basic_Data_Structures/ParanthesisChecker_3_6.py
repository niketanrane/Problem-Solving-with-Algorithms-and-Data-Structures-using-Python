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
        if ch in "({[":
            st.push(ch)
        elif ch in ")}]":
            if st.isEmpty():
                break
            else:
                top = st.pop()
                if not matches(top, ch):
                    break

    else:
        # no break
        if not st.isEmpty():
           return False
        return True
    return False

def matches(c1, c2):
    opening = "([{"
    closing = ")]}"
    return opening.index(c1) == closing.index(c2)

print(parChecker("()"))