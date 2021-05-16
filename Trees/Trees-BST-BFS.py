# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None : return
        queue = [root]
        result = []
        while queue :
            numLevel = len(queue)
            temp = []
            for i in range(numLevel):
                node = queue.pop()
                temp.append(node.val)
                if node.left : queue.insert(0,node.left)
                if node.right : queue.insert(0,node.right)
            result.append(temp)
        return result

    def levelOrderIter(self, root: TreeNode) -> List[List[int]]:
        if root == None: return

        def levelOrderHelper(queue, level):
            if queue == []: return

            newqueue = []
            level_result = []
            for node in queue:
                level_result.append(node.val)
                if node.left: newqueue.append(node.left)
                if node.right: newqueue.append(node.right)
            result.append(level_result)
            levelOrderHelper(newqueue, level + 1)

        queue = [root]
        result = []
        level = 0
        levelOrderHelper(queue, level)
