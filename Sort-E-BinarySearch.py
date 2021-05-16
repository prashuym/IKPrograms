# class Search :
#    __slots__ = ("arr", "searchValue")

def binarySearch(arr, left, right, searchValue):
    print (arr, left, right, searchValue)
    if right < left : return -1
    mid = left + (right-left)//2
    if arr[mid] == searchValue : return mid
    elif arr[mid] > searchValue :
        return binarySearch(arr, left, mid-1, searchValue)
    else :
        return binarySearch(arr, mid+1, right, searchValue)

if __name__ == "__main__" :
    arr = [2,4,6,7,9]
    print (binarySearch(arr, 0, len(arr), 7), arr.index(7))
