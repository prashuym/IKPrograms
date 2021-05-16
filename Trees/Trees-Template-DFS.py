# Template for DFS for Trees and Graphs 
from collections import deque
def dfs_tree (root):
    '''
    root :  Rood node of the tree
    '''
    if root == None : return
    slate = []
    result = []
    def dfs(node, slate, result):
        # Base condition
        if node.left == node.right == None :
            return
        # Recursion condition
        # Do something - preorder 
        if node.left :
            dfs(node.left)
        if node.right :
            dfs(node.right)
        return 
    
    dfs(root, slate, result)
    return result

def dfs_graph(source, visited, adjList):
    visited[source] = 1
    for neighbour in adjList[source]:
        if visited[neighbour] != 1 :
            visited[neighbour] = 1
            dfs(neighbour, visited, adjList)
 
def dfs_graph(source, n, adjList):
    '''
    source : Source node of the tree
    n      : Number of vertices in the tree.
    adjList: Adjacency List/Map for the graph
    '''
    if source == None : return
    # Create adjacencyList 
    visitedNodes = [-1] * n
    dfs(source, visitedNodes, adjList)

    return
