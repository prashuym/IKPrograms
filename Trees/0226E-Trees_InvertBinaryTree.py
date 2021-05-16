"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.

Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None : return root
        def invertHelper(node):
            if node.left : invertHelper(node.left)
            if node.right : invertHelper(node.right)
            node.left, node.right = node.right, node.left
        
        invertHelper(root)
        return root
        