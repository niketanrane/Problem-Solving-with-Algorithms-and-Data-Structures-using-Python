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

def infixToPostfix(infixexpr):
    st = Stack()
    infixexpr = infixexpr.split()
    '''
    Setting the precedence of operators
    '''
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    output = []
    for op in infixexpr:
        if op in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            output.append(op)
        elif op == '(':
            st.push(op)
        elif op == ')':
            top = st.pop()
            while top != '(':
                output.append(top)
                top = st.pop()
        elif op in prec:
            while not st.isEmpty() and prec[st.peek()] >= prec[op]:
                output.append(st.pop())
            st.push(op)

    while not st.isEmpty():
        output.append(st.pop())
    return output

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * ( C + D )"))