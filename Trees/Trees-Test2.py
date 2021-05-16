# complete this function

'''
    For your reference:
'''
class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

def build_balanced_bst(a):
    if a == [] : return None

    def bstHelper(start, end):
        if start > end : return None

        mid = (start + end) // 2
        LN = bstHelper(start, mid-1)
        RN = bstHelper(mid+1, end)
        newNode = TreeNode(a[mid])
        newNode.left_ptr = LN
        newNode.right_ptr= RN
        return newNode

    return bstHelper(0,len(a)-1)

root = build_balanced_bst([1,2,3,4,5,6,7])

print (root.val, root.left_ptr.val, root.right_ptr.val)
root = root.right_ptr
print (root.val, root.left_ptr.val, root.right_ptr.val)
