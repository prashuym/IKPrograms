"""
https://oj.interviewkickstart.com/view_test_problem/16069/50/
Post-order Traversal of a Tree Without Recursion

Problem Statement:
Write a function to traverse a binary tree Post-order, without using recursion.
"""
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
from collections import deque
def postorderTraversal(root):
    if root == None : return []
    q = deque([root])
    result = deque()
    while (q):
        node = q.pop()
        if node.left_ptr : q.append(node.left_ptr)
        if node.right_ptr : q.append(node.right_ptr)
        result.appendleft(node.val)
    return result