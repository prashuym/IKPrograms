'''
https://oj.interviewkickstart.com/view_test_problem/16188/40/
Knight's Tour On A Chess Board
You are given a rows * cols chessboard and a knight that moves like in normal chess. Currently knight is at starting position denoted by start_row th row and start_col th col, and want to reach at ending position denoted by end_row th row and end_col th col.  The goal is to calculate the minimum number of moves that the knight needs to take to get from starting position to ending position.start_row, start_col, end_row and end_col are 0-indexed.

Example
Input:
rows = 5
cols = 5
start_row = 0
start_col = 0
end_row = 4
end_col = 1
Output: 3
3 moves to reach from (0, 0) to (4, 1):
(0, 0) -> (1, 2) -> (3, 3) -> (4, 1).
'''
from collections import deque

def knightMoves (xMax, yMax, x, y):
    moveList = []
    movements = [ (2,-1), (2,1), (-2,-1), (-2,1),
                  (1,2), (1,-2), (-1,2), (-1,-2),]
    # Left positions
    for m in movements :
        if (m[0] + x) > -1 and (m[0] + x) < xMax and (m[1] + y) > -1 and (m[1] + y) < yMax:
            moveList.append((x + m[0], y + m[1]))

    #print (f"{x} {y} : {moveList}")
    return moveList

def bfs (rows, cols, start_row, start_col, end_row, end_col):
    q = deque ()
    visited_list = []
    for x in range(rows) : visited_list.append([-1] * cols)
    visited_list[start_row][start_col] = 1
    q = deque([(start_row, start_col)])
    level = 0
    while q :
        level +=1
        nextQ = deque()
        for curR, curC in q :
            for r,c in knightMoves(rows, cols, curR, curC):
                # print (f"{level} : {curR} {curC} : {r} {c} ")
                if visited_list[r][c] != 1 :
                    visited_list[r][c] = 1
                    nextQ.append((r,c))
                    if r == end_row and c == end_col : return level
        q = nextQ
    return -1

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    if start_row == end_row and start_col == end_col : return 0
    return bfs(rows, cols, start_row, start_col, end_row, end_col)

if __name__ == "__main__":
    rows = 5
    cols = 5
    start_row = 0
    start_col = 0
    end_row = 4
    end_col = 1
    result = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)
    print (f"Result : {result}")
