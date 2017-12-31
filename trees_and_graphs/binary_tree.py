"""
A Binary tree is a tree in which nodes have, at most, two children. These
children are often stored in a left and right attribute.
The Binary Search Tree (BST) is a binary tree in which each node's
left child's data is less that the node's value and the right child's data
is greater.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def bfs(self, target, root = self.root):
        if root:
            queue = [root]
            while len(queue) > 0:
                currNode = queue.pop(0)
                if currNode.data == target:
                    return currNode
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return False

    def dfs(self, target, root = self.root):
        if root:
            if root.data == target:
                return root
            rightResult = self.dfs(target, root.right):
            if rightResult:
                return rightResult
            leftResult = self.dfs(target, root.left):
            if leftResult:
                return leftResult
        return False

    def inOrderTraversal(self, root = self.root):
        results = []
        if root.left:
            results += inOrderTraversal(root.left)
        results.append(root.data)
        if root.right:
            results += inOrderTraversal(root.right)
        return results
