#
# Complete the merger_first_into_second function below.
#
def merger_first_into_second(arr1, arr2):
    lenArr1 = len(arr1)
    lenArr2 = len(arr2)
    arr1F = arr2F = len(arr1) - 1
    writeF = len(arr2) - 1
    while arr1F >= 0 and arr2F >= 0 :
        print (arr1F, arr2F, writeF, arr2, arr1)
        if arr1[arr1F] > arr2[arr2F] :
            arr2[writeF] = arr1[arr1F]
            arr1F -= 1
        else :
            arr2[writeF] = arr2[arr2F]
            arr2F -= 1
        writeF -= 1
    if arr1F >= 0 :
        arr2[0:arr1F+1] = arr1[0:arr1F+1]


if __name__ == "__main__" :
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6, 0, 0, 0]
    merger_first_into_second(arr1, arr2)
    print (arr2)