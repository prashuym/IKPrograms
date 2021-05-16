"""
1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> List[float]:
        if root == None : return -1
        result = 0
        maxSum = float("-inf")
        q = deque([root])
        level = 0
        while q :
            level += 1
            sumLevel = 0
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                sumLevel += node.val
            
            if sumLevel > maxSum :
                result = level
                maxSum = sumLevel
            
        return result