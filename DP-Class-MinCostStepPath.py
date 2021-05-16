"""
You can climb a stair in one step or two steps at a time.  Each step you use has a cost associated with it.  
The start and stop steps do not have a cost.   What is the path to take for minimum steps.
"""
def minCost (costArray):
    costArray.append(0)
    costCache = [None] * len(costArray)
    # Setup base costs

    costCache[0] = costArray[0]
    costCache[1] = min(costCache[0] , 0) + costArray[1]
    for i in range(2,len(costArray)):
        # print (f"Cache : {costCache}")
        costCache[i] = min(costCache[i-1], costCache[i-2]) + costArray[i]
    return costCache[-1]

if __name__ == "__main__":
    costArray = [ 10, 15, 20, 50, 12]
    result = minCost(costArray)
    print (f"Result : {result}")