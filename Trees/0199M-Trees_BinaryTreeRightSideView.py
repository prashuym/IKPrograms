'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[float]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return []
        result = []
        q = deque([root])
        while q :
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            
            result.append(node.val)
            
        return result