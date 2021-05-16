'''
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[float]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return []
        result = []
        q = deque([root])
        while q :
            maxS = float("-inf")
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                maxS = max(maxS, node.val)
            
            result.append(maxS)
            
        return result