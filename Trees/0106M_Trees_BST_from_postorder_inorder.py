"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
106. Construct Binary Tree from Inorder and Postorder Traversal

Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if postorder == [] : return None
        inorderMap = {}
        for i,x in enumerate(inorder): inorderMap[x] = i
        def buildTreeHelper(startP, endP, startI, endI):
            # Leaf node
            if startP > endP : return
            if startP == endP :
                newNode = TreeNode(val=postorder[startP])
                return newNode

            # Intermediate node
            idx = inorderMap[postorder[endP]]
            leftNode = buildTreeHelper(startP, startP + (idx - startI) - 1, startI, idx - 1)
            rightNode = buildTreeHelper(startP + (idx - startI), endP-1, idx + 1, endI)
            rootNode = TreeNode(postorder[endP], leftNode, rightNode)
            return rootNode

        return buildTreeHelper(0, len(postorder)-1, 0, len(inorder)-1)

if __name__ == "__main__" :
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    soln = Solution()
    root = soln.buildTree(inorder, postorder)
    print (root.val, root.left.val, root.right.val)