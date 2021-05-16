'''
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None or x == y: return False
        q = deque([root])
        while q :
            px,py = None, None
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    if node.left.val == x : px = node.val
                    if node.left.val == y : py = node.val
                    q.append(node.left)
                if node.right : 
                    if node.right.val == x : px = node.val
                    if node.right.val == y : py = node.val
                    q.append(node.right)
                if px and py : return px != py
            if px or py : return False

        return False
