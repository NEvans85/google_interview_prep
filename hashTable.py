"""
A hashtable is a data structure which provides constant time complexity for
include, insert, and delete. It is built as a list of lists. When a new element is
added, it's value is hashed then the hashed value determines the index of the 
list in which the element is placed. Since a hashing function is deterministic by
definition, the hash of a value will always be the same and can be used to find 
the location of that value in the hash table in O(1). To avoid clumping of
values at certain indexes (which would increase lookup time), the containing list 
is resized once the hashtable contains a number of elements equal to it's size. 
Although this resizing function takes O(n) time, it need only be performed every n
inserts, resulting in O(1) amortized time complexity.
"""

class HashTable:
    def __init__(self):
        self.size = 8
        self.count = 0
        self.store = [[] for _ in range(self.size)]
    
    def findKey(self, value):
        hv = hash(value)
        return hv % self.size
    
    def insert(self, value):
        if self.count == self.size:
            self.resize()
        self.count += 1
        key = self.findKey(value)
        self.store[key].append(value)
        
    def resize(self):
        self.size = self.size * 2
        self.count = 0
        elements = []
        for li in self.store:
            elements += li
        self.store = [[] for _ in range(self.size)]
        for el in elements:
            self.insert(el)
    
    def include(self, value):
        key = self.findKey(value)
        return value in self.store[key]
    
    def delete(self, value):
        if self.include(value):
            self.store[self.findKey].remove(value)
            return value
        else:
            return False