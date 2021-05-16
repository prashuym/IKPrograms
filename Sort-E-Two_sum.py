# Find the elements in the array arr which add up to value "sumK" , else return None.

# Approach using hashTable with time complexity - O(n) and aux space complexity - O(n)
def two_sum_hash(arr, sumK) :
    hashTable = {}
    for i in arr :
        # find the value for i which makes the sum
        reqNumber = sumK - i
        if reqNumber in hashTable : return i, reqNumber
        else : hashTable[i] = None
    print (hashTable)
    return None

# Approach using Pre-sorting as the initial step followed by element search.
# Time complexity - O(n + nlog n) and aux space complexity - o(1)
def two_sum_two_ptr(arr, sumK):
    arr.sort()   # Internally uses TimSort with n Log n
    i = 0
    j = len(arr) - 1
    while i < j :
        tempSum = arr[i] + arr[j]
        #print(i, j, sumK, tempSum, arr)
        if tempSum == sumK : return arr[i], arr[j]
        elif tempSum > sumK : j += 1
        else : i += 1

    return -1

if __name__ == "__main__" :
    arr = [8,1,2,5,4,7,5,3,9]
    sumK = 17
    print ( two_sum_hash(arr, sumK) )
    print(two_sum_two_ptr(arr, sumK))