class Node:
    def __init__(self, data):
        self.data = value
        self.children = []

    def addChild(self, data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

    def getChild(self, data):
        for child in self.children:
            if child.data == data:
                return child
        return False

class Trie:
    def __init__(self, root = Node("_")):
        self.root = root

    def addWord(self, word):
        currNode = self.root
        word += "$"
        for ch in word:
            nextNode = currNode.getChild(ch)
            if nextNode:
                currNode = nextNode
            else:
                currNode = currNode.addChild(ch)
    def addWordList(self, wordList):
        for word in wordList:
            self.addWord(word)

    def findWords(self, s):
        
