"""
This script contains the implmentation of constructing a binary tree
from an inorder traversal list.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bst_from_preorder(self, preorder: List[int]) -> TreeNode:
        """
        This function constructs a binary tree from a preorder traversal list.
        """

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            if preorder[i] < stack[-1].val:
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()
                node = TreeNode(preorder[i])
                pop.right = node
                stack.append(node)
                
        return root