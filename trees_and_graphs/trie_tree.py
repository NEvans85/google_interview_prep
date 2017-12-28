"""
A trie tree (trie from re-trie-val) is commonly used to hold a collection
of words. The benefit of a trie is that checking for inclusion of a word
happens in O(L) where L is the length of the word. It is also good for
finding all words which start with a given prefix for features like
autocomplete.
The following implementation uses a Trie class and a Node class.
THe Node class can fetch it's children by a value (returning False if the
child is non-existant), add a new child node (returning the new child),
and fetch all suffixes which branch from it (using a BFS through it's
descendents).
The Trie class starts with a blank node (with a value of "_") and can
add words (or a list of words) using the Node class' methods: getChild
(to find the last existing node with the word's characters) and addChild
(to append new nodes for the remaining characters). It can also find all
words with a given prefix by traversing the Trie through the characters
in a given string then using the Node's findSuffixes method.

"""

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
