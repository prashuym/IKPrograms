'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return []
        result = []
        q = deque([root])
        level = 0
        while q :
            result.append([])
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                result[level].append(node.val)
            
            level += 1
            
        return result
