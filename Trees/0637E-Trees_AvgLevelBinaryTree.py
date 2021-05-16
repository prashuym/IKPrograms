'''
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        '''
        root :  Rood node of the tree
        '''
        if root == None : return []
        result = []
        q = deque([root])
        while q :
            sumRes = 0
            numNodes = len(q)
            for _ in range(numNodes) :
                node = q.popleft()
                # if N-ary array : for n in node.children : 
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                sumRes += node.val
            
            result.append(sumRes/numNodes)
            
        return result
