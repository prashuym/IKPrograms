"""
https://oj.interviewkickstart.com/view_test_problem/15890/102/
"""

import heapq

# Complete the function below.
def topK(arr, k):
    topHeap = [arr[0]]
    topHash = {arr[0]: None}
    for i in arr:
        print (topHeap, topHash, i, k)
        if i in topHash: continue
        if len(topHeap) < k:
            topHeap.append(i)
            topHash[i] = None
            if len(topHeap) == k :
                print ("heapify")
                heapq.heapify(topHeap)
        elif i > topHeap[0]:
            heapq.heappush(topHeap, i)
            remI = heapq.heappop(topHeap)
            topHash.pop(remI)
            topHash[i] = None
            print("Remove", remI, topHeap, topHash, i, k)

    return topHeap

if __name__ == "__main__" :
    arr = [2,7,6,1,7,8,10,3,10,7,1,10,6,5,4]
    print (sorted(topK(arr, 4)))