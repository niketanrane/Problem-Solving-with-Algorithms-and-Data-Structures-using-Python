__author__ = "niketanrane"

class Node:
    '''
    Python implementation of Linked list Node
    '''
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setnext(self, newNext):
        self.next = newNext

class OrderedList:
    def __init__(self):
        #The list class will only have one field. The reference to the first node
        # of list. It does not hold any data
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, newdata):
        current = self.head
        previous = None
        while current is not None:
            if current.data > newdata:
                break
            previous = current
            current = current.next

        if previous == None:
            newNode = Node(newdata)
            newNode.next = self.head
            self.head = newNode
        else:
            newNode = Node(newdata)
            newNode.next = previous.next
            previous.next = newNode

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, searchItem):
        '''
        :param searchItem:
        :return: Position or if not found, returns -1
        '''
        cur = self.head
        pos = 0
        while cur is not None:
            if cur.data == searchItem:
                return pos
            elif cur.data > searchItem:
                break
            pos += 1
            cur = cur.next
        return -1

    def remove(self, removeItem):
        current = self.head
        previous = None
        while current is not None and current.data != removeItem:
            previous = current
            current = current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))