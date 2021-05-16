"""
https://oj.interviewkickstart.com/view_test_problem/16313/125/
Minimum Coins
Given a variety of coin types defining a currency system, find the minimum number of coins required to express a given amount of money. Assume infinite supply of coins of every type. 
Example
Input: Coin types: [1, 3, 5]. Amount to express: 9.
Output: 3

Here are all the unique ways to express 9 as a sum of coins 1, 3 and 5:
1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 3
1, 1, 1, 1, 5
1, 1, 1, 3, 3
1, 3, 5
3, 3, 3
Last two ways use the minimal number of coins, 3.

Notes
Every input will include a coin of value 1. This guarantees that a solution will always exist.
There will be no duplicate coin types in the input.
"""
def minimum_coins(coins, value):
# Write your code here
    if value == 0 : return 0
    
    lenTable = max(coins) + 1
    # DP table 
    table = [0] * lenTable
    for i in range(1,value+1):
        minVal = value+1
        for c in coins :
            if i-c >= 0: 
                minVal = min(minVal, table[(i-c) % lenTable])
        if minVal != value+1 : table[i%lenTable] = minVal + 1    
        print(table)
    return table[(value) % lenTable]

if __name__ == '__main__':
    coins = [1,2,5]
    value = 5
    result = minimum_coins(coins, value)
    print (f"Result : {result}")

