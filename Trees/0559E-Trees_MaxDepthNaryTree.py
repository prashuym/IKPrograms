"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None : return 0
        q = deque([root])
        level = 0
        while q :
            level += 1
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                for n in node.children :
                    q.append(n)
            
        return level
