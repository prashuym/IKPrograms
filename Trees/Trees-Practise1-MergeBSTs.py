"""
https://oj.interviewkickstart.com/view_test_problem/16069/109/
Given two BSTs (Binary Search Trees), one with N1 number of nodes and other one with N2 number of nodes.
Your task is to merge them such that:
   - Resultant tree is height balanced.
   - Resultant tree is a BST.
   - Resultant tree contains all values from given BST-1.
   - Resultant tree contains all values from given BST-2.
   - Size of the resultant tree is N1 + N2.
   - For any value, no of occurrences in resultant tree = no of occurrences in BST-1 + no of occurrences in BST-2. (If BST-1 contains 3 nodes with value 50 and BST-2 contains 4 nodes with value 50, then resultant tree should contain exactly 7 nodes with value 50.)
Any resultant tree, satisfying all the above conditions will be considered as valid answer.

Constraints:
1 <= N1, N2 <= 100000
Node value of the BSTs: 1 <= key1, key2 <= 1000000000
You are not allowed to modify the structure of the given BST
"""
# Complete this function and return root of the BST
from collections import deque
class Node:
    def __init__(self, node_value):
        self.key = node_value
        self.left = None
        self.right = None

def inOrder(node, allNums):
    # Leaf past node
    if node == None: return
    # Regular node :
    inOrder(node.left, allNums)
    allNums.append(node.key)
    inOrder(node.right, allNums)

def mergeLists(L1, L2):
    M = deque()
    i = 0
    j = 0
    while L1 and L2 :
        if L1[0] <= L2[0]: M.append(L1.popleft())
        else : M.append(L2.popleft())
    if L1: M.extend(L1)
    if L2: M.extend(L2)
    return M

def BSTfromList(allKeys, start, end):
    if start > end : return
    print (allKeys, start, end)
    mid = (start + end) // 2
    LN = BSTfromList(allKeys, start, mid-1)
    RN = BSTfromList(allKeys, mid+1, end)
    newNode = Node(allKeys[mid])
    newNode.left = LN
    newNode.right = RN
    return newNode


def mergeTwoBSTs(root1, root2):
    node1keys = deque()
    inOrder(root1, node1keys)
    node2keys = deque()
    inOrder(root2, node2keys)
    allKeys = mergeLists(node1keys, node2keys)
    return BSTfromList (allKeys, 0, len(allKeys)-1)

c = Node(2)
b = Node(3)
a = Node(2)
a.left, a.right = c,b
c1 = Node(11)
b1 = Node(13)
a1 = Node(12)

mergeTwoBSTs(a,a1)
