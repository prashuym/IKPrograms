"""
965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
"""
from collections import deque
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None : return True
        unival = root.val
        q = deque([root])
        while q :
            node = q.popleft()
            if node.val != unival : return False
            if node.left : q.append(node.left)
            if node.right : q.append(node.right)

        return True
