"""
Number Of Paths In A Matrix
https://oj.interviewkickstart.com/view_test_problem/16334/131/
"""
def numberOfPaths(matrix):
    if len (matrix) == 0 or matrix[0][0] == 0 or matrix[-1][-1] == 0: return 0
    r = len(matrix)
    c = len(matrix[0])
    # DP Table 
    table = [ [0] * c for _ in range(r)]
    
    for i in range(r) :
        for j in range(c) :
            if matrix[i][j] == 1 : 
                if i > 0 and j > 0 : table[i][j] = table[i-1][j] + table[i][j-1]
                elif i == 0 and j > 0: table[i][j] = table[i][j-1]
                elif j == 0 and i > 0: table[i][j] = table[i-1][j]
                elif i == 0 and j == 0: table[i][j] = 1
    return table[-1][-1] % (10**9 + 7)

if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
    ]
    print (numberOfPaths(matrix))