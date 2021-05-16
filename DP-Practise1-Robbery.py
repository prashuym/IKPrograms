"""
https://oj.interviewkickstart.com/view_test_problem/16313/33/
Robbery 
There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses, but he cannot steal in two adjacent houses because the owner of a stolen house will tell his two neighbors on the left and right side. What is the maximal stolen value?
For example, if there are four houses with values [6, 1, 2, 7], the maximal stolen value is 13, when the first and fourth houses are stolen.

Example One
Input: values = [6, 1, 2, 7]
Output: 13
Steal from the first and the last house.

Example Two
Input: values = [1, 2, 4, 5, 1]
Output: 7
Steal from the second and the fourth house.

Notes
Input Parameters: You will be given an array of integer values, containing the value in each house.
Output: Return an integer max, denoting the maximum possible robbery.

Constraints:
1 <= n <= 10^5
1 <= values[i] <= 10^4
"""
def maxStolenValue(values):
    lenValues = len(values)
    if lenValues == 0 : return 0
    elif lenValues == 1 : return values[0]
    elif lenValues == 2 : return max(values)

    # DP table of len of values
    table = [0] * 3

    # 1st table value will be same as itself
    prev2 = values[0] 
    prev1 = max(values[:2])
    
    for i in range(2, lenValues) :
        prev1, prev2 = max(prev2 + values[i], prev1), prev1
            
    return prev1

if __name__ == "__main__":
    #values =  [6,1,6,1,1,10,1,8,3,2,7,3]
    #values =  [6, 1, 2, 7]
    #values = [1, 2, 4, 5, 1]
    values = [3,5,7,2,2,3,8,2,7,7,7,3,2]

    result = maxStolenValue(values)
    print (f"Result : {result}")




