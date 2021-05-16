"""
Trees - Practise Set -2
Clone a Binary Tree
https://oj.interviewkickstart.com/view_test_problem/385/76/
"""
class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: root of the cloned tree

from collections import deque
def cloneTree(root):
    '''
    root :  Rood node of the tree
    '''
    if root == None : return
    newRoot = TreeNode(val=root.val)
    q = deque([(root, newRoot)])
    while q :
        numNodes = len(q)
        for _ in range(numNodes) :                  
            node, cloneNode = q.popleft()
            if node.left_ptr :
                cloneNode.left_ptr = TreeNode(val=node.left_ptr.val)
                q.append((node.left_ptr, cloneNode.left_ptr))
            if node.right_ptr : 
                cloneNode.right_ptr = TreeNode(val=node.right_ptr.val)
                q.append((node.right_ptr, cloneNode.right_ptr))
        
    return newRoot
