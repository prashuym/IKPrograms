#
# Complete the 'sort_array' function below.
#
# The function accepts Character Array arr as parameter.
#

def sort_array(arr):
    lenArr = len(arr)
    if lenArr < 2 : return arr
    # Using count sort
    countMap = 128 * [0]
    for x in arr :
        print (x, ord(x))
        countMap[ord(x)] += 1

    # Recreate the array from countMap
    i = 0
    for num, count in enumerate(countMap):
        if count == 0 : continue
        char = chr(num)
        arr[i:i+count] = count*[char]
        i += count
    return arr

if __name__ == "__main__" :
    arr = ['a','z','i','#','&','l','c']
    arr = sort_array(arr)
    print (arr)