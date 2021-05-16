# Find the path with the maximum value from source to destination. 
# Allowed movements are down and right.
def findMaxPath(grid):
    r = len(grid)
    c = len(grid[0])
    CacheData = [0] * c
    # Build initial data
    tempCount = 0
    CacheData[0] = grid[0][0]
    for i in range(1,c): CacheData[i] = CacheData[i-1] + grid[0][i]
    # Recursively find the Cache data for each row
    for i in range(1, r):
        CurData = [0] * c
        CurData[0] = CacheData[0] + grid[i][0]
        for j in range(1,c):
            CurData[j] = max(CurData[j-1], CacheData[j]) + grid[i][j]
        CacheData = CurData
    return CacheData[c-1]
    
if __name__ == "__main__" :
    grid = [
        [1,3,2,1],
        [3,4,2,5],
        [4,3,1,1],
    ]
    result = findMaxPath(grid)
    print (f"Result = {result}")