class Node:
    def __init__(self, data):
        self.data = data
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

    def findSuffixes(self):
        queue = [[child, ""] for child in self.children]
        results = []
        while len(queue) > 0:
            currNode, currStr = queue.pop(0)
            if currNode.data == "$":
                results.append(currStr)
            else:
                nextStr = currStr + currNode.data
                queue += [[child, nextStr] for child in currNode.children]
        return results

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

    def findWords(self, prefix):
        currNode = self.root
        for ch in prefix:
            nextNode = currNode.getChild(ch)
            if nextNode:
                currNode = nextNode
            else:
                return []
        suffixes = currNode.findSuffixes()
        return [prefix + suffix for suffix in suffixes]
