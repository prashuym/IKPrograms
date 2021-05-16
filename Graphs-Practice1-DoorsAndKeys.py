'''
https://oj.interviewkickstart.com/view_test_problem/16188/119/

Shortest Path In 2D Grid With Keys And Doors
Given a two-dimensional grid of size n * m that represents a maze-like area, a start cell and a goal cell, you have to find the shortest path from the start to the goal.
You can go up, down, left or right from a cell, but not diagonally.
Each cell in the grid can be either land or water or door or key or start or goal.
You can travel on any cells but water.
Every key and every door belongs to a particular “type”. For example a key of type ‘a’ can open a door of type ‘A’ but not a door of type ‘B’. There can be more than one key of a particular type in the maze, all keys of one type are equivalent. Similarly there can be more than one door of any type. You cannot travel through a door unless you have picked up a key of the corresponding type before. A key is picked up by visiting its cell. If you have picked up a certain type of key, you can then travel through any doors of that type any number of times.
It is allowed to revisit a cell.

Constraints:
1 <= n, m <= 100
There will be exactly one start cell and one goal cell.
It is guaranteed that there exists a path from start to goal.
'a' <= key <= 'j'
'A' <= door <= 'J'

Sample Input:
grid = [
"...B",
".b#.",
"@#+."
]
Sample Output:
[
    [2, 0],
    [1, 0],
    [1, 1],
    [0, 1], 
    [0, 2],
    [0, 3],
    [1, 3],
    [2, 3],
    [2, 2]
]
'''
from collections import deque
def build_adjList(start, grid, keyring):
    adjList = []
    m = len(grid)
    n = len(grid[0])
    x, y = start
    new_pos = []
    #print (f"m - {m}, n - {n} {x+1} {y+1}")
    if x + 1 < m : new_pos.append((x+1, y))
    if x - 1 > -1: new_pos.append((x-1, y))
    if y + 1 < n : new_pos.append((x, y+1))
    if y - 1 > -1: new_pos.append((x, y-1))
    for newX, newY in new_pos :
        c = grid[newX][newY]
        newKeyring = keyring
        # If we hit a Door (ABCD...), check if we have a key
        if c == "#" : continue
        elif c.isupper():
            if keyring & (1 << ord(c)-ord('A')) == 0 :
                continue
        elif c.islower():
            newKeyring = keyring | (1 << ord(c)-ord('a'))
        adjList.append([(newX, newY), newKeyring])
    return adjList

def bfs (start, goal, grid) :
    # Initialize the variables
    visited_nodes = set()
    parent = {}           # List to get the parent of a node.
    keyring = 0

    # Set the values for the start.
    visited_nodes.add((start, keyring)) 
    parent[(start, keyring)] = None
    q = deque([(start, keyring)])
    
    while q :
        node, keyring = q.popleft()
        #print (f"Entering node : {node}, {keyring}")
        for neighbour,newKeyring in build_adjList(node, grid, keyring) :
            #print (f"\t Neighbour : {neighbour}, {newKeyring}")
            if neighbour == goal: 
                #print (f"Parent : {parent}, Neighbour : {neighbour}, Node : {node}, keyring : {keyring}")
                parentPath = deque()
                parentPath.appendleft(neighbour)
                cur = (node, keyring)
                while cur != None :
                    parentPath.appendleft(cur[0])
                    cur = parent[cur]
                return parentPath
                
            if (neighbour, newKeyring) not in visited_nodes :
                # Store Parent information
                parent[(neighbour, newKeyring)] = (node, keyring)
                visited_nodes.add((neighbour, newKeyring))
                q.append((neighbour, newKeyring))
    return []

def find_shortest_path(grid):
    counter = 0
    m = len(grid)
    n = len(grid[0])

    for x in range(m) :
        for y in range(n) :
            if grid[x][y] == "@" : start = (x,y)
            elif grid[x][y] == "+" : goal = (x,y)
    path = bfs (start, goal, grid)
    return path

if __name__ == "__main__" :
    grid = [
        "...B",
        ".b#.",
        "@#+.",
    ]
    result = find_shortest_path(grid)
    print (f"Result : {result}")

