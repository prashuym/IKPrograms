"""
https://oj.interviewkickstart.com/view_test_problem/16069/63/
Print All Paths of a Tree
Given a binary tree, return all paths from root to leaf.
"""
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: A list of integer lists denoting the node values of the paths of the tree

def allPathsOfABinaryTree(root):
    if root == None : return []
    result = []
    def pathHelper(node, slate):
        # Leaf node
        if node.left_ptr == node.right_ptr == None:
            result.append (slate + [node.val])
            return
        # Intermediate Node
        slate.append(node.val)
        if node.left_ptr : pathHelper(node.left_ptr, slate)
        if node.right_ptr: pathHelper(node.right_ptr, slate)
        slate.pop()
        return

    pathHelper(root, [])
    return result