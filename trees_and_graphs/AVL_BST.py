"""
The AVL tree, named for its inventors Adelson-Velsky and Landis, is a self
balancing binary search tree. Each node is given a balance factor which
is the difference between the heights of its left and right branches. If
this factor is ever greater than 1 (or less than -1) for a node the
branches are rotated around that node. Rotations are made when any
modification to the tree results in this inbalance.
"""

# This implementation could be optimized by storing the height on the
# Node rather than calculating height each time.

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value, root = None):
        if not root:
            root = self.root
        if root:
            if root.data < value:
                if root.right:
                    self.insert(value, root.right)
                else:
                    root.right = self.Node(value, root)
            else:
                if root.left:
                    self.insert(value, root.left)
                else:
                    root.left = self.Node(value, root)
            self.balance(root)
        else:
            self.root = self.Node(value)

    def delete(self, value):
        toRemove = self.findNode(value)
        if toRemove:
            

    def findNode(self, value):
        currNode = self.root
        while currNode:
            if currNode.data == value:
                return currNode
            elif value > currNode.data:
                currNode = currNode.right
            else:
                currNode = currNode.left
        return False

    def balance(self, root):
        diff = root.heightDiff()
        if diff > 1:
            if root.left.heightDiff() == -1:
                self.rotateLeft(root.left)
            self.rotateRight(root)
        elif diff < -1:
            if root.right.heightDiff() == 1:
                self.rotateRight(root.right)
            self.rotateLeft(root)

    def rotateLeft(self, root):
        root.right.parent = root.parent
        root.parent = root.right
        root.right = root.right.left

    def rotateRight(self, root):
        root.left.parent = root.parent
        root.parent = root.left
        root.left = root.left.right

    class Node:
        def __init__(self, data, parent = None):
            self.data = data
            self.parent = parent
            self.left = None
            self.right = None

        def height(self):
            return max(self.childHeights())

        def childHeights(self):
            leftH = 0
            rightH = 0
            if self.left:
                leftH = 1 + self.left.height()
            if self.right:
                rightH = 1 + self.right.height()
            return [leftH, rightH]

        def heightDiff(self):
            leftH, rightH = self.childHeights()
            return leftH - rightH
