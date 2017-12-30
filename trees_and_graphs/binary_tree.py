"""
A Binary tree is on in which nodes have, at most, two children. These
children are often stored in a left and right attribute.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
