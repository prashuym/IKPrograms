"""
Equal Sum Subset Partition
https://oj.interviewkickstart.com/view_test_problem/16313/37/
Alt approach : https://www.geeksforgeeks.org/find-maximum-subset-sum-formed-by-partitioning-any-subset-of-array-into-2-partitions-with-equal-sum/?ref=rp
Given an array s of n integers, partition it into two non-empty subsets, s1 and s2, such that the sum of all elements in s1 is equal to the sum of all elements in s2. Return a boolean array of size n where i-th element is True if i-th element of s belongs to s1 and False if it belongs to s2. Any valid answer will be accepted. If such partitioning is not possible, return an empty array.

Example
Input: n = 6, s = [10, -3, 7, 2, 1, 3]
Output: [True, True, False, False, False, True]

There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:
s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)
s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]
s1 = [10] and s2 = [-3, 3, 7, 2, 1]
s1 = [-3, 3, 7, 2, 1] and s2 = [10]
s1 = [10, -3, 2, 1] and s2 = [7, 3]
s1 = [7, 3] and s2 = [10, -3, 2, 1]
"""
def equalSubSetSumPartition(s):
    n = len(s)

    if n == 0:
        return []

    total = sum(s)

    # if total is odd, no way to create equal sub-sets.
    if total % 2 == 1:
        return []

    target = total // 2
    res = [False] * n

    if target == s[0]:  # special base case
        res[0] = True
        return res

    dp = [set()]
    dp[0].add(s[0])
    found = False

    for i in range(1, n-1):

        dp.append(set())

        dp[i].add(s[i])
        for val in dp[i - 1]:
            dp[i].add(val)
            dp[i].add(val + s[i])

        if target in dp[i]:
            found = True
            break

    if not found:
        return []  # target val not attainable
    
    for i in reversed(range(len(dp))):
        if i != 0:
            if target in dp[i] and target not in dp[i - 1]:
                # this i'th element contributed to the sum
                res[i] = True
                target -= s[i]
                if target == 0:
                    break
        else:
            res[i] = True
    print (dp)
    return res

if __name__ == "__main__":
    s = [-3, 7, 2, 1, 3]
    result = equalSubSetSumPartition(s)
    print (f"Result : {result}")