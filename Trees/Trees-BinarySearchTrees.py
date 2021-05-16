class Treenode:
    key = None
    left = None
    right = None
    value = None

    def __init__(self, key, value=None):
        self.key = key
        self.value = value


class BinarySearch:
    def __init__(self, head=None):
        self.head = head

    def search(self, key):
        if self.head is None: return False

        curr = self.head
        while curr is not None:
            if key == curr.key:
                return True
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        return False

    def insert(self, key, value=None):
        newNode = Treenode(key, value)
        self.insertNode(newNode)
        return newNode

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        prev = None
        curr = self.head
        while curr is not None:
            prev = curr
            if newNode.key == curr.key:
                print("Error : Duplicate key found")
                return
            elif newNode.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if newNode.key < prev.key:
            prev.left = newNode
        else:
            prev.right = newNode
        return

    def min(self, curr):
        if curr is None: return None
        while curr.left is not None: curr = curr.left
        return curr.key

    def max(self, curr):
        if curr is None: return None
        while curr.right is not None: curr = curr.right
        return curr.key

    def successor(self, node):
        if self.head is None: return None
        # If right subtree, Successor is the Minimum (leftmost) of the right subtree
        if node.right:
            node = node.right
            while node.left is not None: node = node.left
            # print (f"Successor : ", node.key )
            return node
        # If not right subtree, Last node that turned left when moving from root to current element.
        else:
            curr = self.head
            ancestor = None
            while curr is not None:
                if node.key == curr.key:
                    # print(f"Successor : ", node.key)
                    return ancestor
                elif node.key < curr.key:
                    ancestor = curr
                    curr = curr.left
                else:
                    curr = curr.right
            return ancestor

    def predecessor(self, node):
        if self.head is None: return None
        # If left subtree, Successor is the Maximum (rightmost) of the right subtree
        if node.left:
            node = node.left
            while node.right is not None: node = node.right
            # print (f"Predecessor : ", node.key )
            return node
        # If not left subtree, Last node that turned right when moving from root to current element.
        else:
            curr = self.head
            parent = None
            while curr is not None:
                if node.key == curr.key:
                    # print(f"Predecessor : ", node.key)
                    return parent
                elif node.key < curr.key:
                    curr = curr.left
                else:
                    parent = curr
                    curr = curr.right
            return parent

    def delete(self, key):
        # Search for key and get the curr and prev node.
        # Code copied from search
        if self.head is None: return None
        prev = None
        curr = self.head
        while curr is not None:
            if key == curr.key:
                break
            elif key < curr.key:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        # If key not found
        if curr is None: return None

        # Prev will be None only if the key is found at the head.
        # Case 1 : If the curr node has both left and right nodes
        if curr.left is not None and curr.right is not None:
            # Find the successor and set the prev.
            prev = curr
            node = curr.right
            while node.left is not None:
                prev = node
                node = node.left
            # Swap values of curr and successor nodes
            curr.key, node.key = node.key, curr.key
            curr.value, node.value = node.value, curr.value
            # Deletion node is the successor node
            curr = node

        # Delete current node
        # Case 2 : If node is leaf node just delete it.
        child = None
        # Case 3 : One of the node needs to be deleted
        if curr.left is not None:
            child = curr.left
        elif curr.right is not None:
            child = curr.right
        # if curr node is head
        if prev is None:
            self.head = child
        # Set the parent node to child
        elif prev.left == curr:
            prev.left = child
        else:
            prev.right = child

        return self.head

    # Need to redo after learning DFS
    def print(self, node):
        if node is None: return
        def orderHelper(node, level=0):
            if node == None: return
            # print (f"Input : {node.val}, {result}")
            print (f"{level*'    '}Node : {node.key}")
            orderHelper(node.left, level+1)
            orderHelper(node.right, level+1)

        orderHelper(node, level=0)
        return

    def orderTraversal(self, node, order="inorder") :
        if node == None: return []
        order.lower()
        if order not in ("preorder", "inorder", "postorder") : return
        result = []

        def orderHelper(node, order):
            if node == None: return
            if order == "preorder" : result.append(node.key)
            # print (f"Input : {node.val}, {result}")
            orderHelper(node.left, order)
            if order == "inorder": result.append(node.key)
            orderHelper(node.right, order)
            if order == "postorder": result.append(node.key)

        orderHelper(node, order)
        return result

if __name__ == "__main__":
    btree = BinarySearch()
    node = btree.insert(10)
    node2 = btree.insert(3)
    node3 = btree.insert(11)

    btree.insert(1)
    btree.insert(7)
    btree.insert(13)
    btree.insert(5)
    btree.insert(8)
    btree.insert(12)
    btree.print(btree.head)
    #print (f"PreOrder : {btree.orderTraversal(btree.head, 'preorder')}")
    #print (f"InOrder : {btree.orderTraversal(btree.head, 'inorder')}")
    #print(f"InOrder : {btree.orderTraversal(btree.head, 'postorder')}")
    # print(btree.min(btree.head), btree.max(btree.head))
    # print("Successor", node.key, btree.successor(node).key)
    # print("Predecessor", node.key, btree.predecessor(node).key)
    # print("Successor", node2.key, btree.successor(node2).key)
    # print("Predecessor", node2.key, btree.predecessor(node2).key)
    # btree.delete(3)
    # print("Successor", node.key, btree.successor(node).key)
    # node = btree.insert(3)
    # print("Successor", node.key, btree.successor(node).key)
