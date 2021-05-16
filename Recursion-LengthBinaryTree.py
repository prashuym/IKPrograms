class btree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxdepth(node):
    if node == None: return 0, 0
    maxH = minH = 0
    treePaths = []
    def maxdepthHelper(node, level, path):
        nonlocal maxH, minH
        # Base condition
        # print (node.data, node.left, node.right, path, treePaths)
        if node.left == None and node.right == None:
            if level > maxH: maxH = level
            if minH == 0 or level < minH: minH = level
            path.append(node.data)
            treePaths.append(path[:])
            path.pop()
            return

        # Parent - left & right
        path.append(node.data)
        if node.left: maxdepthHelper(node.left, level + 1, path)
        if node.right: maxdepthHelper(node.right, level + 1, path)
        path.pop()
        return

    maxdepthHelper(node, 1, [])
    return maxH, minH, treePaths


root = btree(1)
root.left = btree(2)
root.right = btree(3)
root.left.left = btree(4)
root.left.right = btree(5)
root.left.left.left = btree(6)
root.left.left.left.left = btree(7)
# root = None

print("max and min depth :", maxdepth(root))