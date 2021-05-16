'''
Height Of K-Ary Tree
'''
'''
    For your reference:

    class TreeNode:
        def __init__(self):
            self.children = []

'''


# Complete the function below.
import sys
def find_height(root):
    if not root : return 0
    maxCount = 0
    def heightHelper (node, count):
        # print (node.children, count, maxCount, file=sys.stderr)
        nonlocal maxCount
        if not node.children :
            maxCount = max(count, maxCount)
        for c in node.children :
            heightHelper(c, count+1)
    heightHelper(root, 0)
    return maxCount
