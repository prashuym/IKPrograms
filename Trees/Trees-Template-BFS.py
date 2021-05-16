# Template for BFS for Trees and Graphs 
from collections import deque
def bfs_tree (root):
    '''
    root :  Rood node of the tree
    '''
    if root == None : return
    q = deque([root])
    while q :
        node = q.popleft()
        # if N-ary array : for n in node.children : 
        if node.left : 
            q.append(node.left)
        if node.right : 
            q.append(node.right)
        
        # Do something

    return

def bfs_tree_level (root):
    '''
    root :  Rood node of the tree
    '''
    if root == None : return
    q = deque([root])
    while q :
        numNodes = len(q)
        for _ in range(numNodes) :                  
            node = q.popleft()
            # if N-ary array : for n in node.children : 
            if node.left :  
                q.append(node.left)
            if node.right : 
                q.append(node.right)
        
            # Do something

    return

def bfs_graph (source, n, adjList):
    '''
    source : Source node of the tree
    n      : Number of vertices in the tree.
    adjList: Adjacency List/Map for the graph
    '''
    if source == None : return
    visitedNodes = [-1] * n
    visitedNodes[source] = 1
    q = deque([source])
    
    while q :
        node = q.popleft()

        for n in adjList[node] :
            if visitedNodes[n] == -1 :
                visitedNodes[n] = 1
                q.append(n)

        # Do something

    return