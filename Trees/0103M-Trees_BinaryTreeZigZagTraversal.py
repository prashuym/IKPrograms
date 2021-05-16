'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return []
        result = []
        q = deque([root])
        level = 0
        while q :
            result.append(deque())
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                if level%2 == 0 : result[level].append(node.val)
                else : result[level].appendleft(node.val)
            
            level += 1
            
        return result
