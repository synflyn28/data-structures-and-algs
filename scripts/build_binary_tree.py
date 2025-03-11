"""
This script contains the code needed to build a binary tree from preorder 
and inorder traversal lists.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Build a binary tree from preorder and inorder traversal lists.
        """

        if len(inorder) == 0:
            return None

        if len(preorder) == 0:
            return TreeNode(preorder[0])
        

        ind = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[ind])

        node.left = self.build_tree(preorder, inorder[:ind])
        node.right = self.build_tree(preorder, inorder[ind+1:])
        
    