"""
This script contains the implementation of a binary tree inversion.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """
        Invert a binary tree.
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left) # Tunnel through left side of tree
        self.invert_tree(root.right) # Tunnel through right side of tree