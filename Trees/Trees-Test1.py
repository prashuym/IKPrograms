"""
Kth Smallest Element Of BST
"""
'''
    For your reference:
'''
class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
import sys
def kth_smallest_element(root, k):
    if root == None : return 0
    count = 0
    def smallestHelper(node, k) :
        nonlocal count
        # Beyond leaf node
        if node == None : return
        # Other nodes
        LH = smallestHelper(node.left_ptr,k)
        if LH != None : return LH
        count += 1
        if k == count : return node.val
        RH = smallestHelper(node.right_ptr,k)
        if RH != None : return RH
        return
    return smallestHelper(root, k)

c = TreeNode("3")
b = TreeNode("1")
a = TreeNode("2")
a.left_ptr=b
a.right_ptr = c
print (kth_smallest_element(a,3))