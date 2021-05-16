"""
https://oj.interviewkickstart.com/view_test_problem/15890/103/
"""
def findZeroSum(arr):
    # Write your code here.
    if len(arr) < 2: return []

    arr.sort()  # n log(n)
    res = []

    lenArr = len(arr)
    # print ("sorted ", arr)
    prevValue = None
    for i in range(lenArr - 1):
        curEle = arr[i]
        if curEle > 0 or curEle == prevValue: continue
        testHash = {}
        prevValue = curEle
        for j in range(i + 1, lenArr):
            if arr[j] in testHash: testHash[arr[j]] += 1
            else: testHash[arr[j]] = 1

            sumElement = - (curEle + arr[j])
            if (sumElement == arr[j]) and (testHash[sumElement] != 2): continue
            elif (sumElement !=arr[j] and testHash[arr[j]]>1) : continue

            if sumElement in testHash:
                res.append("%s,%s,%s" % (curEle, arr[j], sumElement))
            print("Enter: ", curEle, arr[j], sumElement, testHash, res)

    return res


if __name__ == "__main__" :
    arr = [-1,-1,0,0,0,0,2,2,2,1,1,8,-3, -4, -4]
    print (findZeroSum(arr))