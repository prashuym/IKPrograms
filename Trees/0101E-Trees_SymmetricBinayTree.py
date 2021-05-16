"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None : return True
        elif root.left == root.right == None : return True
        elif root.left == None or root.right == None : return False
        p = root.left
        q = root.right
        
        queue = deque([(p,q)])
        while queue :
            numNodes = len(queue)
            for _ in range(numNodes) :                  
                nodeP, nodeQ = queue.popleft()
                if (nodeP.val != nodeQ.val) : return False
                if nodeP.left != None and nodeQ.right != None : 
                    queue.append((nodeP.left, nodeQ.right))
                elif nodeP.left != None or nodeQ.right != None : 
                    return False
                
                if nodeP.right != None and nodeQ.left != None : 
                    queue.append((nodeP.right, nodeQ.left))
                elif nodeP.right != None or nodeQ.left != None : 
                    return False
                
        return True       