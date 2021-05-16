"""
https://oj.interviewkickstart.com/view_test_problem/16068/86/
n Queen Problem
Given an integer n, find all the possible ways to position n queens on an n×n chessboard so that no two queens attack each other.
A queen in chess can move horizontally, vertically, or diagonally.
Do solve the problem using recursion first even if you see some non-recursive approaches.
"""

# Complete the function below.
def find_all_arrangements(n):
    res = []
    def validate_queen (slate, x, y):
        # print (slate, x, y)
        for Qx, Qy in enumerate(slate) :
            if (y == Qy) or (abs(x-Qx) == abs(y-Qy)):
                return False
        return True

    def  nqueenHelper(n, S, row, col, slate) :
        # print (n, row, len(slate), slate)
        if row == n :
            new_matrix = [["-" for x in range(n)] for y in range(n)]
            for x,y in enumerate(slate) :
                new_matrix[x][y]='q'
                new_matrix[x] = "".join(new_matrix[x])
            res.append(new_matrix)
            return
        for i in range(col, len(S)):
            # print ("Row-Column ; ", row,i,col, S, slate)
            if validate_queen (slate, row, S[i]) :
                slate.append(S[i])
                S[i], S[col] = S[col], S[i]
                pr = nqueenHelper(n, S, row+1, col+1, slate)
                S[i], S[col] = S[col], S[i]
                slate.pop()
    slate = []
    S = list(range(n))
    nqueenHelper(n,S,0,0,slate)
    return res

if __name__ == "__main__" :
    n = 12
    res = find_all_arrangements(n)
    print ("Result : ", res, len(res))