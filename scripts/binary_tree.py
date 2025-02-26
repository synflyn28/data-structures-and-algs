"""
This module contains the implementation of a binary tree.
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        
    def peek(self):
        if len(self.items) > 0:
            return self.items[0].value
        
    def __len__(self):
        return len(self.items)
    

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, start, traversal):
        if start is None:
            return

        traversal.append(start.value)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        return traversal
    
    def inorder(self, start, traversal):
        if start is None:
            return
        
        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)

        return traversal
    
    def postorder(self, start, traversal):
        if start is None:
            return
        
        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)

        return traversal

    def levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal


if __name__ == "__main__":
    tree = BinaryTree(3)
    tree.root.left = Node(4)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(7)
    tree.root.right = Node(5)

    print(tree.preorder(tree.root, []))
    print(tree.inorder(tree.root, []))
    print(tree.postorder(tree.root, []))
    print(tree.levelorder(tree.root))
