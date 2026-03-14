#Simple Hash Table
class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index] = key

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])

h = HashTable()

h.insert(10)
h.insert(20)
h.insert(25)

h.display()