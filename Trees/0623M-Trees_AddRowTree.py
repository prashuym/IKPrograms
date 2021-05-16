"""
623. Add One Row to Tree
https://leetcode.com/problems/add-one-row-to-tree/
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   
v = 1
d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if root == None : return
        if d == 1 : return TreeNode(val=v, left = root, right = None)

        q = deque([root])
        level = 0
        while q :
            level += 1
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                if level == d-1 :
                    node.left = TreeNode(val=v, left = node.left, right = None)
                    node.right = TreeNode(val=v, left = None, right = node.right)
                # if N-ary array : for n in node.children : 
                else : 
                    if node.left : q.append(node.left)
                    if node.right : q.append(node.right)
            if level == d-1 : break

        return root