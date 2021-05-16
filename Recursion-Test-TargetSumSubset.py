"""
https://oj.interviewkickstart.com/view_test_problem/16092/5/
Possible To Achieve Target Sum?
Given a set of integers and a target value k, find a non-empty subset that sums up to k.

Example One
Input: [2 4 8], k = 6
Output: True Because 2+4=6.

Example Two
Input: [2 4 6], k = 5
Output: False - Because no subset of numbers from the input sums up to 5.

Notes
Input Parameters: Function has two arguments: an array of integers (their order doesn’t matter) and the target value  k.
Output: Function must return a boolean value.
Constraints:
1 <= size of the input array <= 18
-10^17 <= elements of the array, k <= 10^17
"""

# Complete the function below.
import sys


def check_if_sum_possible(arr, k):
    if len(arr) == 0 : return False
    elif len(arr) == 1 : return arr[0] == k
    subset = []
    res = []
    # Slate is sum so far, Subset is elements passed down.
    def helper(k, idx, slate, subset):
        #print (k,idx,slate,subset, arr)
        #print("Subset :", subset)
        # Base condition
        if (subset and slate == k) :
            return True
        if idx == len(arr):
            return False
        subset.append(arr[idx])
        if helper(k, idx + 1, slate+arr[idx], subset): return True
        subset.pop()
        if helper(k, idx + 1, slate, subset): return True
        return False

    return helper(k, 0, 0, subset)

arr = [10,20, 30]
k =  40
res = check_if_sum_possible(arr, k)
print ("Result : ", res)