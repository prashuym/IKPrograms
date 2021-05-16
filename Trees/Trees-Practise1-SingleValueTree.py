"""
https://oj.interviewkickstart.com/view_test_problem/16069/45/
Given a binary tree, find the number of unival subtrees. An unival tree is a tree that has the same value in every node.
"""
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def findSingleValueTrees(root):
    if root == None : return 0
    univals = 0
    def singleValueHelper(node):
        nonlocal univals
        # Leaf condition
        if node.left_ptr == None and node.right_ptr == None :
            univals += 1
            return True
        # Regular node
        LH = RH = True
        if node.left_ptr : LH = singleValueHelper(node.left_ptr) and node.val == node.left_ptr.val
        if node.right_ptr : RH = singleValueHelper(node.right_ptr) and node.val == node.right_ptr.val
        if LH and RH :
            univals += 1
            return True
        return False
    singleValueHelper(root)

    return univals
