# Complete the function below.

# For your reference:
#

# ---- Not working --- Needs to be fixed.
from collections import defaultdict, deque


class Node:
   def __init__(self):
       self.val = 0
       self.neighbours = []

def dfs(node, visited_nodes, childNodes):
    print("Visit : ", node.val, childNodes, visited_nodes)
    for neighbour in node.neighbours:
        if visited_nodes[neighbour.val] == 0:
            childNode = Node()
            childNode.val = neighbour.val
            childNode.neighbours = [node]
            childNodes.append(childNode)
            visited_nodes[neighbour.val] = 1
            print("Created : ", childNode.val, childNode.neighbours[0].val)
            dfs(neighbour, visited_nodes, childNodes)

    return childNodes[-1]


def print_dfs(node, visited_nodes):
    for neighbour in node.neighbours:
        print(f"Visited : {node.val} (Neighbour :{neighbour.val})")
        if visited_nodes[neighbour.val] == 0:
            visited_nodes[neighbour.val] = 1
            print_dfs(neighbour, visited_nodes)
    return

def build_other_graph(node):
    visited_nodes = defaultdict(int)
    return dfs(node, visited_nodes, [])

if __name__ == "__main__" :
    a = Node()
    a.val = "1"
    b = Node()
    b.val = "2"
    c = Node()
    c.val = "3"
    a.neighbours = [b]
    b.neighbours = [c]
    c.neighbours = [a]
    visited_nodes = defaultdict(int)
    c = build_other_graph(a)
    print (c, c.val, c.neighbours[0].val, len(c.neighbours))
    c = c.neighbours[0]
    print(c, c.val, c.neighbours[0].val, len(c.neighbours))
    c = c.neighbours[0]
    print(c, c.val, c.neighbours[0].val, len(c.neighbours))
    c = c.neighbours[0]
    print(c, c.val, c.neighbours[0].val, len(c.neighbours))
    c = c.neighbours[0]
    print(c, c.val, c.neighbours[0].val, len(c.neighbours))