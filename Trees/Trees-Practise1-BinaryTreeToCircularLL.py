"""
https://oj.interviewkickstart.com/view_test_problem/16069/64/
Convert a Binary Tree into a Circular Doubly Linked List
Problem Statement:
Write a function BTtoLL(TreeNode root) that takes a binary tree and rearranges its left_ptr and right_ptr pointers to make a circular doubly linked list out of the tree nodes in the in-order traversal order. The head of the list must be the leftmost node of the tree (since it is the first one in the in-order traversal) and the tail of the list must be the rightmost node of the tree. Tail’s “next” pointer must point to the head and head’s “previous” pointer must point to the tail (as circular doubly-linked lists go).
In the resultant data structure we will think of right_ptr as “next” pointer of the list and of left_ptr as the “previous” pointer of the list. Note that although the resultant data structure will consist of a bunch of TreeNode instances, it will not be a tree (because, as a graph, it will have cycles).
The function must not allocate any new TreeNode instances, it must not change existing TreeNodes’ values either. It must change left_ptr and right_ptr pointers of the existing TreeNodes to form the desired data structure.
The function must return a TreeNode instance which is the head of the resultant circular doubly-linked list. The function must not print anything to the standard output.
"""
# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def BTtoLL(root):
    if root == None : return None

    head = None
    prev_node = None
    def inOrderhelper(node):
        nonlocal head, prev_node
        # Any leaf
        if node.left_ptr : inOrderhelper(node.left_ptr)
        # Set leftmost node to head
        if head == None : head = node
        if prev_node :
            node.left_ptr = prev_node
            prev_node.right_ptr = node
        prev_node = node
        if node.right_ptr: inOrderhelper(node.right_ptr)
        return
    inOrderhelper(root)
    prev_node.right_ptr = head
    head.left_ptr = prev_node
    return head