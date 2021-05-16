'''
323 Number of connected components in a Undirected Graph
Given n nodes labeled from 0 o n-1 and list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1:
Input n = 5 and edges = [[0,1], [1,2], [3,4]]
Output = 2
Example 2:
Input n = 5 and edges = [[0,1], [1,2], [2,3], [3,4]]
Output = 1
'''

from collections import deque
def build_adjList(n, edge_list):
    adjList = [[] for i in range(n)]
    for src, dst in edge_list :
        adjList[src].append(dst)
        adjList[dst].append(src)
    return adjList

def bfs (src, visited_nodes, adjList, counter) :
    visited_nodes[src] = counter
    q = deque([src])
    while q :
        node = q.popleft()
        for neighbour in adjList[node] :
            if visited_nodes[neighbour] == -1 :
                visited_nodes[neighbour] = counter
                q.append(neighbour)

def dfs (node, visited_nodes, adjList, counter) :
    visited_nodes[node] = counter
    for neighbour in adjList[node] :
        if visited_nodes[neighbour] == -1 :
            dfs(neighbour, visited_nodes, adjList,counter)

def findConnectedComp(n, edgeList):
    adjList = build_adjList(n, edge_list)
    visited_nodes = [-1] * n
    counter = 0
    for n,v in enumerate(visited_nodes) :
        if v == -1 :
            counter += 1
            dfs (n, visited_nodes, adjList, counter)

    # for x in enumerate(visited_nodes) : print (x)
    return counter

if __name__ == "__main__" :
    n = 5
    edge_list = [[0,1], [1,2],[3,4]]
    result = findConnectedComp(n,edge_list)
    print (f"Result : {result}")
