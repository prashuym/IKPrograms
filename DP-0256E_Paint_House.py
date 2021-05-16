'''
256. Paint House
https://leetcode.com/problems/paint-house/
'''
def paintHouse(costs) :
    if len(costs) == 0 : return 0
    r = len(costs)
    c = len(costs[0])
    colors = ["red", "blue", "green"]
    paintCost = 0
    prevIdx = -1
    costList = []
    for i in range(r) :
        minCost = float("inf")
        for j in range(c) :
            if prevIdx == j : continue
            if costs[i][j] < minCost :
                minCost = costs[i][j]
                prevIdx = j
        paintCost += minCost
        costList.append((i,colors[prevIdx],minCost))

    return paintCost, costList
    
if __name__ == "__main__":
    costs = [
        [17,2,17],
        [16,16,5],
        [14,3,19]
        ]
    result = paintHouse(costs)
    print (f"Result : {result}")
