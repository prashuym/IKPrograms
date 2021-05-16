'''
Find Order Of Characters From Alien Dictionary
https://oj.interviewkickstart.com/view_test_problem/16305/38/
'''
# Complete the function below.
from collections import defaultdict, deque
import sys
def genAdjList(words):
    adjList = defaultdict(list)
    adjList[words[0][0]] = []
    for i in range(len(words)-1):
        for j in range(len(words[i])):
            firstStr = words[i][j]
            secondStr = words[i+1][j]
            if firstStr != secondStr :
                adjList[firstStr].append(secondStr)
                break
    print ("ADJ: ", adjList, file=sys.stderr)
    return adjList

def dfs (node, adjList, visited_nodes, result):
    visited_nodes[node] = 1
    print("Node",  node, result, file=sys.stderr)
    for neighbour in adjList[node] :
        if visited_nodes[neighbour] == 0 :
            visited_nodes[neighbour] = 1
            dfs(neighbour, adjList, visited_nodes, result)
    result.appendleft(node)

def find_order(words):
    if len(words) == 0 : return ""
    #if len(words) == 1: return words[0][0]

    adjList = genAdjList(words)
    if len(adjList) == 0 : return []
    visited_nodes = defaultdict(int)
    result = deque()
    start_node = words[0][0] # adjList.keys()[0]
    for x in visited_nodes :
        if visited_nodes[x] == 0 :
            dfs (visited_nodes[x], adjList, visited_nodes, result)
    return "".join(result)

if __name__ == "__main__":
    words = ["c", "ba", "bba","bbc"]
    result = find_order(words)
    print (f"Result : {result}")