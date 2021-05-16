"""
100. Same Tree
https://leetcode.com/problems/same-tree/
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None : return True
        elif p == None or q == None : return False
        queue = deque([(p,q)])
        while queue :
            numNodes = len(queue)
            for _ in range(numNodes) :                  
                nodeP, nodeQ = queue.popleft()
                if (nodeP.val != nodeQ.val) : return False

                if nodeP.left != None and nodeQ.left != None : 
                    queue.append((nodeP.left, nodeQ.left))
                elif nodeP.left != None or nodeQ.left != None : 
                    return False
                
                if nodeP.right != None and nodeQ.right != None : 
                    queue.append((nodeP.right, nodeQ.right))
                elif nodeP.right != None or nodeQ.right != None : 
                    return False
                
        return True 
