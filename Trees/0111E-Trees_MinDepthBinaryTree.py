"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> List[List[int]]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return 0
        q = deque([root])
        level = 0
        while q :
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                if node.left == node.right == None :
                    return level+1
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            
            level += 1
            
        return level
