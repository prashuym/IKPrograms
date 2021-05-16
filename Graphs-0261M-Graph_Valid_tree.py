'''
261.  Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1 :
Input : n = 5, and edges = [[0,1], [0,2], [0,3],[1,4]]
Output : True
Example 2 :
Input : n = 5, and edges = [[0,1], [1,2], [2,3], [1,3],[1,4]]
Output : False
'''
# Uses the standard Graph BFS/DFS template as in Graphs-0323M-Num_Connected_Undirected_graph.py
# The changes from the standard template are commented.
# Rules for Graph to be a valid Tree
# 1. There should be only one connected Tree.   More than one connected tree indicates broken trees.
# 2. Each node in the adjacency list/map should have only parent or new child nodes i.e., no visited nodes other than the parent.

from collections import deque
def build_adjList(n, edge_list):
    adjList = [[] for i in range(n)]
    for src, dst in edge_list :
        adjList[src].append(dst)
        adjList[dst].append(src)
    return adjList

def bfs (src, visited_nodes, parent, adjList, counter) :
    visited_nodes[src] = counter
    q = deque([src])
    while q :
        node = q.popleft()
        for neighbour in adjList[node] :
            if visited_nodes[neighbour] == -1 :
                # Store Parent information
                parent[neighbour] = node
                visited_nodes[neighbour] = counter
                q.append(neighbour)
            else :
                # If visited nodes is other than the parent then we have a circular loop and not a Tree
                if neighbour != parent[node]:  # Cross edge found
                    return False
    return True

def dfs (node, visited_nodes, parent, adjList, counter) :
    visited_nodes[node] = counter
    for neighbour in adjList[node] :
        if visited_nodes[neighbour] == -1 :
            # Store Parent information
            parent[neighbour] = node
            if dfs(neighbour, visited_nodes, parent, adjList,counter) == False:
                return False
        else :
            # If visited nodes is other than the parent then we have a circular loop and not a Tree
            if neighbour != parent[node] :  # Back edge found
                return False
    return True

def findValidTree(n, edgeList):
    adjList = build_adjList(n, edge_list)
    visited_nodes = [-1] * n
    parent = [-1] * n           # List to get the parent of a node.
    counter = 0
    for n,v in enumerate(visited_nodes) :
        if v == -1 :
            counter += 1
            # Handle Case - There should be only one connected Tree.
            # More than one connected tree indicates broken trees.
            if counter > 1 or bfs (n, visited_nodes, parent, adjList, counter) == False : return False

    # for x in enumerate(visited_nodes) : print (x)
    return True

if __name__ == "__main__" :
    n = 5
    edge_list = [[0,1], [0,2], [0,3],[1,4]]
    # edge_list = [[0,1], [1,2], [2,3], [1,3],[1,4]]
    result = findValidTree(n,edge_list)
    print (f"Result : {result}")
