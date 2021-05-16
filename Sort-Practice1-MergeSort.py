#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

def merge_sort(arr):
    if len(arr) < 2: return arr

    # Write your code here
    def merge_sort_helper(start, end):
        if start >= end: return
        mid = start + (end - start) // 2
        merge_sort_helper(start, mid)
        merge_sort_helper(mid + 1, end)
        # Merge left and right
        res = []
        i = start
        j = mid + 1
        while (i <= mid) and (j <= end):
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        if i <= mid:
            res.extend(arr[i:mid + 1])
        elif j <= end:
            res.extend(arr[j:end + 1])
        arr[start:end + 1] = res[:]
        return

    merge_sort_helper(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    arr = [1, 7, 5, 3, -1, 9]
    print(merge_sort(arr))
