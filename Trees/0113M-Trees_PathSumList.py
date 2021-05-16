"""
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None : return []
        result = []
        
        def dfs(node, slate, target):
            slate.append(node.val)
            target-=node.val
            # Base condition
            if node.left == node.right == None :
                if target == 0 : 
                    result.append(slate[:])
                
            # Recursion condition
            if node.left :
                dfs(node.left, slate, target)
            if node.right :
                dfs(node.right, slate, target)
            slate.pop()
            return 
        
        dfs(root, [], sum)
        return result
        