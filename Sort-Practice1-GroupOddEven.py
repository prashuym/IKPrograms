# " https://oj.interviewkickstart.com/view_test_problem/15890/101/"
# Complete the function below.

def solve(arr):
    lenArr = len(arr)
    ptrEven = ptrOdd = 0
    while ptrOdd < lenArr:
        if arr[ptrOdd] % 2 == 0:
            arr[ptrEven], arr[ptrOdd] = arr[ptrOdd], arr[ptrEven]
            ptrEven += 1
            ptrOdd += 1
        else:
            ptrOdd += 1

    return arr


def solve2(arr):
    ptrEven = 0
    ptrOdd = len(arr) - 1
    while ptrEven <= ptrOdd:
        if (arr[ptrEven] % 2 == 1) and (arr[ptrOdd] % 2 == 0):
            arr[ptrEven], arr[ptrOdd] = arr[ptrOdd], arr[ptrEven]
            ptrEven += 1
            ptrOdd -= 1
        if (arr[ptrEven] % 2 == 0):
            ptrEven += 1
        elif (arr[ptrOdd] % 2 == 1):
            ptrOdd -= 1

    return arr

if __name__ == "__main__":
    arr = [1,2,3,4]
    print (solve2(arr))