# def
#     for streamArray in arr:
#         arrPtr = streamPtr = 0
#         arrLen = len(res)
#         streamLen = len(streamArray)
#         newArray = []
#         while arrPtr < arrLen and streamPtr < streamLen:
#             # print (arrPtr, arrLen, streamPtr, streamLen, newArray)
#             if incOrder:
#                 if (res[arrPtr] <= streamArray[streamPtr]):
#                     newArray.append(res[arrPtr])
#                     arrPtr += 1
#                 else:
#                     newArray.append(streamArray[streamPtr])
#                     streamPtr += 1
#             else:
#                 if (res[arrPtr] >= streamArray[streamPtr]):
#                     newArray.append(res[arrPtr])
#                     arrPtr += 1
#                 else:
#                     newArray.append(streamArray[streamPtr])
#                     streamPtr += 1
#
#         newArray.extend(streamArray[streamPtr:])
#         newArray.extend(res[arrPtr:])
#         res = newArray
#
#     return res
#
def mergeArrays(arr):
    incOrder = False
    for tempArr in arr[:] :
        if tempArr[0] < tempArr[-1] :
            incOrder = True
            break

    res = []
    def mergeArrayRecurrsive(left, right):
        # print (left, right, incOrder)
        if left >= right: return arr[left]
        mid = left + ((right-left)//2)
        arrLeft = mergeArrayRecurrsive(left, mid)
        arrRight = mergeArrayRecurrsive(mid+1, right)
        # Merge the two arrays
        ptrLeft = ptrRight = 0
        lenLeft = len(arrLeft)
        lenRight = len(arrRight)
        res = []
        # print ("Left :", arrLeft, "Right :", arrRight)
        while ptrLeft < lenLeft and ptrRight < lenRight:
            # print(ptrLeft, lenLeft, ptrRight, lenRight, incOrder)
            if (incOrder == True and (arrLeft[ptrLeft] <= arrRight[ptrRight])) or (incOrder == False and (arrLeft[ptrLeft] >= arrRight[ptrRight])):
                res.append(arrLeft[ptrLeft])
                ptrLeft += 1
            else:
                res.append(arrRight[ptrRight])
                ptrRight += 1

        res.extend(arrLeft[ptrLeft:])
        res.extend(arrRight[ptrRight:])
        return res

        # mergeTwoArrays(arrLeft, arrRight)

    arrLen = len(arr)
    res = mergeArrayRecurrsive(0, len(arr)-1)

    print (res)
    return res


if __name__ == "__main__":
    arr = [ [9,9,9,9],
[9,9,9,9],
[9,9,9,9],
[9,9,9,10],
[9,9,9,9],
[9,9,9,9] ]
    res = mergeArrays (arr)
    print ("Result :", res)