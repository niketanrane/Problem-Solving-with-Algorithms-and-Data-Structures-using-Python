__author__ = "niketanrane"

class HashTable:
    '''
    Implementing the "MAP" avstract data type
    '''
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def hashFunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def put(self, key, data):
        hashValue = self.hashFunction(key)

        if self.slots[hashValue] == None:
            # Key slot is empty, Add straightaway
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                #replace data
                self.data[hashValue] = data
            else:
                #print("Collision and process for", data)
                hashValue = self.rehash(hashValue)
                while self.slots[hashValue] != None and self.slots[hashValue] != key:
                    #print("hashValue is ", hashValue)
                    hashValue = self.rehash(hashValue)

                if self.slots[hashValue] == None:
                    self.slots[hashValue] = key
                    self.data[hashValue] = data
                else:
                    #Need to replace the data for that key, as key already exists
                    #print("Replacing", self.data[hashValue], "with", data)
                    self.data[hashValue] = data

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        startSlot = self.hashFunction(key)

        currentSlot = startSlot
        while self.slots[currentSlot] != None:
            if self.slots[currentSlot] == key:
                return self.data[currentSlot]
            else:
                currentSlot = self.rehash(currentSlot)
                if currentSlot == startSlot:
                    break

        return None

    def __getitem__(self, item):
        return self.get(item)




H = HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
