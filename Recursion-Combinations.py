def generateAllCombinations(arr):
    if len(arr) == 0:
        return [arr]
    res = []

    def genAllHelper(idx, slate):
        # Exit condition
        if idx == len(arr):
            res.append(slate[:])
            return

        # Recursion condition
        genAllHelper(idx+1, slate)
        slate.append(arr[idx])
        genAllHelper(idx + 1, slate)
        slate.pop()

    genAllHelper(0, [])
    return res


def countAllCombinations(arr):
    if len(arr) == 0:
        return [arr]

    def countAllHelper(idx, slate):
        # Exit condition
        if idx == len(arr):
            return 1

        # Recursion condition
        x = countAllHelper(idx+1, slate)
        slate.append(arr[idx])
        y = countAllHelper(idx + 1, slate)
        slate.pop()
        return x + y

    return countAllHelper(0, [])


def generateKCombinations(arr, k):
    if len(arr) == 0:
        return [arr]
    res = []

    def genKHelper(idx, slate):
        # Exit condition
        if len(slate) == k:
            res.append(slate[:])
            return
        if idx == len(arr):
            return

        # Recursion condition
        genKHelper(idx + 1, slate)
        slate.append(arr[idx])
        genKHelper(idx + 1, slate)
        slate.pop()

    genKHelper(0, [])
    return res


if __name__ == "__main__":
    arr = [3, 6, 8, 10]
    result = generateAllCombinations(arr)
    print("Result : ", result, len(result))
    result = countAllCombinations(arr)
    print("Count : ", result)
    k = 2
    result = generateKCombinations(arr, k)
    print("Result : ", result, len(result))
    # import itertools
    #print ("Verify : ", itertools.groupby())
