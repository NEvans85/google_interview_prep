"""
Heapsort is performed in O(n * log(n)). In order to maintain this logarithmic 
complexity, a heap is represented as a balanced binary tree. This will be 
maintained by building the heap as a complete binary tree, where all nodes have 
both a left and a right child with the exception of the bottom level which is 
filled from left to right. Due to it's completeness, the elements in a heap can be
represented in a single list. The children of an element (at index p) are at 
indices 2p and 2p + 1; and the parent of any element (at index n) is at index n / 2
(using integer division). The heap's store is initialized with a single value 0 to 
facilitate other operations of the heap. 
Utilizing heapsort involves placing the list of items into a heap, then removing 
the minimum item until all items have been removed.
"""

class BinaryHeap:
    def __init__(self):
        self.store = [0]
        self.currentSize = 0

      
# Insert appends the next value to the end of the store then percelates the value 
# up until the heap satisfies the heap order property (any value is greater than 
# its parent).

    def insert(self, value):
        self.store.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx] < self.store[idx // 2]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2
        
# By maintaining a balanced tree satisfying the heap order property, findng the 
# minimum value is simple it will always be the root and will always be at index 1 
# of the store. A delMin method is necessary for heapsort. It works by removing 
# the minimum value and swapping the last element into the root of the tree, which
# will destroy compliance of the heap order property. Then the new root value is
# percelated down the tree until the heap order property is restored.

    def delMin(self):
        minValue = self.store[1]
        self.store[1] = self.store[self.currentSize]
        self.currentSize -= 1
        self.store.pop()
        self.percDown(1)
        return minValue
    
    def percDown(self, idx):
        while idx * 2 <= self.currentSize:
            sc = self.smallestChild(idx)
            if self.store[idx] > self.store[sc]:
                temp = self.store[idx]
                self.store[idx] = self.store[sc]
                self.store[sc] = temp
            idx = sc
            
    def smallestChild(self, idx):
        if idx * 2 + 1 > self.currentSize:
            return idx * 2
        else:
            if self.store[idx * 2] < self.store[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1

# The buildHeap method assigns the heap's store to the input list of numbers, then 
# calls percDown on the first half of the list. Only the first half needs to be 
# addressed as all others represent leaf nodes in a complete binary tree. This method
# leaves the heap in a state satisfying the heap order property.
            
    def buildHeap(self, iList):
        idx = len(iList) // 2
        self.currentSize = len(iList)
        self.store = [0] + iList[:]
        while (idx > 0):
            self.percDown(idx)
            idx -= 1

def heapSort(iList):
    data = BinaryHeap()
    data.buildHeap(iList)
    result = []
    while len(result) < len(iList):
        result.append(data.delMin())
    return result