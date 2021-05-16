"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
 Return False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root) -> bool:
        if root == None : return True
        isBalance = [True]
        def dfs (node):
            if isBalance[0] == False : return 0
            # Base condition
            if node.left == node.right == None :
                return 1

            leftheight = rightheight = 0
            if node.left :
                 leftheight = dfs(node.left) 
            if node.right :
                 rightheight = dfs(node.right) 
            
            #print (f"{node.val} - {leftheight} - {rightheight} - {abs(leftheight - rightheight)}")
            if abs(leftheight - rightheight) > 1 :
                isBalance[0] = False
            return max(leftheight, rightheight) + 1

        dfs (root)
        return isBalance[0]

if __name__ == "__main__":
    nodes = [1,2,2,3,3,None,None,4,4]
    from LeetcodeTreeCreate import createNodes
    root = createNodes(nodes)
    
    soln = Solution()
    result = soln.isBalanced(root)
    print (f"Result = {result}")