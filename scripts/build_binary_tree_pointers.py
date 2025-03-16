"""
This script contains the code needed to build a binary tree from preorder 
and inorder traversal lists using pointers and a dictionary.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        memory = {}

        for i, e in enumerate(inorder):
            memory[e] = i
        
        root = self.helper(preorder, inorder, 0, len(inorder), memory)

        return root
    
    def helper(self, preorder, inorder, left_pointer, right_pointer, memory):

        if left_pointer >= right_pointer:
            return None

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)

        root.left = self.helper(preorder, inorder, left_pointer, idx, memory)
        root.right = self.helper(preorder, inorder, idx + 1, right_pointer, memory)

        return root