from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createNodes (nodes):
    if not nodes : return None
    nodes = deque(nodes)
    root = TreeNode(nodes.popleft())
    q = deque([root])
    while q :
        numNodes = len(q)
        for _ in range(numNodes) :
            n = q.popleft()
            if n and len(nodes) > 1:
                nextNum = nodes.popleft()
                if nextNum: 
                    n.left = TreeNode(nextNum)
                    q.append(n.left)
                nextNum = nodes.popleft()
                if nextNum: 
                    n.right = TreeNode(nextNum)
                    q.append(n.right)
    return root

def printNodes (root):
    if not root : return None
    q = deque([root])
    level = 0
    while q :
        level += 1
        print (f"Level - {level} : ", end="")
        numNodes = len(q)
        for _ in range(numNodes) :
            n = q.popleft()
            print (f"{n.val} ",end="")
            if n.left : 
                print (f"(L-{n.left.val} ",end="")
                q.append(n.left)
            else : print (f"(L-none ",end="")
            if n.right :
                print (f"R-{n.right.val}) ", end="")
                q.append(n.right)
            else : print (f"R-none) ",end="")
            print (f"\t", end="")
        print (f"")    
    return root

if __name__ == "__main__":
    nodes = [1,2,3,4,None,6,7]
    root = createNodes(nodes)
    printNodes(root)

