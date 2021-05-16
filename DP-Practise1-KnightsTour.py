"""
https://oj.interviewkickstart.com/view_test_problem/16313/31/
Knight's tour!
Given a phone keypad as shown below:
1 2 3
4 5 6
7 8 9
– 0 –
How many different phone numbers of given length can be formed starting from the given digit? The constraint is that the movement from one digit to the next is similar to the movement of the Knight in chess.
For example if we are at 1 then the next digit can be either 6 or 8, if we are at 6 then the next digit can be 1, 7 or 0.
Repetition of digits is allowed, e.g. 1616161616 is a valid number.
The problem requires us to just give the count of different phone numbers and not necessarily list the numbers.
Find a polynomial-time solution, based on Dynamic Programming.

Example One
Input: startdigit = 1, phonenumberlength = 2
Output: 2
Two possible numbers of length 2: 16, 18.

Example Two
Input: startdigit = 1, phonenumberlength = 3
Output: 5
The possible numbers of length 3: 160, 161, 167, 181, 183
"""
from collections import defaultdict
def numPhoneNumbers(startdigit, phonenumberlength):
    if phonenumberlength in (0,1) : return phonenumberlength
    numDigits = 10

    knightMoves = [
        (4,6),   # 0
        (6,8),   # 1
        (7,9),   # 2
        (4,8),   # 3
        (3,9,0), # 4
        (),      # 5    
        (0,1,7),   # 6
        (2,6),   # 7
        (1,3),   # 8
        (4,2)    # 9 
        ]
    # DP Table 
    table = defaultdict(int)

    table[startdigit] = 1
    for i in range(2,phonenumberlength+1):
        items = table.items()
        table = defaultdict(int)
        for j,n in items:
            for val in knightMoves[j] : table[val] += n 
    return sum(table.values())

if __name__ == "__main__":
    startdigit = 6
    phonenumberlength = 20
    result = numPhoneNumbers(startdigit, phonenumberlength)
    print (f"Result : {result}")