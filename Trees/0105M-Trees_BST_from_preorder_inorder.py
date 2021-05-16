"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
105. Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder) -> TreeNode:
        if preorder == [] : return None
        inorderMap = {}
        for i,x in enumerate(inorder): inorderMap[x] = i
        def buildTreeHelper(startP, endP, startI, endI):
            # Leaf node
            if startP > endP : return
            if startP == endP :
                newNode = TreeNode(val=preorder[startP])
                return newNode

            # Intermediate node
            idx = inorderMap[preorder[startP]]
            leftNode = buildTreeHelper(startP + 1, startP + (idx - startI), startI, idx - 1)
            rightNode = buildTreeHelper(startP + (idx - startI) + 1, endP, idx + 1, endI)
            rootNode = TreeNode(preorder[startP], leftNode, rightNode)
            return rootNode

        return buildTreeHelper(0, len(preorder)-1, 0, len(inorder)-1)

if __name__ == "__main__" :
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    soln = Solution()
    root = soln.buildTree(preorder, inorder)
    print (root.val, root.left.val, root.right.val)