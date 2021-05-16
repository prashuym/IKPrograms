"""
https://oj.interviewkickstart.com/view_test_problem/16069/65/
Find the lowest common ancestor (LCA) of two nodes in a binary tree of n nodes. Given references to the root node and nodes a and b of the tree, return the value from the LCA node of a and b.
The LCA of nodes a and b in a tree is defined as the shared ancestor node of a and b that is located farthest from the root.

Example
Input: a=8, b=9.
Output: LCA(8, 9)=5
There are three shared parents of 8 and 9 in this tree: 5, 2, 1. Of those three, the farthest from the root is 5.

Other examples:
LCA(2,5) = 2
LCA(2,3) = 1
"""

#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

import sys
def lca(root, p, q):
    if root == None : return None
    lca = [None]
    def lcaHelper(node, p, q):
        if lca[0] != None : return False
        found = False

        # Beyond Leaf node
        if node == None : 
            return False
        
        LH = RH = False
        # Normal tree element
        if node.left :
            LH = lcaHelper(node.left, p, q)
        if node.right : 
            RH = lcaHelper(node.right, p, q)

        if (LH == RH == True) or ( (LH or RH) and (node.val == p.val or node.val == q.val)): 
            lca[0] = node
        
        return LH 

    lcaHelper(root, p, q)
    return lca[0]