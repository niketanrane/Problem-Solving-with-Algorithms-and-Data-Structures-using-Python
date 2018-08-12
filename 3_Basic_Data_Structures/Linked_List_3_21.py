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

#temp = Node(93)
#print(temp.getData())

class UnorderedList:
    def __init__(self):
        #The list class will only have one field. The reference to the first node
        # of list. It does not hold any data
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, newdata):
        if self.head is None:
            newNode = Node(newdata)
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                #print(cur.data)
                cur = cur.next
            newNode = Node(newdata)
            cur.setnext(newNode)

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def remove(self, value):
        pass

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



mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))