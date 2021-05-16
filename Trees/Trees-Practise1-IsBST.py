"""
https://oj.interviewkickstart.com/view_test_problem/16069/46/
Is It A BST
Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.
Consider the below definition of a BST:

All nodes values of left subtree are less than or equal to parent node value
All nodes values of right subtree are greater than or equal to parent node value
Both left subtree and right subtree must be a BST
By definition, NULL tree is a BST
By definition, tree having a single node or leaf nodes are BST
"""


# class TreeNode():
#    def __init__(self, val=None, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

# complete the function below

def isBST(root):
    if root == None: return True
    BSTFlag = [True]
    prev_value = float("-inf")
    def isBSTHelper(node):
        nonlocal prev_value
        print (f"1. {node.val} : {node.left} {prev_value} {BSTFlag}")
        if BSTFlag[0] == False : return False

        # Normal node
        if node.left : 
            LH = isBSTHelper(node.left)
            if LH == False : 
                BSTFlag[0] == False
                return False
        print (f"Comparing - {node.val} <= {prev_value}")
        if node.val <=  prev_value : 
            BSTFlag[0] == False
            return False
        prev_value = node.val
        print (f"3. {node.val} : {node.left} {prev_value} {BSTFlag}")
        if node.right :
            RH = isBSTHelper(node.right)
            if RH == False : 
                BSTFlag[0] == False
                return False
        return True

    return isBSTHelper(root)

if __name__ == "__main__":
    nodes = [3,1,5,None,None,4,6]
    nodes = [1,1,None]
    from LeetcodeTreeCreate import createNodes
    root = createNodes(nodes)
    
    result = isBST(root)
    print (f"Result = {result}")