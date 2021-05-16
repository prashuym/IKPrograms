"""
Cut The Rope
https://oj.interviewkickstart.com/view_test_problem/16335/26/
https://leetcode.com/problems/integer-break/
"""
#
# Complete the max_product_from_cut_pieces function below.
#
def max_product_from_cut_pieces(n):
    # Handling custom case for 2 and 3
    if n == 2 or n ==3 : return n-1
    # DP table 
    table = [0] * (n+1)
    # Override values for 2 and 3
    table[2] = 2
    table[3] = 3
    table[4] = 4
    # For every value of i from 4 to n , back track and create the DP table entry
    # Then iterate down one step at a time to find the max value for every backward step
    # Exampe for 4 - Max (dp[4] * 1, dp[3] * 2, dp[2] * 1, dp [1] * 0  ) 
    for i in range(5,n+1):
        for j in range(1,4) :   
            table[i] = max(table[i], table[i-j] * j) % (10**9 + 7)
    return table

if __name__ == "__main__":
    print (max_product_from_cut_pieces(5))