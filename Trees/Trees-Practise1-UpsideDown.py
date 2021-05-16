'''
https://oj.interviewkickstart.com/view_test_problem/16069/110/
Upside Down
Given a binary tree where every node has either 0 or 2 children and every right node is a leaf node, flip it upside down turning it into a binary tree where all left nodes are leafs.
'''
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
import sys
def printTree (node) :
    while node :
        print (f"Node : {node.val}, left : {node.right_ptr}, left : {node.right_ptr}", file=sys.stderr)
        node = node.left_ptr

def flipUpsideDown(root):
    if root == None : return None
    printTree(root)
    newHead = None
    def flipHelper(node):
        nonlocal newHead
        # Bottom leaf node becomes head
        if node.left_ptr == None :
            newHead = node
            return

        flipHelper(node.left_ptr)
        node.left_ptr.left_ptr=node.right_ptr
        node.left_ptr.right_ptr=node
        node.left_ptr = node.right_ptr = None

    printTree(newHead)
    flipHelper(root)

    return newHead