"""
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None : return 0
        result = [0]
        
        def dfs(node, slate, target):
            slate.appendleft(node.val)
            tsum = 0
            for x in slate :
                tsum += x
                result[0] += (tsum == target)
            
            # Recursion condition
            if node.left :
                dfs(node.left, slate, target)
            if node.right :
                dfs(node.right, slate, target)
            # Cleanup slate
            slate.popleft()
            return 
        
        dfs(root, deque(), sum)
        return result[0]
