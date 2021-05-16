"""
958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root == None: return 0
        q = deque([(root, 1)])
        nodeNum = 1
        while q:
            nextq = deque([])
            for node, num in q:
                if num != nodeNum : return False
                nodeNum += 1
                if node.left: nextq.append((node.left, 2 * num))
                if node.right: nextq.append((node.right, 2 * num + 1))
            q = nextq

        return True
        